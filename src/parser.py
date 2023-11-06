
import re

def parse_chat_log(chat_log):
    participants = {}
    tutor_name = 'Mikhail McDowell'  # Assuming this is the tutor's name
    tutor_questions = []
    last_speaker = None  # Variable to keep track of the last speaker

    # Split logs into individual messages
    messages = chat_log.strip().split("\n")

    for i, message in enumerate(messages):
        # Match the timestamp, sender, and recipient
        header_match = re.match(r'(\d{2}:\d{2}:\d{2}) From ([\w\s]+) to Everyone:', message)
        if header_match:
            _, last_speaker = header_match.groups()
        else:
            # If this line is not a header, it should be a message content
            content = message.strip('\t')
            if last_speaker == tutor_name:
                # Assume every message from the tutor is a question
                tutor_questions.append(content)
            else:
                # Add the participant's response to the list
                if last_speaker not in participants:
                    participants[last_speaker] = []
                participants[last_speaker].append(content)

    return tutor_questions, participants
