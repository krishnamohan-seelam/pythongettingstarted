students = []


def read_file():
    try:
        student_file = open("students.txt" , "r")
        for student in student_file:
            add_student(student.strip(" \n"))
        student_file.close()
    except  Exception:
        print("file cannot be accessed")


def add_student(student):
    students.append(student)


def save_student(students):
    try:
        student_file = open("students.txt" , "w")
        for student in students:
            student_file.write(student + "\n")
        student_file.close()
    except Exception:
        print("Could not save file")


def print_students(students):
    if not students:
        print("list is empty")
    print(students)


def get_students():
    more_input = "yes"
    while (more_input == "yes"):
        student_name = input("Enter student name:")
        add_student(student_name)
        more_input = input("continue(yes/no):").lower()
    return


def main():
    read_file()
    print_students(students)
    get_students()
    print_students(students)
    save_student(students)


if __name__ == '__main__':
    main()
