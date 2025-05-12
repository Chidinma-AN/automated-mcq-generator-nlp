# 🧠 Automated MCQ Generator using NLP

This beginner-friendly Python project generates multiple-choice questions from any text file using NLP techniques like TF-IDF and N-grams.

## 📌 Features
- Extracts key phrases using TF-IDF
- Generates 3 realistic MCQs per sentence
- Each question includes 4 options (1 correct, 3 distractors)
- Ensures the answer doesn’t appear in the question

## 🛠 Setup

```bash
git clone https://github.com/Chidinma-AN/automated-mcq-generator-nlp.git
cd automated-mcq-generator
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
