# API Development and Documentation Final Project

## Trivia App

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## API Documentaion

### Getting Started

- App is set to run locally and is currently in development. Backend is hosted at the localhost address
- No API key is required to access the API

### API Endpoints

#### GET/categories

- Returns all availabe categories
- Response

```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
  }

```

#### GET/questions

- Returns a list of questions, 10 questions pew page
- URL http://127.0.0.1:5000/questions
- Response:

```bash
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": null,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 18
}
```

#### POST /questions

- create new questions
- URL: http://127.0.0.1:5000/questions
- Arguments: Question, answer, category, diffculty

- JSON format:

```bash
{
  "question": "What is the largest country"
  "answer": "Russia",
  "category": "3",
  "difficulty": 2,
}
```

- Response

```bash
{
"success": True,

"created": 20
            }
```

#### POST /questions/search

- Find a question buy searching the question body
- Returns any substring found
- Arguments: searchTerm
- Response:

```bash
    {
"success": True,
"questions": [],
"total_questions: 8
    }
```

#### GET /categories/int:id/questions

- Returns questions that belongs to a certion category, Given an category ID
- URL sample http://127.0.0.1:5000/categories/1/questions
- Response:

```bash
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}

```

#### DELETE /questions/int:question_id

- Deletes a guestion givin an ID
- URL smaple http://127.0.0.1:5000/questions/18
- Response:

```bash
{
  "deleted_id": 18,
  "success": true
}
```

#### POST /quizzes

- Returns a list of questions to play a quiz game
- URL POST http://127.0.0.1:5000/quizzes
- Arguments: quiz_category, previous_questions
- Response:

```bash
{
{
  "success": true,
  "question": []
}
}
```

##

### Error handling

The API will return the following errors:

- 404: Resource Not Found
- 400 : Bad Request
- 405 : method not allowed
- 422 : unprocessable

Errors are return in the following format:

```bash
{
    "success": False,
     "error": 404,
     "message": "resource not found"
     }
```

##

### Screenshots

![alt text](cd0037-API-Development-and-Documentation-project\screenshots\1.png)
![alt text](cd0037-API-Development-and-Documentation-project\screenshots\2.png)
