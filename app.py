from flask import Flask, render_template, request
from services.data_service import load_data
from services.model_service import find_similar_questions

app = Flask(__name__)

# Load data
data = load_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    similar_questions = []
    if request.method == 'POST':
        query = request.form['query']
        similar_questions = find_similar_questions(query, data, top_k=3)
    return render_template('index.html', similar_questions=similar_questions)

if __name__ == '__main__':
    app.run(debug=True)
