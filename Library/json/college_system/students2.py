import json

def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)

def calculate_average_grades(grades):
    return {subject: round(sum(scores) / len(scores)) for subject, scores in grades.items()}

def print_student_average(student_info, average_grades):
    print("\nStudent name:", student_info["name"])
    for subject, grade in average_grades.items():
        print(f"{subject}: {grade}")

def process_students(data):
    student_tuples = []
    grades_tuples = []

    for student_id, student_data in data.items():
        student_info = {
            "id": student_id,
            "name": student_data['name'],
            "group": student_data['group']
        }
        student_tuples.append(student_info)

        average_grades = calculate_average_grades(student_data['grades'])
        print_student_average(student_info, average_grades)

        for subject, subject_grades in student_data['grades'].items():
            grades_info = {
                "id": student_id,
                "subject": subject,
                "grades": subject_grades
            }
            grades_tuples.append(grades_info)

    return student_tuples, grades_tuples

def main():
    data = load_data('students.json')

    student_tuples, grades_tuples = process_students(data)

    print("\nStudent Tuples:")
    for student_info in student_tuples:
        print(student_info)

    print("\nGrades Tuples:")
    for grades_info in grades_tuples:
        print(grades_info)


if __name__ == "__main__":
    main()
    