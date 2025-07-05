
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st
import os
import streamlit as st

from src.market_sentiment import fetch_random_article,fetch_article_content,summarize_article
from src.stock_utils import get_stock_price, plot_stock_performance, get_company_financials

# Streamlit UI
st.title("💰 Financial Advisor")

# Sidebar for stock selection
st.sidebar.header("Stock Information")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL)")

if ticker_symbol:
    # Fetch current stock price
    price = get_stock_price(ticker_symbol)
    st.subheader(f"📊 Current Stock Price: {ticker_symbol}")
    st.write(f"${price:.2f}")

    # Display performance chart for the past month
    st.subheader(f"📈 {ticker_symbol} Performance (Last 1 Month)")
    fig = plot_stock_performance(ticker_symbol)
    st.plotly_chart(fig)

    # Fetch and display company financials
    st.subheader(f"🏢 {ticker_symbol} Financials")
    financials = get_company_financials(ticker_symbol)
    st.write(financials)

# Fetch and display a summarized financial news article
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
import streamlit as st

# Initialize Hugging Face summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to extract paragraphs and clean up
def extract_paragraphs_from_html(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted tags like <script>, <style>, <meta>
        for unwanted_tag in soup(["script", "style", "meta", "header", "footer", "nav"]):
            unwanted_tag.decompose()

        # Extract all paragraphs
        paragraphs = soup.find_all("p")

        # Combine paragraphs into a single string, filtering out any empty ones
        article_content = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])
        
        # If content is too short, return an error message
        if len(article_content) < 200:
            return "❌ Article content is too short."
        
        return article_content
    except Exception as e:
        return f"❌ Error during content extraction: {str(e)}"

def summarize_article(text):
    try:
        # Limit to ~1024 tokens (about 1300–1500 characters for English)
        max_input_length = 2000  # Safe cap to avoid overflow
        input_text = text[:max_input_length]

        summary = summarizer(
            input_text,
            max_length=100,
            min_length=50,
            do_sample=False
        )

        return summary[0]['summary_text']
    except Exception as e:
        return f"❌ Error during summarization: {str(e)}"

# Streamlit App
def app():
    st.title("Finance News Summarizer")

    # Input URL to fetch article from
    url = st.text_input("Enter Article URL", "https://www.pioneerspost.com/news-views/20250704/blended-finance-remains-most-promising-tool-financing-development-needs-fixing")

    if url:
        # Fetch the article content from the URL
        article_content = extract_paragraphs_from_html(url)
        
        if "❌" not in article_content:
            st.subheader("📊 Summary:")
            summary = summarize_article(article_content)
            st.write(summary)  # Display the summary in Streamlit
        else:
            st.warning("⚠️ Unable to extract or summarize the article.")

if __name__ == "__main__":
    app()
