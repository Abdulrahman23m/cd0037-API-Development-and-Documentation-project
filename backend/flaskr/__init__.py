import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_question(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    question = [question.format() for question in selection]
    current_books = question[start:end]

    return current_books


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    with app.app_context():
        setup_db(app)
    CORS(app)


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.route("/categories")
    def get_categories():
        selection = Category.query.order_by(Category.id).all()

        if len(selection)==0:
            abort(404)

        return jsonify({
            "success": True,
            "categories": {category.id: category.type for category in selection},
            "total_categories":len(selection)
        })

    @app.route("/questions")
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_question(request,selection)
        if len(current_questions)==0:
            abort(404)
        categories = Category.query.order_by(Category.id).all()
        print() 
        return jsonify({
            "success": True,
            "questions": current_questions,
            "total_questions":len(selection),
            "categories": {category.id: category.type for category in categories},
            "currentCategory": None
        })

    @app.route('/questions/<int:question_id>', methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            print(question)

            if question is None:
                abort(404)

            question.delete()

            return jsonify({"success": True})
        except:
            abort(422)


    @app.route('/questions',methods=['POST'])
    def add_question():
        body = request.get_json()
        print(body)
        new_question = body.get('question',None)
        new_answer = body.get('answer',None)
        new_category = body.get('category',None)
        new_difficulty = body.get('difficulty',None)
        print(new_question)

        try:
            question = Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty)
            question.insert()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_question(request,selection)
            if len(current_questions)==0:
                abort(404)

            return jsonify({
            "success": True,

            "created": question.id
            })
        except:
            abort(422)

    @app.route('/questions/search', methods=["POST"])
    def search_question():
        seearch_term = request.get_data()

        print(seearch_term)
        questions = Question.query.filter(Question.question.contains("title")).all()
        if len(questions)==0:
            abort(404)
        question = [question.format() for question in questions]
        return jsonify({
            'success': True,
            "questions":question,
            "total_questions": len(question),
        })
    @app.route('/categories/<int:id>/questions')
    def get_category_questions(id):
        questions = Question.query.filter(Question.category == id).all()
        if len(questions)==0:
            abort(404)
        question = [question.format() for question in questions]
        category = Category.query.get(id)

        return jsonify({
            'success': True,
            "questions":question,
            "total_questions": len(question),
            "current_category": category.type

        })

    @app.route('/quizzes', methods=['POST'])
    def get_quiz():
        # get the JSON object to check category and the previous questions
        request_data = request.get_json()

        previous_questions = request_data.get('previous_questions',[])
        quiz_category=request_data.get('quiz_category')

        if quiz_category is None:
            abort(400)
        #check if all categories has been selected 
        if quiz_category['id']==0:
            questions = Question.query.filter(Question.id.notin_(previous_questions)).limit(1).one_or_none()
        else:
            questions = Question.query.filter_by(category = quiz_category['id']).filter(Question.id.notin_(previous_questions) ).limit(1).one_or_none()
        if len(questions.format())==0:
            abort(404)
        return jsonify({"success": True, "question": questions.format()})


    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """


    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )
    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )
    return app

