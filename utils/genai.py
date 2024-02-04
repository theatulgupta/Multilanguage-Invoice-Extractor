import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure GenAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Creating GenAI model
model = genai.GenerativeModel(model_name="gemini-pro-vision")

# Function to get Gemini response
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text
