
from keywords_module import check_keywords

def analyze_responses(tutor_questions, participants):
    scores = {name: 0 for name in participants.keys()}
    questions_answered = {name: 0 for name in participants.keys()}  # Tracks the number of questions each student answered
    participation = {name: 0 for name in participants.keys()}  # Tracks the total number of messages from each student

    for question in tutor_questions:
        for name, responses in participants.items():
            for response in responses:
                if check_keywords(question, response):
                    scores[name] += 2  # Full points for correct keyword
                    questions_answered[name] += 1  # Increment the number of questions answered
                elif "O" in response:  # If they mention Big O notation, give partial points
                    scores[name] += 1
                participation[name] += 1  # Increment participation count for any response

    # Categorize the level of participation based on the total messages
    high_threshold = max(participation.values()) * 0.7
    medium_threshold = max(participation.values()) * 0.4
    participation_levels = {
        name: ('High' if count >= high_threshold else 'Medium' if count >= medium_threshold else 'Low')
        for name, count in participation.items()
    }

    return scores, questions_answered, participation_levels
