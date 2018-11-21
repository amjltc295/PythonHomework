# Python Homework
Python homework for Introduction to Computer (計算機概論), Fall 2018

## Introduction

In this homework, you will learn some basic techniques for Python, Git and CI/CD.


### Task 0: Environment Setup

#### OS

If you are using Linux, perfect! Please ignore this part.

If you are using MacOS, good for you. Don't you consider using Linux?

If you are using other operation systems (I suppose it's Windows), you will probably have some troubles for this homework.

Windows is good for many things, but for not programming. Note that **TA will not answer any homework problem if you are using Windows**, so please have Linux installed. Ubuntu 16.04 or 18.04 is preferred.

If you are using Windows, please choose one of the following ways to use Linux:
1. (For Windows10 users) Use the Windows Subsystem for Linux (WSL). Instructions could be found [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
It is the most convinient way as you could use both Linux terminal and Windows at the same time. However, WSL dose not support CUDA drivers, which means you could not use your GPU in WSL, but GPU is not needed for this homework.
2. (For CSIE students) Use the CSIE workstation by SSH. See [NTU CSIE System Administration Team](https://wslab.csie.ntu.edu.tw/SSH_tutorial.html) for details. This is the easiest way but you could not install packages that requires root access in the future.
3. (For all users) Dual boot your OS with Ubuntu. Google key words like "Win10 dual boot Ubuntu". This is a bit tricky and may take a while, but you could enjoy the full utilities of Linux!
4. (For all users) Use a [portable Ubuntu USB](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#0) to boot. It is ligth-weighted and you could bring your Linux everywhere, but the memory is limited.
5. (Not suggested) Use vitual machines.
6. (Not suggested) Borrow a laptop with Linux.

#### Anaconda/Miniconda
### Task 1: Basic Syntax and Flake8 Checker

### Task 2: Data Types: String, Integer, Float, List, Dictionary

### Task 3: I/O

### Task 4: Conditions

### Task 5: For and While Loop

### Task 6: Function

### Task 7: Class

### Task 8: Modules


## Grading

### Send a Pull Request (PR) (20%)

Please send a Pull Request (PR) to the *master* branch.

Your PR should include only 1 file change.

Please name the title as `[status] studentID name` (e.g., `[test] r07944019 張雅量`)

TA would review your code once you mark your PR as `[Needs Review]`.

The CI test will tell you if your code is runnable.

If the PR is merged, you will be graded immediately for the tasks and get this 20%.

The results could be seen [here]()

If you are not satisfied with your score, you could send another PR.

However, each following make-up PR would result in *10 points off*.


### Pass the tests for each task (60%)

You could use `pytest -<student ID>` to see if you pass all the tasks for the public data.

You will know the score for the private data once the PR is merged.

### Pass the Flake8 checker (10%)

Please use `flake8 src/<student ID>.py` to see if your file has passed the Flake8 checker.

### Write readable code and commit message (10%)

Please write readable code and commit message.

Some examples could be found [here]().

### Bonus (up to 50%)

* Rebase before the Pull Request (10%)

* Create an issue for a bug / unclear part of this repository (10%)

* Create an issue for a technical problem that could not be solved easily (e.g. by Google) (10%)

* Answer an issue that could not be solved easily (10%)

* Send a PR and solve a bug in this repository (30%)



