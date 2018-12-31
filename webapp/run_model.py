import pickle
import re

def clean_text(text):
    text = text.lower()
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text

def predict(input_text):
    input_text = [clean_text(input_text)]

    with open(f'model/finalized_model.sav', 'rb') as f:
        model = pickle.load(f)

    with open(f'model/tfidf_model.sav', 'rb') as f:
        vectorizer = pickle.load(f)

    mapping = {0: 'CLIMATE',
    1: 'SCIENCE',
    2: 'SOCIETY',
    3: 'BUSINESS',
    4: 'SCI-TECH',
    5: 'SPORTS',
    6: 'ENTERTAINMENT',
    7: 'POLITICS',
    8: 'EDUCATION'}

    #text = ["science is fun temperature"]

    text_feats = vectorizer.transform(input_text)
    prediction = model.predict(text_feats)[0]

    category = ""
    for key, value in mapping.items():
        if key == prediction:
            category = value
    return category
