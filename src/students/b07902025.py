'''
This is the sample code from the homework. You shold NOT modify this file.
Instead, please copy this file to src/students/<your student ID>.py and
edit it there.
'''
import os

# Define global variables with upper case
SRC_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEST_DATA_DIR = os.path.join(SRC_PATH, 'test_data')


def task_1(dummy=None):
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
    if True:
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
            The first one is an integer that indicates the length of input_list
            The second one is a string that contains the combination of
            input_list[target_index] and input_dictionary[target_key]

    Examples:
        Inputs:
            input_list = [1, 3, 5, 7, 9]
            target_index = 0
            input_dictionary = {"1": "8", "f": "abc", "s": 5.5, "5.5" 900}
            target_key = "5.5"

        Returns:
            input_list_length_and_sentence = (5, "1900")

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


def task_3(
    number: int = 1314151677777
) -> list:
    '''
    Task 3: Conditions

    Args:
        number: a integer input

    Returns:
        prime_factors_below_10: a list of the number's largest factors
            below 10
            if the number is negative, return [-1]
            if the number is zero, return [0]

    Hints:
        * Use % to get the remainder
        * Using a loop (introduced in the next task) will make some
          conditions simpler
    '''
    prime_factors_below_10 = []
    # TODO: fill in the conditions
    if "some condition here":
        prime_factors_below_10 = [-1]
    # elif stands for "else if" in Python.
    elif "some condition here":
        prime_factors_below_10 = [0]
    else:
        if "some condition here":
            prime_factors_below_10.append(2)
        if "some condition here":
            prime_factors_below_10.append(3)
        if "some condition here":
            prime_factors_below_10.append(5)
        if "some condition here":
            prime_factors_below_10.append(7)
    # End of TODO
    print(prime_factors_below_10)
    return prime_factors_below_10


def task_4(
    numbers: list = [2, 4, 5, 6, 9]
) -> list:
    '''
    Task 4: For and While Loop

    Args:
        numbers: a list of integers

    Returns:
        list_of_stars: a list of stars (*)
            For each number n in the list, you need to
            append n lines of stars to the list, where
            the first line has one star, the last line
            has n stars.

    Examples:
        input:
            [1, 3, 5]
        output:
            ['*',
             '*',
             '**',
             '***',
             '*',
             '**',
             '***',
             '****',
             '*****']

    Hints:
        * You could create a string with repetitive substring by <str> * <int>
    '''
    list_of_stars = []
    # In Python, the for loop could iterate through a list directly
    for number in numbers:
        # TODO: change stars to correct length
        for i in range(1, number+1):
            stars = "*"
            list_of_stars.append(stars)
        # End of TODO

    # This could be done by the while loop
    list_of_stars_while = []
    i = 0
    while i < len(numbers):
        # TODO: change stars to correct length
        j = 1
        while j <= numbers[i]:
            stars = "*"
            j += 1  # This line is equivalant to j = j + 1
            list_of_stars_while.append(stars)
        i += 1
        # End of TODO

    print("=====> Output list_of_stars")
    for stars in list_of_stars:
        print(stars)
    print("=====> Output list_of_stars_while")
    for stars in list_of_stars_while:
        print(stars)

    for ans1, ans2 in zip(list_of_stars, list_of_stars_while):
        assert ans1 == ans2
    return list_of_stars


def task_5(
    input_filename: str = 'task_5_input.txt',
    output_filename: str = 'task_5_output.txt'
) -> str:
    '''
    Task 5: I/O with files

    Args:
        input_filename: input filename
        output_filename: output filename

    Returns:
        lines: content in the output file without commas

    Hints:
        * Use <str>.split(something) to split a string into several substring
        * Use fout.write(something) to write text into the output file

    '''
    input_filename = os.path.join(TEST_DATA_DIR, input_filename)
    output_filename = os.path.join(TEST_DATA_DIR, output_filename)
    # Remove previous output file
    if os.path.exists(output_filename):
        os.remove(output_filename)

    with open(input_filename, 'r') as fin, open(output_filename, 'w') as fout:
        lines = fin.readlines()
        print(f"=======> Input file content:")
        for line in lines:
            print(f"{line}")
        # TODO: read the content of the input file, where words are separate by
        # commas. Please remove the commas and write words to the output file
        pass
    # End of TODO

    with open(output_filename, 'r') as fin:
        lines = fin.readlines()
        print(f"=======> Output file content:")
        print(lines)
        return "".join(lines)


def task_6(
    matrix: list = [[-0.5, 1], [1, 0.5], [-1, 0.5], [-1, -0.5]],
    vector: list = [1, 0.5]
) -> list:
    '''
    Task 6: Functions

    Args:
        matrix: a list of v1
        vector: v2

    Returns:
        cos_sims: a list of cosine similarity between v1s and v2

    Hints:
        * A good function name should be self-explained
        * A good function should be less than 30 lines
        * A good function should include comments to explain how to use it
        * Cosine similarity of the vector itself will be 0.9999999 instead of 1
    '''
    # You could define function B in function A, but function B could only
    # be used in the scope of function A
    def dot_product(v1, v2):
        assert len(v1) == len(v2)
        return sum(a*b for a, b in zip(v1, v2))

    def norm(vector):
        # Note that this function would have some minor error due to the
        # approximation of square root
        return dot_product(vector, vector) ** 0.5

    def get_cosine_simialrity(v1, v2):
        '''
        Calculate the cosine similarity = v1 * v2 / (|v1| *  |v2|)
        '''
        # TODO: use the above functions to calculate cosine similarity of
        # the two vectors v1 and v2
        cos_sim = 0
        # End of TODO

        return cos_sim

    cos_sims = []
    for v1 in matrix:
        cos_sim = get_cosine_simialrity(v1, vector)
        print(f"Cosine similarity between {v1} and {vector}: {cos_sim}")
        cos_sims.append(cos_sim)
    return cos_sims


class Student():
    def __init__(self, student_id, time):
        self.student_id = student_id
        self.time = time
        self.words_to_say = "initial value"

    def set_words_to_say(self, words_to_say):
        self.words_to_say = words_to_say

    def hello(self):
        return (
            f"Hello, {self.student_id}! Time is {self.time}. "
            f"I want to say {self.words_to_say}"
        )


def task_7(
    student_id: str = 'test_id',
    time: str = '2018_11_24_0000'
) -> Student:
    '''
    Task 7: Class

    Args:
        student_id: someone's student ID
        time: a certain time

    Returns:
        student: an Student object

    Hints:
        * Use Student(parameters1, parameters2 ...) to create an object
          and assign it to a variable
        * Use <created object>.<object function> to call object function
    '''
    # TODO: create a student object with different words to say
    student = None
    # End of TODO

    print(student.hello())
    return student


def task_8(
    img_url: str = 'https://i.imgur.com/B75zq0x.jpg'
) -> object:
    '''
    Task 8: Module

    Args:
        img_url: address of an image

    Returns:
        result_img: an PIL Image

    Hints:
        * Make sure you have installed the PIL package
        * Take a look at utils.py first
        * You could easily find answers with Google
    '''
    from urllib import request
    result_img = None

    # TODO: download the image from img_url with the request module
    # and add your student ID on it with draw_name() in the utils module
    # under src/.

    # You are allowed to change the img_url to your own image URL.

    # Display the image:
    # result_img.show()
    # Note: please comment this line when hand in.

    # If you are running on a server, use
    # result.save('test.jpg')
    # and copy the file to local or use Jupyter Notebook to render.

    # End of TODO

    return result_img
