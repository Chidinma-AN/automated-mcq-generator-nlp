import nltk
from utils.mcq_generator import generate_mcqs

# Download NLTK data once
nltk.download('punkt')
nltk.download('stopwords')

# Read input text
with open("data_science.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Generate questions
mcqs = generate_mcqs(text)

# Display questions
for i, q in enumerate(mcqs):
    print(f"\nQ{i+1}: {q['question']}")
    for j, opt in enumerate(q['options']):
        print(f"  {chr(65 + j)}. {opt}")
    print(f"Answer: {q['answer']}")
