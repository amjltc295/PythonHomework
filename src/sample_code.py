'''
This is the sample code from the homework. You shold NOT modify this file.
Instead, please copy this file to src/students/<your student ID>.py and
edit it there.
'''


def task_1():
    '''
    Task 1: Basic Syntax and Flake8 Checker

    Python uses indentations to separate blocks instead of backets.
    Unlike most programming language (like C++), indentations in Python
    are required.

    See https://www.python-course.eu/python3_blocks.php for some examples.

    Flake8 (http://flake8.pycqa.org/en/latest/) could help you check these
    syntax error. It also regular your coding style. For example, using
    two whitespaces as indentation is allowed in Python. However, Flake8
    will tell you it is an error "E111: indentation is not a multiple of four".
    This is because when many people work on the same project, it would be
    confusing if people are using different identation style.

    Following the coding style in Flake8 is strongly suggested.

    '''
    # Hint:
    # Run `python src/autograder.py -task 1 -student <your student ID>`
    # to see if you pass this task.
    # The correct output would be "Hello world" without any
    # error. Note that passing this task does NOT mean you pass the
    # Flake8 chcker. Please check your style with
    # `flake8 src/student/<your student ID>.py`

    # TODO: fix the syntax error for the following code
    if true:
        sentence="Hello world"
      print (sentence)

    # End of TODO (do not change the code below)
    return True


def task_2(
    input_list: list = [1, 4, 53, 27, 9],
    target_index: int = 0,
    input_dictionary: dict = {"a": " taiwan", "b": 20, "c": "CSIE"},
    target_key: str = "a"
) -> tuple:
    '''
    Task 2: Data Types

    Python has many data types, including Boolean, String, Integer, Float,
    List, Dictionary, etc.

    You could use the function type() to see the data type:

    >>> type(5)
    <class 'int'>
    >>> type("hi")
    <class 'str'>
    >>> type(9.2)
    <class 'float'>
    >>> type(["list", "could", "include", "different", "data type", 5, 3.2])
    <class 'list'>
    >>> type(("you could not change elements", "in a tuple"))
    <class 'tuple'>
    >>> type({"a": 1, "b":20})
    <class 'dict'>
    >>> type(True)
    <class 'bool'>
    >>>

    Try to play with the Python IDE to see different data types by yourself.

    In this task, you are asked to use these datatype.

    Args:
        input_list: a list with several items
        target_index: target index for the input_list. You need to get the
            list element with this index (i.e, 'input_list[target_index]')
        input_dictionary: a dictionary with several key-value pairs.
        target_key: target key for the input_dictionary You need to get the
            value with this key (i.e., input_dictionary[target_key])

    Returns:
        input_list_length_and_sentence: a tuple that contains two elements.
            The fisrt one is an integer that indicates the length of input_list
            The second one is a string that contains the combination of
            input_list[target_index] and input_dictionary[target_key]

    Examples:
        Inputs:
            input_list = [1, 3, 5, 7, 9]
            target_index = 0
            input_dictionary = {"1": "8", "f": "abc", "s": 5.5, "5.5" 900}
            target_key = "5.5"

        Returns:
            sentence = (5, "1900")

    Hints:
        * Try to use print() to print out the inputs.
        * Use len() to get the length of the list.
        * Different data types could not be added. Use str() to convert data
        to string.
        * Run `python src/autograder.py -task 2 -student_id <your student ID>`
        to see if you pass this task.
        * The correct output would be (5, '1 taiwan')
    '''
    # TODO: change length and sentence to fit the requirement
    length = None
    sentence = None
    # End of TODO
    input_list_length_and_sentence = (length, sentence)
    print(input_list_length_and_sentence)
    return input_list_length_and_sentence


def task_5(
    input_filename: str = 'task_5_input.txt',
    output_filename: str = 'task_5_output.txt'
):
    '''

    Args:
        input_filename: input filename
        output_filename: output filename

    Returns:
        lines: content in the output file
    Hints:
        * Use <str>.split(something) to split a string into several substring
        * Use fout.write(something) to write text into the output file

    '''
    with open(input_filename, 'r') as fin, open(output_filename, 'w') as fout:
        lines = fin.readlines()
        print(f"=======> Input file content:")
        for line in lines:
            print(f"{line}")
        # TODO: read the content of the input file, remove all commas and
        # write to the output file
        pass
    # End of TODO

    with open(output_filename, 'r') as fin:
        lines = fin.readlines()
        print(f"=======> Output file content:")
        for line in lines:
            print(f"{line}")
        return lines
