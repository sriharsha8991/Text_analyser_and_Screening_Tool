from transformers import pipeline

def sentiment_analysis(text):
    # Load the sentiment analysis pipeline
    classifier = pipeline('sentiment-analysis')

    # Perform sentiment analysis
    result = classifier(text)

    return result


