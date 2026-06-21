import streamlit as st
from interview import questions
from feedback import evaluate_answer
from utils import extract_score

st.set_page_config(
    page_title="AI Interview Bot",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Bot")
st.markdown("### Practice interviews with AI-powered feedback")

name = st.text_input("👤 Enter Your Name")

category = st.selectbox(
    "📚 Select Category",
    list(questions.keys())
)

question = st.selectbox(
    "❓ Select Question",
    questions[category]
)

answer = st.text_area(
    "✍️ Your Answer",
    height=200,
    placeholder="Type your answer here..."
)

if st.button("🚀 Evaluate Answer"):

    if answer.strip() == "":
        st.warning("Please enter your answer.")
    else:

        with st.spinner("Analyzing your answer..."):

            result = evaluate_answer(
                question,
                answer
            )

        score = extract_score(result)

        st.success("Evaluation Complete ✅")

        st.metric(
            label="Interview Score",
            value=f"{score}/10"
        )

        st.progress(score * 10)

        st.markdown("## 🤖 AI Feedback")

        st.write(result)