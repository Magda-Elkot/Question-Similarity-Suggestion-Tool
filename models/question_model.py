from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class QuestionModel:
    def __init__(self, questions):
        self.questions = questions
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(questions)
    
    def find_similar(self, query, top_k=3):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = linear_kernel(query_vector, self.question_vectors).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-top_k-1:-1]
        return [self.questions[i] for i in related_docs_indices]
