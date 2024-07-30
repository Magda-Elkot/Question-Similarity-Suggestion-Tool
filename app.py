from flask import Flask, render_template, request  # Import necessary Flask modules
from services.data_service import load_data  # Import function to load data from file
from services.model_service import find_similar_questions  # Import function to find similar questions

app = Flask(__name__)  # Create a new Flask web application instance

# Load the input and suggested questions data
data = load_data()

@app.route('/', methods=['GET', 'POST'])  # Define the route for the home page, accepting both GET and POST requests
def index():
    similar_questions = []  # Initialize an empty list to hold similar questions
    if request.method == 'POST':  # Check if the request method is POST (form submission)
        query = request.form['query']  # Get the query input from the submitted form
        similar_questions = find_similar_questions(query, data, top_k=3)  # Find similar questions based on the user query
    return render_template('index.html', similar_questions=similar_questions)  # Render the HTML template with the similar questions

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
