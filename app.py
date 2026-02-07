import streamlit as st
from groq import Groq
import os

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AISummarizer", layout="centered")
st.title=("Docuent Summarizer")
st.write("Paste text below and choose how you want it summarized.")


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("API_KEY not found in environment variables.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

text = st.text_area("Enter text to summarize", height=220)

summary_type = st.selectbox(
    "Summary style",
    ["Brief", "Detailed", "Bullet Points"]
)

def prompt(text,summary_type):
    if summary_type=="Brief":
        return f"Summarize the following text briefly:\n\n{text}"
    elif summary_type=="Detailed":
        return f"Summarize the following text Detailed:\n\n{text}"
    else:
        return f"Summarize the following text in bullet points:\n\n{text}"
if st.button("Summarize"):
    if not text:
        st.warning("Please enter some text.")
    else:
        try:
            with st.spinner("Generating summary..."):
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt(text, summary_type)
                        }
                    ],
                    temperature=0.5
                )
                summary = response.choices[0].message.content

                st.subheader("Summary")
                st.write(summary)

        except Exception as e:
            st.error(f"Error: {e}")

