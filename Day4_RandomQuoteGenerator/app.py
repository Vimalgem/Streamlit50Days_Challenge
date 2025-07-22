import streamlit as st
import random
import json

# Load quotes
def load_quotes():
    with open('quotes.json', 'r') as file:
        return json.load(file)

# Title
st.title("💬 Random Quote Generator")

# Load and show a random quote
quotes = load_quotes()
if st.button("🔄 Refresh Quote"):
    selected = random.choice(quotes)
    st.markdown(f"> *{selected['quote']}*")
    st.caption(f"– {selected['author']}")
else:
    selected = random.choice(quotes)
    st.markdown(f"> *{selected['quote']}*")
    st.caption(f"– {selected['author']}")
