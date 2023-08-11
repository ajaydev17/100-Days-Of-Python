# student score dictionary
student_scores = {
    "Harry": 81,
    "Price": 78,
    "Ron": 58,
    "Max": 99,
    "Muller": 61
}

student_grades = {}

# loop through the dictionary
for student in student_scores:
    score = student_scores[student]

    if score >= 90:
        student_grades[student] = "Outstanding"
    elif score >= 80:
        student_grades[student] = "Excellent"
    elif score >= 70:
        student_grades[student] = "Good"
    elif score >= 60:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
