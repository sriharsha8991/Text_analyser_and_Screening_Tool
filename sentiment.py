from textblob import TextBlob
import matplotlib.pyplot as plt
import streamlit as st

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

def plot_sentiment(sentiment):
    fig, ax = plt.subplots()
    ax.barh(['Polarity', 'Subjectivity'], [sentiment.polarity, sentiment.subjectivity], color=['skyblue', 'salmon'])
    ax.set_xlim(-1, 1)
    for i, v in enumerate([sentiment.polarity, sentiment.subjectivity]):
        ax.text(v, i, f" {'Positive' if v > 0 else 'Negative' if v < 0 else 'Neutral'}", color='blue' if i == 0 else 'red', va='center')
    st.pyplot(fig)


