courses = {
    "Math": [85, 67, 90],
    "English": [91, 95, 93],
    "Science": [65, 72, 89],
    "History": [82, 85, 88]
}

#averages = {}

#for course, scores in courses.items():
#    average = sum(scores) / len(scores)
#    averages[course] = average


averages = {key: round(sum(value) / len(value), 2) for key, value in courses.items()}
print(averages)
print("Maximum in: ", max(averages, key=averages.get))
