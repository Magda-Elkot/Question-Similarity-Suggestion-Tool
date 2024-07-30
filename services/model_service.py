import sys
import os

# Add the parent directory to the system path
# This allows Python to find and import modules located in the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the QuestionModel class from the models.question_model module
# This class is used to handle question similarity computations
from models.question_model import QuestionModel

def find_similar_questions(query, data, top_k=3):
    """
    Finds the top K similar questions to a given query.

    Parameters:
    query (str): The question or text for which similar questions are to be found.
    data (tuple): A tuple containing two lists:
                  - The first list contains input questions.
                  - The second list contains suggested questions corresponding to each input question.
    top_k (int): The number of top similar questions to return. Default is 3.

    Returns:
    list: A list of the top K similar questions to the given query.
    """
    # Unpack the tuple into two separate lists
    input_questions, suggested_questions = data
    
    # Create an instance of the QuestionModel with the input questions
    model = QuestionModel(input_questions)
    
    # Find the top K similar questions to the provided query
    similar_questions = model.find_similar(query, top_k)
    
    # Return the list of similar questions
    return similar_questions
