
keywords_dict = {
    "What is the Big O efficiency of Dijkstra’s algorithm if we use a min-priority queue data structure to implement it?": ["O(V + E log V)", "O(v^2)", "quadratic", "linear"],
    # Add more questions and keywords as needed
}

def check_keywords(question, response):
    keywords = keywords_dict.get(question, [])
    return any(keyword.lower() in response.lower() for keyword in keywords)

def update_keywords(question, keywords):
    keywords_dict[question] = keywords

def is_correct_response(question, response):
    return check_keywords(question, response)
