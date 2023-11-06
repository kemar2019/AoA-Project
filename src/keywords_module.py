
keywords_dict = {
    "What is the speed of light in vacuum?": ["299,792 km/s"],
    "Who is known as the father of computing?": ["Charles Babbage"],
    "What is the main ingredient in guacamole?": ["Avocado"],
    "What is the largest planet in our solar system?": ["Jupiter"],
    "What is the capital of France?": ["Paris"],
    "What is the highest mountain in the world?": ["Mount Everest"],
    "What is the smallest prime number?": ["2"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci"],
    "What is the chemical symbol for water?": ["H2O"],
    "Who wrote 'Romeo and Juliet'?": ["William Shakespeare"],
    "What is the Big O efficiency of Dijkstra’s algorithm if we use a min-priority queue data structure to implement it?": ["O(V + E log V)", "O(v^2)", "quadratic", "linear"],
    "What is the capital of Jamaica?": ["Kingston", "kingston"]
    # Add more questions and keywords as needed
}

def check_keywords(question, response):
    keywords = keywords_dict.get(question, [])
    return any(keyword.lower() in response.lower() for keyword in keywords)

def update_keywords(question, keywords):
    keywords_dict[question] = keywords

def is_correct_response(question, response):
    return check_keywords(question, response)
