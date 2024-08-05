# test_dependencies.py
import torch
from sentence_transformers import SentenceTransformer

print(torch.__version__)
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully")
