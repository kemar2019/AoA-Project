
from keywords_module import is_correct_response

def analyze_responses(tutor_questions, participants):
    scores = {name: 0 for name in participants.keys()}

    for question in tutor_questions:
        for name, responses in participants.items():
            for response in responses:
                if is_correct_response(question, response):
                    scores[name] += 2  # Full points for correct keyword
                elif "O" in response:  # If they mention Big O notation, give them partial points
                    scores[name] += 1

    return scores
