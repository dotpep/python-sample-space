import json
from typing import Dict, Tuple, Generator

def load_json_data(filename: str) -> Dict:
    """Load JSON data from a file and convert it to a dictionary.
    Args:
        filename (str): path to json data "data.json"
    Returns:
        dict: python json representation converted to dictionary
    """
    with open(filename) as file:
        return json.load(file)


def proccess_student_data(data: Dict) -> Generator[Tuple[Tuple, Dict, Dict]]:
    """Process student data and yield tuples containing information, data, and grades.
    Args:
        data (Dict): dictionary containing student data.
    Returns:
        Generator[Tuple[Tuple, Dict, Dict]]: generator yielding tuples with following components:
            - Tuple: Student information (id, name, group).
            - Dict: Student data.
            - Dict: Student grades.
    """
    for student_id, student_data in data.items():
        student_info: Tuple = (student_id, student_data['name'], student_data['group'])
        student_grades: Dict = student_data['grades']
        yield student_info, student_data, student_grades


def calculate_average_grades(grades: Dict) -> Dict:
    """Calculate average grades for each subject.
    Args:
        grades (Dict): dictionary containing grades for various subjects.
    Returns:
        Dict: dictionary with subjects as keys and corresponding average grades as values.
    """
    return {subject: round(sum(grade) / len(grade)) for subject, grade in grades.items()}


def print_student_info(info: Tuple, data_dict: Dict) -> None:
    """Print student information."""
    print("\n\n------")
    print("Info: ", info)
    for student_name, student_group in data_dict.items():
        print(f"\t{student_name}: {student_group}")


def print_student_grades(student_dict: Dict, grades: Dict) -> None:
    """Print student grades."""
    print("\n------")
    print("Student name: ", student_dict["name"])
    print("Group: ", student_dict["group"])
    print("Grades: ")
    for subject, grade in grades.items():
        print(f"\t{subject}: {grade}")


def main() -> None:
    filename: str = "students.json"
    data: Dict = load_json_data(filename)

    for student_info, student_data, student_grades in proccess_student_data(data):
        avg_grades: Dict = calculate_average_grades(student_grades)

        print_student_info(student_info, student_data)
        print_student_grades(student_data, avg_grades)
        

if __name__ == "__main__":
    main()
