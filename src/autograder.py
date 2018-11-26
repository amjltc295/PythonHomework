import os
import argparse
import importlib
from time import gmtime, strftime

import yaml

from logging_config import logger


def parse_args():
    ''' Parse the arguments by the argparse module.

    Additional argurments could be defined in this function.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-student_id', type=str, help="Your student ID, such as r07944019",
        required=True
    )
    parser.add_argument(
        '-tasks', type=int, nargs="+",
        default=[1, 2, 3, 4, 5, 6, 7, 8],
        help="The tasks you want to test (dafault: all)"
    )

    parser.add_argument(
        '-all', action='store_true',
        help="Grade all files in students/"
    )
    args = parser.parse_args()
    return args


def parse_yaml(filename):
    with open(filename, 'r') as fin:
        test_data = yaml.load(fin)
    return test_data


def autograde(student_id, tasks):
    ''' Grade tasks specified in args.'''
    # Get path of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Check if student's file exists
    student_file = os.path.join(dir_path, 'students', student_id + '.py')
    assert os.path.exists(student_file), f"{student_file} not exists"

    # Import student's file as module
    student_module = importlib.import_module(f'students.{student_id}')  # NOQA

    # Load testing data
    test_data_filename = os.path.join(
        dir_path, 'test_data', 'public_data.yaml')
    test_data = parse_yaml(test_data_filename)
    print(test_data)

    # Load testing answers
    test_answers_filename = os.path.join(
        dir_path, 'test_data', 'public_answers.yaml')
    test_answers = parse_yaml(test_answers_filename)
    print(test_answers)

    # Run each task
    points = {}
    for task_id in tasks:
        logger.info(f"Testing Task {task_id}")
        # Use try-except to catch erros in order to run througth all tasks
        try:
            # This part is a bit dirty. If you have a better way, send a PR to
            # improve!
            if task_id == 7:
                time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                student = student_module.task_7(student_id, time)
                assert student.student_id == student_id
                assert student.time == time
                assert student.words_to_say != "initial value"
                points[task_id] = test_answers[task_id]['points']
            elif task_id == 8:
                image = student_module.task_8()
                assert str(type(image))[8:11] == 'PIL', type(image)
                points[task_id] = test_answers[task_id]['points']
            else:
                result = eval(
                    f"student_module.task_{task_id}(**{test_data[task_id]})")
                if test_answers[task_id]['check'] == 0:
                    points[task_id] = test_answers[task_id]['points']
                elif test_answers[task_id]['check'] == 1:
                    if result == test_answers[task_id]['answer']:
                        points[task_id] = test_answers[task_id]['points']
                    else:
                        logger.error(f"Your result {result}")
                        logger.error(
                            f"is different from ")
                        logger.error(f"{test_answers[task_id]['answer']}")
                        points[task_id] = 0
                elif test_answers[task_id]['check'] == 2:
                    if set(result) == set(test_answers[task_id]['answer']):
                        points[task_id] = test_answers[task_id]['points']
                    else:
                        logger.error(f"Your result {result}")
                        logger.error(
                            f"is different from ")
                        logger.error(f"{test_answers[task_id]['answer']}")
                        points[task_id] = 0
                else:
                    points[task_id] = None

        except Exception as err:
            points[task_id] = 0
            logger.error(err, exc_info=True)
    logger.info(f"Points {points}")


if __name__ == '__main__':
    args = parse_args()
    if args.all:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        student_ids = os.listdir(os.path.join(dir_path, 'students'))
        student_ids = [
            x[:-3] for x in student_ids if x[-3:] == '.py' and
            'sample' not in x
        ]
        for student_id in student_ids:
            autograde(student_id, args.tasks)
    else:
        autograde(args.student_id, args.tasks)
