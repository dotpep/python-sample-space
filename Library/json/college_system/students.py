import json

## 1
#with open('students.json') as file:
#    data = json.load(file)


## 2
#for student_id, student_data in data.items():
#    student_info = (student_id, student_data['name'], student_data['group'])
#    student_dict = {
#        "id": student_id,
#        "name": student_data['name'],
#        "group": student_data['group']
#    }

#    # 3
#    average_grade = {key: round(sum(value) / len(value)) for key, value in student_data['grades'].items()}

    ## 4
    #print("\n\n------")
    #print("Info: ", student_info)
    #for student_name, student_group in student_dict.items():
    #    print(f"\t{student_name}: {student_group}")

    ## 5
    #print("\nStudent name: ", student_dict["name"])
    #print("Group: ", student_dict["group"])
    #print("Grades: ")
    #for subject, grade in average_grade.items():
    #    print(f"\t{subject}: {grade}")




def load_json_data(filename): # 'students.json'
    with open(filename) as file:
        return json.load(file)


def proccess_data(data): # load_json_data()
    for student_id, student_data in data.items():
        student_info = (student_id, student_data['name'], student_data['group'])
        student_dict = {
            "id": student_id,
            "name": student_data['name'],
            "group": student_data['group']
        }
        return student_info, student_dict, student_data['grades'] # data_tuple, data_dict, student_grades


def calculate_average_grades(grades): # student_grades
    average_grade = {subject: round(sum(grade) / len(grade)) for subject, grade in grades.items()}
    return average_grade


def print_student_info(info, data_dict): # data_tuple, data_dict
    print("\n\n------")
    print("Info: ", info)
    for student_name, student_group in data_dict.items():
        print(f"\t{student_name}: {student_group}")


def print_student_grades(student_dict, grades): # data_dict, student_grades
    print("\nStudent name: ", student_dict["name"])
    print("Group: ", student_dict["group"])
    print("Grades: ")
    for subject, grade in grades.items():
        print(f"\t{subject}: {grade}")


def main():
    data = load_json_data("students.json")

    data_tuple, data_dict, student_grades = proccess_data(data)

    avg_grades = calculate_average_grades(student_grades)

    print_student_info(data_tuple, data_dict)
    print_student_grades(data_dict, avg_grades)


if __name__ == "__main__":
    main()
