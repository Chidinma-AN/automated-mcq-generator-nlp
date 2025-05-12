import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

stop_words = set(stopwords.words('english'))

def extract_keywords(text, n=2, top_k=30):
    vectorizer = TfidfVectorizer(ngram_range=(1, n), stop_words='english')
    X = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), X.toarray()[0])
    sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)
    return [kw[0] for kw in sorted_keywords[:top_k]]

def generate_question(sentence, keyword):
    # Clean exact keyword match
    keyword_cleaned = keyword.strip().lower()
    if keyword_cleaned not in sentence.lower():
        return None, None, None

    # Replace only first occurrence
    index = sentence.lower().find(keyword_cleaned)
    question = sentence[:index] + "________" + sentence[index+len(keyword_cleaned):]

    # Generate distractors
    words = [w for w in word_tokenize(sentence) if w.isalpha() and w.lower() not in stop_words and w.lower() != keyword_cleaned]
    distractors = random.sample(words, min(3, len(words)))
    
    options = distractors + [keyword]
    random.shuffle(options)
    return question.strip(), options, keyword

def generate_mcqs(text, ngram_n=2):
    sentences = sent_tokenize(text)
    all_keywords = extract_keywords(text, n=ngram_n)
    used_keywords = set()

    questions = []
    for sent in sentences:
        count = 0
        for kw in all_keywords:
            if count >= 3:
                break
            if kw.lower() in sent.lower() and kw.lower() not in used_keywords:
                q, opts, ans = generate_question(sent, kw)
                if q and ans not in q:
                    questions.append({
                        'question': q,
                        'options': opts,
                        'answer': ans
                    })
                    used_keywords.add(kw.lower())
                    count += 1
    return questions
