# The below is an assignment part of Python: Getting Started

students = []


def get_students():
    more_input = "yes"
    while (more_input == "yes"):
        student_name = input("Enter student name:")
        student_class = input("Enter student's class:")
        add_student(
            student_name=student_name ,
            student_class=student_class)
        more_input = input("continue(yes/no):").lower()
    return


def add_student(**kwargs):
    students.append(kwargs)


def print_students(students):
    if not students:
        print("list is empty")
    print(students)


def main():
    get_students()
    print_students(students)


if __name__ == '__main__':
    main()
