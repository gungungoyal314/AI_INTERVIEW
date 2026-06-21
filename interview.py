import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

questions = [
    "What is Machine Learning?",
    "What is Overfitting?",
    "Difference between AI and ML?",
    "What is Random Forest?",
    "Explain Deep Learning."
]