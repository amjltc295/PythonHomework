import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))  # NOQA
sys.path.append(dir_path)  # NOQA
import importlib

from flask import Flask, jsonify
from flask_cors import CORS
from flake8.api import legacy as flake8

from logging_config import logger


app = Flask(__name__)
CORS(app)

TASK_NUM = 8


@app.route('/hi', methods=['GET'])
def hi():
    return jsonify(
        {"message": "Hi! This is the server for Introduction to Computer."})


def grade():
    '''
    Get test results of all students in src/students/
    '''

    # Get path of this file

    # Save results to a dict
    results = {}

    student_ids = os.listdir(os.path.join(dir_path, 'students'))
    student_ids = [x[:-3] for x in student_ids if x[-3:] == '.py']
    for student_id in student_ids:
        student_result = {}
        student_module = None
        try:
            student_module = importlib.import_module(f'src.students.{student_id}')  # NOQA
        except Exception as err:
            logger.info(err, exc_info=True)
            student_result['import'] = "Failed"
        else:
            student_result['import'] = "Success"

        # Check each task
        for task_id in range(1, TASK_NUM + 1):
            logger.info(f"Testing {student_id} Task {task_id}")
            try:
                eval(f"student_module.task_{task_id}()")
            except Exception as err:
                logger.error(err, exc_info=True)
                student_result[f"task_{task_id}"] = "WA"
            else:
                student_result[f"task_{task_id}"] = "AC"

        # Check flake8
        style_guide = flake8.get_style_guide()
        student_file = os.path.join(dir_path, 'students', student_id + '.py')
        report = style_guide.check_files(
            [student_file]
        )
        if (report.get_statistics('E') == [] and
                report.get_statistics('W') == []):
            logger.info(report.get_statistics('E'))
            logger.info(report.get_statistics('W'))
            student_result['flake8'] = "Pass"
        else:
            student_result['flake8'] = "Fail"
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
