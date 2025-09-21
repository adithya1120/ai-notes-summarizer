import streamlit as st
from google import genai
import PyPDF2 as pdf
import os

# Get API key from Streamlit Secrets
API_KEY = os.getenv("GOOGLE_API_KEY")
client = None
if API_KEY:
    client = genai.Client(api_key=API_KEY)

def get_gemini_response(input_text, prompt):
    if not client:
        return "API key not found. Please set it in Streamlit Secrets."
    response = client.models.generate_content(
        model="gemini-1.5-flash-latest",
        contents=[input_text + "\n" + prompt]
    )
    return response.text

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is None:
        return ""
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""

input_prompt = """
You are an expert in summarizing academic notes and articles. 
Please provide a concise summary of the following text. The summary should capture the key points, 
main arguments, and any significant findings mentioned. Structure the summary into clear, 
easy-to-digest bullet points.

Text to summarize:
"""

st.set_page_config(page_title="AI Notes Summarizer 📝", layout="wide")
st.header("AI Notes Summarizer 📝")
st.subheader("Condense your notes and articles instantly")

text_input = st.text_area("Paste your text here...", height=250)
uploaded_file = st.file_uploader("...or upload a PDF", type=["pdf"])
submit_button = st.button("Summarize")

if submit_button:
    with st.spinner('Summarizing...'):
        input_data = ""
        if uploaded_file is not None:
            input_data = extract_text_from_pdf(uploaded_file)
        elif text_input:
            input_data = text_input
        else:
            st.warning("Please upload a PDF or paste some text to summarize.")
            st.stop()

        if not input_data.strip():
            st.error("Could not extract any text from the source. Please check your PDF or text input.")
            st.stop()

        summary = get_gemini_response(input_data, input_prompt)
        st.subheader("Here's your summary:")
        st.write(summary)
