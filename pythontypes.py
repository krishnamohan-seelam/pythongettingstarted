'''
Type declaration  is not required   in python as declared in statically typed
languages like java or C#.
There are advantages and disadvantages over this, the primary advantage  is it
speeds up  the development time  and  major disadvantage we would face issues
when we are dealing with multiple custom types and may lead to subtle bugs
'''


# type hinting in python 3.5 , this would help developers,editors,ides to
# understand the types passed into function.


def add_numbers(a: int , b: int) -> int:
    """
    addition of two integers.
    :type a: int
    :type b:int
    """
    return a + b


def numeric_types():
    answer = 21  # integer
    pi = 3.14159  # float
    final_answer = answer + pi  # not required to be worried on types
    print("final answer :{0}".format(final_answer))
    print_line()


import numbers


def convert_float(a: float) -> int:
    # the result of the below statement is boolean type
    is_number = isinstance(a , numbers.Number)
    print("python type of is_number {0}".format(type(is_number)))
    if is_number:
        return int(a)
    else:
        return 0.0


def string_introduction():
    message = "Hello world , this is python"
    print("length of message {0}".format(len(message)))
    print("lower case of message :{0}".format(message.lower()))
    print("captalize message :{0}".format(message.capitalize()))
    ### splitting strings
    words = message.split()
    print(words)
    print_line()


def ternary_if():
    a = 10
    b = 5
    result = "a is bigger" if a > b else "b is bigger"
    print(result)
    print_line()


def print_line(symbol="=" , width=80):
    print(symbol * width)


def list_introduction():
    # create empty list
    fruits = []
    fruits = ["Apple" , "Banana" , "Cherry" , "Dates" , "Fig" , "Grapes"]
    fruits.append("Jack Fruit")
    # list slicing
    print(fruits[1:])
    print_line()


def dict_introduction():
    student = {'name': 'Krishna' , 'id': 1 , 'feedback': 'good'}
    print("Name os student:{0}".format(student['name']))
    # if key does not exist,  we get key error to prevent it we use
    # default value
    print("Default value example")
    grade = student.get('grade' , "NA")
    print("default value for key grade : {0}".format(grade))


def main():
    print("Addition of numbers:{0}".format(add_numbers(21 , 9)))
    numeric_types()
    pi = 3.14159
    print("{0} convert into int {1}".format(pi , convert_float(3.14159)))
    string_introduction()
    ternary_if()
    list_introduction()
    dict_introduction()


if __name__ == '__main__':
    main()
