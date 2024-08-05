import sys
import os

# Add the parent directory of the current script to the system path to enable importing from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the QuestionModel class from the models.question_model module
from models.question_model import QuestionModel

def find_similar_questions(query, data, top_k=3):
    """
    Find and return a list of questions similar to the given query.

    Parameters:
    - query (str): The question or query for which similar questions are to be found.
    - data (tuple): A tuple containing:
        - input_questions (list of str): The list of questions to compare against.
        - suggested_questions (list of str): A list of suggested questions (not used in this function).
    - top_k (int): The number of top similar questions to return (default is 3).

    Returns:
    - list of str: A list of the top_k most similar questions to the query.
    """
    # Unpack the data tuple into input_questions and suggested_questions
    input_questions, suggested_questions = data

    # Initialize the QuestionModel with the list of input questions
    model = QuestionModel(input_questions)

    # Find similar questions to the query; get one extra to handle exact matches
    similar_questions_with_scores = model.find_similar(query, top_k + 1)

    # Filter out questions that are exact matches (score < 1.0) and select the top_k questions
    similar_questions = [q for q, score in similar_questions_with_scores if score < 1.0][:top_k]

    # Return the list of similar questions
    return similar_questions
