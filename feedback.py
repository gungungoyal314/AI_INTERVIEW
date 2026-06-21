import interview

def evaluate_answer(question, answer):
    try:
        prompt = f"""
        Question:
        {question}

        Candidate Answer:
        {answer}

        Evaluate the answer and provide:
        Score: X/10
        Strengths
        Weaknesses
        Suggestions
        """

        response = interview.model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"API Error: {str(e)}"