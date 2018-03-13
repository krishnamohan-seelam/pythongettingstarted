# concepts :classes, instance attributes,class attributes, overriding methods,
# calling parent methods,overriding attributes

students = []


class Student:
    school_name = "St.Joseph's Primary School"

    def __init__(self , id , name , last_name):
        self.id = id
        self.name = name
        self.last_name = last_name
        students.append(self)

    def __str__(self):
        return "Student : {0}".format(self.name)

    def __repr__(self):
        return "Student({0},{1})".format(self.id , self.name)

    def get_schoolname(self):
        return self.school_name

    def get_name_captialize(self):
        return self.name.capitalize()


class HighSchoolStudent(Student):
    school_name = "St.Joseph's Secondary School"

    def get_name_captialize(self):
        return super().get_name_captialize() + "-HS"


def main():
    krishna = Student(1 , "Krishna")
    mohan = Student(2 , "Mohan")

    print("list of students")
    print(students)

    print("object representation(__repr__)")
    print("{!r}".format(krishna))

    print("string representation")
    print("{!s}".format(krishna))

    print("=" * 80)

    swathi = HighSchoolStudent(3 , "Swathi")

    print("overidden version of get_name_captialize()")
    print(swathi.get_name_captialize())

    print(students)


if __name__ == '__main__':
    main()
