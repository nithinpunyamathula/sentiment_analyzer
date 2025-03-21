Multi-Language Sentiment Analyzer

Overview

The Multi-Language Sentiment Analyzer is a Streamlit-based web application that detects sentiment in text inputs across multiple languages. It translates non-English text into English, performs sentiment analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner), and visually represents sentiment scores using a gauge chart.

Features

Supports sentiment analysis for multiple languages.

Automatic translation of non-English text into English using Google Translate.

Uses VADER Sentiment Analysis to assess polarity scores.

Visual representation of sentiment scores with a gauge chart.

Emoji-based sentiment categories for better user experience.

Energy Vibe Card to provide positive, encouraging feedback based on sentiment.

Technologies Used

Python

Streamlit (for web-based UI)

Googletrans (for language translation)

VADER SentimentIntensityAnalyzer (for sentiment analysis)

Plotly (for data visualization)

Installation

To run this application locally, follow these steps:

Prerequisites

Ensure you have Python installed (Python 3.7+ recommended). Then, install the required dependencies:

pip install streamlit googletrans==4.0.0-rc1 vaderSentiment plotly

Running the Application

Run the Streamlit app with the following command:

streamlit run app.py

How It Works

Enter text: Type or paste any text in any language.

Automatic translation: If the text is not in English, it will be translated automatically.

Sentiment analysis: VADER analyzes the translated text and provides a compound sentiment score.

Visualization: A gauge chart displays the sentiment score visually.

Feedback: A descriptive sentiment category with emojis is shown, along with an energy vibe message.

Sentiment Categories

Sentiment Score Range

Category

Emoji

-1.0 to -0.75

Very Negative

😡

-0.75 to -0.5

Negative

😞

-0.5 to -0.25

Disappointed

😔

-0.25 to 0.0

Neutral

😐

0.0 to 0.25

Calm

🙂

0.25 to 0.5

Good

😊

0.5 to 0.75

Happy

😁

0.75 to 1.0

Very Positive

🤩

Example Output

Input: "C'est une belle journée!" (French: "It's a beautiful day!")

Translated: "It's a beautiful day!"

Sentiment Score: 0.85

Category: Very Positive 🤩

Energy Vibe: "Absolutely fantastic! Your energy is through the roof! 🌟"

Future Improvements

Improve translation accuracy with better API integration.

Expand sentiment analysis models for better multilingual support.

Enhance UI/UX with more interactive elements.

License

This project is open-source and available for use under the MIT License.

Developed with ❤️ using Streamlit & Python
