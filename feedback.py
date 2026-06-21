from interview import model

def evaluate_answer(question, answer):

    prompt = f"""
    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and provide:

    Score out of 10
    Strengths
    Weaknesses
    Suggestions
    """

    response = model.generate_content(prompt)

    return response.text