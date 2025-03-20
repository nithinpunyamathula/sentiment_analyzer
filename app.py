import streamlit as st
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Multi-Language Sentiment Analyzer",
    page_icon="🎭",
    layout="wide"
)

# Initialize translator and sentiment analyzer
translator = Translator()
analyzer = SentimentIntensityAnalyzer()

# Sentiment categories with emojis
SENTIMENT_CATEGORIES = {
    (-1.0, -0.75): ("Very Negative", "😡"),
    (-0.75, -0.5): ("Negative", "😞"),
    (-0.5, -0.25): ("Disappointed", "😔"),
    (-0.25, 0.0): ("Neutral", "😐"),
    (0.0, 0.25): ("Calm", "🙂"),
    (0.25, 0.5): ("Good", "😊"),
    (0.5, 0.75): ("Happy", "😁"),
    (0.75, 1.0): ("Very Positive", "🤩")
}

def get_sentiment_category(score):
    for (lower, upper), (category, emoji) in SENTIMENT_CATEGORIES.items():
        if lower <= score <= upper:
            return category, emoji
    return "Neutral", "😐"

def create_gauge(score):
    category, emoji = get_sentiment_category(score)
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [-1, 1]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [-1, -0.75], 'color': "darkred"},
                {'range': [-0.75, -0.5], 'color': "red"},
                {'range': [-0.5, -0.25], 'color': "orange"},
                {'range': [-0.25, 0], 'color': "yellow"},
                {'range': [0, 0.25], 'color': "lightgreen"},
                {'range': [0.25, 0.5], 'color': "green"},
                {'range': [0.5, 0.75], 'color': "lightblue"},
                {'range': [0.75, 1], 'color': "blue"}
            ]
        },
        title={'text': f"Sentiment Score: {category} {emoji}"}
    ))
    
    return fig

def main():
    st.title("🎭 Multi-Language Sentiment Analyzer")
    st.write("Enter text in any language to analyze its sentiment!")

    # Text input
    text = st.text_area("Enter your text:", height=100)
    
    if st.button("Analyze Sentiment"):
        if text:
            # Translate if not in English
            try:
                translation = translator.translate(text, dest='en')
                translated_text = translation.text
                
                if translation.src != 'en':
                    st.info(f"Translated from {translation.src}: {translated_text}")
                
                # Analyze sentiment
                sentiment = analyzer.polarity_scores(translated_text)
                compound_score = sentiment['compound']
                
                # Display results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.plotly_chart(create_gauge(compound_score), use_container_width=True)
                
                with col2:
                    category, emoji = get_sentiment_category(compound_score)
                    st.markdown(f"### Sentiment Analysis Results {emoji}")
                    st.write(f"**Category:** {category}")
                    st.write(f"**Score:** {compound_score:.2f}")
                    
                    # Energy vibe card
                    st.markdown("### Energy Vibe 💫")
                    if compound_score > 0.75:
                        st.success("Absolutely fantastic! Your energy is through the roof! 🌟")
                    elif compound_score > 0.5:
                        st.success("Great vibes! Keep that positive energy flowing! ✨")
                    elif compound_score > 0.25:
                        st.info("Nice and positive! Things are looking good! 🌤")
                    elif compound_score > 0:
                        st.info("Keeping it steady and calm. 🌅")
                    elif compound_score > -0.25:
                        st.warning("A bit down, but hanging in there. 🌥")
                    elif compound_score > -0.5:
                        st.warning("Could use a pick-me-up! 🍵")
                    elif compound_score > -0.75:
                        st.error("Having a rough time. Take care! 🫂")
                    else:
                        st.error("Time for some self-care and support! 💝")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()