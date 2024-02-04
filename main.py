# app.py
import streamlit as st
from utils.genai import get_gemini_response
from utils.image import  input_image_details
from PIL import Image

# Streamlit app
st.set_page_config(
    page_title="Multilanguage Invoice Extractor",
    page_icon=":gemini:",
    layout="wide"
)

# Header
st.title("Multilanguage Invoice Extractor")

# File uploader
uploaded_file = st.file_uploader("Choose an invoice image:", type=["png", "jpg", "jpeg"])
image = ""

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=False, width=300)

# Input prompt for Gemini
input_prompt = """
 You are an expert in understanding invoices. You will receive input images as invoices & you will have to answer questions based on the input image.
"""

# Input text
input = st.text_input("Input Prompt: ", key="input")

# Handle Submit Button
if st.button("Tell me about the invoice") and input:
    try:
        # Add a loading spinner while fetching the query response
        with st.spinner("Digging into your invoice..."):
            # Get Gemini response and display
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input)
        # Remove the loading spinner and display the response
        st.write(f"Response: {response}")
    except FileNotFoundError as e:
        st.error(str(e))
