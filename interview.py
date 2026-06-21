import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

questions = {
    "Python": [
        "What is OOP?",
        "What is Inheritance?",
        "What is Polymorphism?"
    ],

    "Machine Learning": [
        "What is Machine Learning?",
        "What is Overfitting?"
    ],

    "HR": [
        "Tell me about yourself"
    ]
}



print('MODEL LOADED')
