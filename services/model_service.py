import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.question_model import QuestionModel

def find_similar_questions(query, data, top_k=3):
    input_questions, suggested_questions = data
    model = QuestionModel(input_questions)
    similar_questions = model.find_similar(query, top_k)
    return similar_questions
