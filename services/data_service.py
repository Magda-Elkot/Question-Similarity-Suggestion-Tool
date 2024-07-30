import json

def load_data(file_path='data/questions.json'):
    """
    Loads the questions data from a JSON file.

    Parameters:
    file_path (str): The path to the JSON file. Default is 'data/questions.json'.

    Returns:
    tuple: A tuple containing two lists:
        - The first list contains the input questions.
        - The second list contains the suggested questions corresponding to each input question.
    """
    # Open the JSON file in read mode
    with open(file_path, 'r') as file:
        # Parse the JSON content into a Python dictionary
        data = json.load(file)
    
    # Return the input questions and suggested questions from the dictionary
    return data['Input Question'], data['Suggested Questions']
