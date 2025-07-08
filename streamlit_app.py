import streamlit as st
from app.main import get_prices
import pandas as pd

# Replace this with your Groq API Key
GROQ_API_KEY = "your-groq-api-key"

st.title("🌐 Global Price Comparator (Groq LLM Powered)")
query = st.text_input("Enter product name", "iPhone 16 Pro, 128GB")
country = st.selectbox("Select country", ["US", "IN", "UK"])

if st.button("Compare Prices"):
    with st.spinner("Fetching and analyzing..."):
        results = get_prices(query, country, GROQ_API_KEY)
        if results:
            st.success(f"Found {len(results)} results")
            df = pd.DataFrame(results)
            st.dataframe(df)
        else:
            st.warning("No matching results found.")