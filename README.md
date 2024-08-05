# Question-Similarity-Suggestion-Tool
# Project Overview

The Question Similarity Suggestion Tool is a web application designed to suggest similar questions based on a user's input. The application leverages the TF-IDF (Term Frequency-Inverse Document Frequency) model to compute the similarity between the user's query and a set of pre-defined questions stored in a JSON file. The goal is to provide users with relevant suggestions that match their queries, enhancing their experience by offering useful and related information.

# Project Structure


### Description of Key Components

- **app.py**: Contains the Flask application with routes for handling HTTP requests.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **data/questions.json**: Contains the dataset with questions used for similarity computation.
- **models/question_model.py**: Implements the logic for computing question similarity using the Sentence Transformer model.
- **services/data_service.py**: Contains logic for loading and preparing data from `questions.json`.
- **services/model_service.py**: Contains logic for initializing the model and computing similarities between questions.
- **templates/index.html**: HTML template for the web interface where users interact with the application.
- **test_dependencies.py**: Script to test the installation of PyTorch and SentenceTransformer.
- **static/css/styles.css**: Contains CSS styles to enhance the visual appearance of the web interface.




# Detailed Project Breakdown

## app.py
- **Purpose**: Contains the Flask application with routes for handling HTTP requests.
- **Goal**: Serve as the entry point for the web application, managing user requests and routing them to the appropriate service functions.
- **Advantage**: Centralizes route definitions and application logic, making it easier to manage and understand the application's flow. Helps in separating the web interface from the business logic.

  ![image](https://github.com/user-attachments/assets/908ea142-f1b3-40ec-8683-5d47692e78e6)


  ![image](https://github.com/user-attachments/assets/012b5c77-f63f-477d-831f-fe60ce868d5b)


## requirements.txt
- **Purpose**: Lists all Python dependencies required for the project.
- **Goal**: Ensure that all necessary libraries are installed and configured correctly in the virtual environment.
- **Advantage**: Simplifies setting up the development environment by providing a single file to install all dependencies, ensuring consistency across different setups.

## data/questions.json
- **Purpose**: Contains the dataset with questions used for similarity computation.
- **Goal**: Provide a structured data source in JSON format that can be easily read and processed.
- **Advantage**: JSON is a lightweight and easy-to-parse format, making it convenient for storing and retrieving structured data.

## models/question_model.py
- **Purpose**: IImplements the logic for computing question similarity using the Sentence Transformer model.
- **Goal**: Define a class QuestionModel to handle text vectorization with Sentence Transformers and similarity calculations.
- **Advantage**: Sentence Transformers capture the semantic meaning of sentences, providing more accurate and context-aware similarity comparisons.

## services/data_service.py
- **Purpose**: Contains logic for loading and preparing data from `questions.json`.
- **Goal**: Read and preprocess the data to be used by the model.
- **Advantage**: Separates data handling from the model logic, making it easier to modify or extend data processing without impacting the model. Enhances code readability and maintainability.

## services/model_service.py
- **Purpose**: Contains logic for initializing the model and computing similarities between questions.
- **Goal**: Use the `QuestionModel` class to perform similarity computations and provide recommendations.
- **Advantage**: Encapsulates the model-related functionality, making it easier to manage and extend. Provides a clear interface for interacting with the model and computing results.

## templates/index.html
- **Purpose**: HTML template for the web interface where users interact with the application.
- **Goal**: Provide a user-friendly interface for submitting queries and displaying results.
- **Advantage**: Separates the presentation layer from the application logic, allowing for easier modifications to the user interface without affecting the backend.

## static/css/styles.css
- **Purpose**: Contains CSS styles to enhance the visual appearance of the web interface.
- **Goal**: Style the HTML elements to create a visually appealing and user-friendly interface.
- **Advantage**: Allows for customization of the web interface's look and feel, improving user experience. Keeping styles in a separate file promotes modularity and ease of maintenance.

# Advantages of Using Sentence Transformers
- **Captures Semantic Meaning**: Sentence Transformers generate embeddings that reflect the context and meaning of sentences, enabling more accurate similarity comparisons.
- **Context-aware**: Better at understanding nuances and relationships between words compared to TF-IDF and CountVectorizer.
- **Improves Accuracy**: Provides more relevant and precise similarity comparisons, enhancing the user experience by suggesting more appropriate related questions.


# Model Architecture and Block Diagram
## Model Architecture
The Sentence Transformer model used in this project is based on transformer architecture, which encodes sentences into dense vector representations. These vectors capture the semantic meaning of the sentences.

![image](https://github.com/user-attachments/assets/3b9fb326-233d-473c-873b-30c698f028d9)

## Block Diagram
The system is composed of several key components:

![image](https://github.com/user-attachments/assets/259c0863-d89c-4730-8d63-12d2c157ed42)


# Summary
The purpose of the Question Similarity Suggestion Tool is to provide an easy-to-use web application that suggests similar questions based on user input, leveraging the advanced capabilities of Sentence Transformers for text similarity tasks. The project structure is designed to be modular and maintainable, ensuring a clear separation of concerns and enhancing both development and user experience.

