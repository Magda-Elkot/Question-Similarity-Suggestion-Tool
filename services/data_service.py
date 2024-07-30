import json

def load_data(file_path='data/questions.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['Input Question'], data['Suggested Questions']
