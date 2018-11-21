import os
import argparse
import importlib

from logging_config import logger


def parse_args():
    ''' Parse the arguments by the argparse module.

    Additional argurments could be defined in this function.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-student_id', type=str, help="Your student ID, such as r07944019"
    )
    parser.add_argument(
        '-tasks', type=int, nargs="+",
        default=[1, 2, 3, 4, 5, 6, 7, 8],
        help="The tasks you want to test (dafault: all)"
    )
    args = parser.parse_args()
    return args


def autograde(args):
    ''' Grade tasks specified in args.'''
    # Get path of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Check if student's file exists
    student_file = os.path.join(dir_path, 'students', args.student_id + '.py')
    assert os.path.exists(student_file), f"{student_file} not exists"

    # Import student's file as module
    student_module = importlib.import_module(f'students.{args.student_id}')  # NOQA

    # Run each task
    for task_id in args.tasks:
        logger.info(f"Testing Task {task_id}")
        # Use try-except to catch erros in order to run througth all tasks
        try:
            eval(f"student_module.task_{task_id}()")
        except Exception as err:
            logger.error(err, exc_info=True)


if __name__ == '__main__':
    args = parse_args()
    autograde(args)
