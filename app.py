import streamlit as st
from file_reader import read_pdf, read_docx, read_txt
from text_summarization import nltk_summarize, counter
from sentiment import analyze_sentiment, plot_sentiment
from readability_analysis import readability_analysis
from named_entity import named_entity_recognition
from keyword_extraction import extract_keywords

def main():
    #st.title("Enhanced Assignment Evaluation Tool")

    menu = ["Text Analysis", "Assignment Analysis"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Text Analysis":
        st.title("Text Analysis and Summarizer")
        text_area = st.text_area("Input your text here:", height=150)
        word_count = len(text_area.split()) if text_area else 0
        st.write(f"Word Count: {word_count}")
        if st.button("Analyze") and text_area:
            # Text Summarization
            summary = nltk_summarize(text_area)
            st.subheader("Summary")
            st.write(summary)
            st.subheader("Count")
            word_counts = len(summary.split()) if summary else 0
            st.write(f"Word Count: {word_counts}")
            

            # Keyword Extraction
            keywords = extract_keywords(text_area)
            st.subheader("Keywords")
            st.write(keywords)

            # Sentiment Analysis
            sentiment = analyze_sentiment(text_area)
            st.subheader("Sentiment Analysis")
            plot_sentiment(sentiment)

            # Readability Analysis
            readability = readability_analysis(text_area)
            st.subheader("Readability Analysis")
            st.write(f"Flesch Reading Ease: {readability['flesch_reading_ease']}")
            st.write("The Flesch Reading Ease gives a text a score between 1 and 100, with 100 being the highest readability score. Scoring between 70 to 80 is equivalent to school grade level 8. This means text should be fairly easy for the average adult to read")
            
            st.write(f"SMOG Index: {readability['smog_index']}")
            st.write("Simple Measure of Gobbledygook. It is a readability framework. It measures how many years of education the average person needs to have to understand a text. It is best for texts of 30 sentences or more.")

    elif choice == "Assignment Analysis":
        st.title("Assignment Evaluation Tool")
        uploaded_file = st.file_uploader("Upload Assignment File", type=["pdf", "docx", "txt"])
        if uploaded_file is not None:
            file_type = uploaded_file.type
            if file_type == "application/pdf":
                text = read_pdf(uploaded_file)
            elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = read_docx(uploaded_file)
            elif file_type == "text/plain":
                text = read_txt(uploaded_file)
            else:
                st.error("Unsupported file type")
                return

            # Perform analysis
            if text:
                st.subheader("Text Analysis Results")

                # Word Count and Summarization
                word_count = len(text.split())
                st.write(f"Word Count: {word_count}")
                summary = nltk_summarize(text)
                st.write(f"Summary: {summary}")

                # Readability Scores
                readability_scores = readability_analysis(text)
                st.write("Readability Scores:", readability_scores)

                # Named Entity Recognition
                entities = named_entity_recognition(text)
                st.write("Named Entities:", entities)

                # Sentiment Analysis
                sentiment = analyze_sentiment(text)
                st.write(f"Sentiment Polarity: {sentiment[0]:.2f}, Sentiment Subjectivity: {sentiment[1]:.2f}")

                # Keyword Extraction
                keywords = extract_keywords(text)
                st.write("Keywords:", keywords)


if __name__ == '__main__':
    main()
