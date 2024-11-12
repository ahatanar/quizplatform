# src/models/quiz_model.py
from src.database import db

# INCOMPLETE: Define the QuizModel class
# TODO: Create a class named QuizModel that inherits from db.Model
class QuizModel(db.Model):
    # INCOMPLETE: Set up the table name
    # TODO: Define `__tablename__` as 'quizzes'
    
    # INCOMPLETE: Define table columns
    # TODO: Define an integer primary key column named `id`
    # TODO: Define a string column named `title` that cannot be null
    # TODO: Define a column named `questions` with PickleType to store a list
    
    def __init__(self, title, questions):
        # INCOMPLETE: Initialize the model with title and questions
        # TODO: Assign `self.title` and `self.questions` with `title` and `questions`
        pass  # REMOVE when implementing

    def save(self):
        # INCOMPLETE: Save the quiz to the database
        # TODO: Use `db.session.add(self)` and `db.session.commit()` to save the instance
        pass  # REMOVE when implementing

    @classmethod
    def get_quiz(cls, quiz_id):
        # INCOMPLETE: Retrieve a quiz by its ID
        # TODO: Use `cls.query.get(quiz_id)` to retrieve a quiz and return it
        pass  # REMOVE when implementing
