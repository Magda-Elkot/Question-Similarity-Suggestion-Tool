from sentence_transformers import SentenceTransformer, util
import torch

class QuestionModel:
    def __init__(self, questions, model_name='all-MiniLM-L6-v2'):
        """
        Initialize the QuestionModel with a list of questions and a pre-trained model.

        Parameters:
        - questions (list of str): The list of questions to encode and compare.
        - model_name (str): The name of the pre-trained SentenceTransformer model to use (default is 'all-MiniLM-L6-v2').
        """
        # Store the list of questions
        self.questions = questions

        # Load the SentenceTransformer model with the specified model name
        self.model = SentenceTransformer(model_name)

        # Encode the list of questions into embeddings using the model
        self.question_embeddings = self.model.encode(questions, convert_to_tensor=True)
    
    def find_similar(self, query, top_k=3):
        """
        Find and return a list of questions similar to the given query.

        Parameters:
        - query (str): The question or query for which similar questions are to be found.
        - top_k (int): The number of top similar questions to return (default is 3).

        Returns:
        - list of tuples: A list of tuples where each tuple contains a similar question and its cosine similarity score.
        """
        # Encode the query into an embedding using the model
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        # Compute cosine similarities between the query embedding and the question embeddings
        cosine_similarities = util.pytorch_cos_sim(query_embedding, self.question_embeddings).flatten()

        # Get indices of the top_k most similar questions
        related_docs_indices = cosine_similarities.argsort(descending=True)[:top_k]

        # Retrieve the similar questions and their similarity scores
        similar_questions = [(self.questions[i], cosine_similarities[i].item()) for i in related_docs_indices]

        # Return the list of similar questions and scores
        return similar_questions
