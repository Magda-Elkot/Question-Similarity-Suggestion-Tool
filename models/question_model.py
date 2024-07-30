# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Define the QuestionModel class
class QuestionModel:
    def __init__(self, questions):
        """
        Initialize the QuestionModel with a list of questions.

        :param questions: List of questions (strings) to be used for similarity comparison.
        """
        self.questions = questions  # Store the list of questions
        self.vectorizer = TfidfVectorizer()  # Initialize a TfidfVectorizer
        # Fit the vectorizer on the questions and transform them into TF-IDF vectors
        self.question_vectors = self.vectorizer.fit_transform(questions)
    
    def find_similar(self, query, top_k=3):
        """
        Find the top_k questions most similar to the query.

        :param query: The input query string for which to find similar questions.
        :param top_k: The number of top similar questions to return.
        :return: List of top_k similar questions.
        """
        # Transform the query into a TF-IDF vector using the same vectorizer
        query_vector = self.vectorizer.transform([query])
        # Compute cosine similarities between the query vector and all question vectors
        cosine_similarities = linear_kernel(query_vector, self.question_vectors).flatten()
        # Get the indices of the top_k questions with the highest similarity scores
        related_docs_indices = cosine_similarities.argsort()[:-top_k-1:-1]
        # Return the list of top_k similar questions using the computed indices
        return [self.questions[i] for i in related_docs_indices]
