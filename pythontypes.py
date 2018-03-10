
'''
Type declaration  is not required   in python as declared in statically typed
languages like java or C#.
There are advantages and disadvantages over this, the primary advantage  is it
speeds up  the development time  and  major disadvantage we would face issues
when we are dealing with multiple custom types and may lead to subtle bugs
'''

# type hinting in python 3.5 , this would help developers,editors,ides to
# understand the types passed into function.


def add_numbers(a:int,b:int) ->int:
    """
    addition of two integers.
    :type a: int
    :type b:int
    """
    return a+b

def main():
     print("Addition of numbers:{0}".format(add_numbers(21,9)))


if __name__=='__main__':
    main()