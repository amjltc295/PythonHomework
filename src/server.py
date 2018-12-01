import os
import sys
import urllib.request
DIR_PATH = os.path.dirname(os.path.realpath(__file__))  # NOQA
sys.path.append(DIR_PATH)  # NOQA

from flask import Flask, jsonify
from flask_cors import CORS

from logging_config import logger
from autograder import autograde, check_flake8


app = Flask(__name__)
CORS(app)

TASK_NUM = 8


@app.route('/hi', methods=['GET'])
def hi():
    return jsonify(
        {"message": "Hi! This is the server for Introduction to Computer."})


def get_data_and_ans_paths():
    public_data_filename = os.path.join(
        DIR_PATH, 'test_data', 'public_data.yaml')
    public_ans_filename = os.path.join(
        DIR_PATH, 'test_data', 'public_answers.yaml')

    private_data_filename = os.path.join(
        DIR_PATH, 'test_data', 'private_data.yaml')
    private_ans_filename = os.path.join(
        DIR_PATH, 'test_data', 'private_answers.yaml')

    # Dowonload private data
    try:
        private_data_url = os.environ.get('PRIVATE_DATA_URL')
        urllib.request.urlretrieve(private_data_url, private_data_filename)
        private_ans_url = os.environ.get('PRIVATE_ANS_URL')
        urllib.request.urlretrieve(private_ans_url, private_ans_filename)
    except Exception as err:
        logger.info(err, exc_info=True)

    return (
        public_data_filename, public_ans_filename,
        private_data_filename, private_ans_filename
    )


def grade():
    '''
    Get test results of all students in src/students/
    '''
    # Save results to a dict
    results = {}

    student_ids = os.listdir(os.path.join(DIR_PATH, 'students'))
    student_ids = [x[:-3] for x in student_ids if x[-3:] == '.py']
    for student_id in student_ids:
        student_result = {}

        (public_data_filename, public_ans_filename, private_data_filename,
            private_ans_filename) = get_data_and_ans_paths()
        # Test public data
        try:
            logger.info("Testing public data")
            student_result['public_scores'] = autograde(
                student_id, range(1, TASK_NUM + 1),
                public_data_filename, public_ans_filename
            )
            student_result['import'] = "Success"
        except Exception as err:
            logger.info(err, exc_info=True)
            student_result['import'] = "Failed"

        # Test private data
        try:
            logger.info("Testing private data")
            student_result['private_scores'] = autograde(
                student_id, range(1, TASK_NUM + 1),
                private_data_filename,
                private_ans_filename
            )
        except Exception as err:
            logger.info(err, exc_info=True)

        # Check flake8
        student_file = os.path.join(DIR_PATH, 'students', student_id + '.py')
        student_result['flake8'] = check_flake8(student_file)

        # Add to all results
        results[student_id] = student_result
    return {
        "results": results,
        "task_num": TASK_NUM,
        "student_num": len(student_ids)
    }


@app.route('/get_results', methods=['GET'])
def get_results():
    return jsonify(results)


results = grade()
if __name__ == "__main__":
    app.run()
