import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")

analyzer = SentimentIntensityAnalyzer()

def extract_signals(text):

    doc = nlp(text)

    signals = {}

    signals["sentiment"] = analyzer.polarity_scores(text)

    signals["verbs"] = len([t for t in doc if t.pos_ == "VERB"])
    signals["adjectives"] = len([t for t in doc if t.pos_ == "ADJ"])

    return signals