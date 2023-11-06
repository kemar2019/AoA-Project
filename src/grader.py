
def assign_grades(scores):
    grades = {}
    max_score = max(scores.values()) if scores else 0
    for name, score in scores.items():
        scaled_score = (score / max_score) * 100 if max_score else 0
        if scaled_score >= 90:
            grades[name] = 'A'
        elif scaled_score >= 80:
            grades[name] = 'B'
        elif scaled_score >= 70:
            grades[name] = 'C'
        elif scaled_score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades
