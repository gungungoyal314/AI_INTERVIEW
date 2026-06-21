import streamlit as st
from interview import questions
from feedback import evaluate_answer

st.set_page_config(page_title="AI Interview Bot")

st.title("🎤 AI Interview Bot")

selected_question = st.selectbox(
    "Select Interview Question",
    questions
)

answer = st.text_area(
    "Enter Your Answer"
)

if st.button("Evaluate Answer"):

    if answer:

        with st.spinner("Analyzing..."):

            result = evaluate_answer(
                selected_question,
                answer
            )

        st.success("Evaluation Complete")

        st.write(result)

    else:
        st.warning("Please enter an answer.")