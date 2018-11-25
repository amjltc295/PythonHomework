# Python Homework
Python homework for Introduction to Computer (計算機概論), Fall 2018

## Introduction

In this homework, you will learn some basic techniques for Python, Git and CI/CD.


## Task 0: Environment Setup

### OS

If you are using Linux, perfect! Please ignore this part.

If you are using MacOS, good for you. Don't you consider using Linux?

If you are using other operation systems (I suppose it's Windows), you will probably have some troubles for this homework.

Windows is good for many things, but not for programming. Note that **TA will not answer any homework problem if you are using Windows**, so please have Linux installed. Ubuntu 16.04 or 18.04 is preferred.

If you are using Windows, please choose **one** of the following ways to use Linux:
1. (For Windows10 users) Use the Windows Subsystem for Linux (WSL). Instructions could be found [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
It is the most convinient way as you could use both Linux terminal and Windows at the same time. However, WSL dose not support CUDA drivers, which means you could not use your GPU in WSL, but GPU is not needed for this homework.
2. (For CSIE students) Use the CSIE workstation by SSH. See [NTU CSIE System Administration Team](https://wslab.csie.ntu.edu.tw/SSH_tutorial.html) for details. This is the easiest way but you could not install packages that requires root access in the future.
3. (For all users) Dual boot your OS with Ubuntu. Google key words like "Win10 dual boot Ubuntu". This is a bit tricky and may take a while, but you could enjoy the full utilities of Linux!
4. (For all users) Use a [portable Ubuntu USB](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#0) to boot. It is ligth-weighted and you could bring your Linux everywhere, but the memory is limited.
5. (Not suggested) Use vitual machines.
6. (Not suggested) Borrow a laptop with Linux.

For 2 and 3, use `<ctrl>+<alt>+T` to open the terminal after booting your Linux.

### GitHub

1. Please create a GitHub account.

    It would be better to use your NTU mail so that you would have the privilege to create private repositories.
    You could [add an SSH key](https://help.github.com/articles/connecting-to-github-with-ssh/) so that you don't need to verify the password every time when push/pull.

2. [Fork](https://help.github.com/articles/fork-a-repo/) this repository by clicking `fork` on the top-right of this page.

3. Clone your **forked** repository to local.
    ```
    git clone git@github.com:<your_github_account_name>/PythonHomework.git
    cd PythonHomework
    ```


### Miniconda

_"Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN"_ -- https://conda.io/docs/

Conda is a very powerful package for development. You could easily switch between environments (e.g, Python2/3, Pytorch0.2/0.4.1 ...), which is extremely helpful when you are working on several projects as they may have conflicts with one another. Conda also help you solve the package dependencies.

Miniconda is a light-weighted version of Conda. Installing Miniconda for Python3.7 is highly suggested. You could use Anaconda as well but it requires way more space and time.

1. Download installation file from [Miniconda](https://conda.io/miniconda.html) and install accrodingly, or run 
    ```
    wget repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```
    in your command line, and follow the instruction.

2. After installation, use `conda -V` to check.

    It should display something like `conda 4.5.11`. If you found `conda: command not found` or similar message, it probably means you did not add the path to the  conda binary to the environment variable `PATH`. Don't worry; just type `export PATH=~/miniconda3/bin:$PATH`  and try it again. It would be better to add `export PATH=~/anaconda3/bin:$PATH` to your `~/.bashrc`

3. Create a new environment from scatch `conda create -n <any name>` or from file (suggested) `conda env create -f environement.yaml`

4. Activate the environment by `source activate <name>`.
    Your terminal should now look like this:
    ```
    (your_environment_name) user@PC-name $
    ```
    which means you are in the environment `your_environment_name` now. If you want to change to another environment, type `source deactivate`

5. Install Flake8 in the environment
    ```
    (your_environment_name) user@PC-name $ conda install flake8
    (your_environment_name) user@PC-name $ flake8 .
    ```
    It should prompt some warning messages regarding to Python style and syntax:
    ```
    ./src/sample_code.py:1:1: E902 IndentationError: unindent does not match any outer indentation level
    ./src/sample_code.py:38:17: E225 missing whitespace around operator
    ./src/sample_code.py:39:22: E999 IndentationError: unindent does not match any outer indentation level
    ```
    You need to fix them later to get the points of Flake8.


### Others (optional)

The following tools would **significantly** improve your coding efficiency if you learn how to use it. Please at least give [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) a try.
* Install [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh). OMZ is a wonderful command line configuration. It includes auto-completion, alias, beautiful display and many more utilities.
* Use Vim > 8.0 and install good [vimrc](https://github.com/amix/vimrc)
* Install [ALE](https://github.com/w0rp/ale) for syntax/style check
* Install [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) for code auto-completion
* Install [ack](https://github.com/beyondgrep/ack2) to search local code
* Use tmux and install [oh-my-tmux](https://github.com/gpakosz/.tmux)



## Task 1 - 8
Please copy `src/students/sample_code.py` to `src/students/<your student ID>.py` first and edit that file.

### Task 1: Basic Syntax and Flake8 Checker

### Task 2: Data Types: String, Integer, Float, List, Dictionary

### Task 3: Conditions

### Task 4: For and While Loop

### Task 5: I/O

### Task 6: Function

### Task 7: Class

### Task 8: Modules


## Repository Structure
```
├── client
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   └── manifest.json
│   ├── README.md
│   └── src
│       ├── App.css
│       ├── App.js
│       ├── App.test.js
│       ├── index.css
│       ├── index.js
│       ├── logo.svg
│       ├── python.png
│       ├── results.js
│       └── serviceWorker.js
├── environment.yaml
├── netlify.toml
├── Procfile
├── README.md
├── LICENSE
├── requirements.txt
└── src
    ├── autograder.py
    ├── logging_config.py
    ├── server.py
    ├── students 
    │   └── sample_code.py
    └── utils.py

```
`client/` is for the frontend. It is written in ReactJS, based on [facebook/create-react-app](https://github.com/facebook/create-react-app)

`src/` is for the backend and homework. The `server.py` uses Flask to build a backend server. The rest are files for homework. Students should only create a file under `src/students` to submit their homework.

`environment.yaml` is for conda environemnt.

`netlify.toml` is for the Netlify settings. It is used to deploy the frontend.

`Procfile` is for the Heroku settings. It is used to deploy the backend.

`requirements.txt` is for pip environemnt, required by Heroku.


## Grading

### Send a Pull Request (PR) (20%)

Please send a Pull Request (PR) to the *master* branch.

Your PR should include only 1 file change (i.e., `<your student ID>.py`).

Please name the title as `[status] studentID name` (e.g., `[test] r07944019 張雅量`)

TA would review your code once you mark your PR as `[Needs Review]`.

The CI test will tell you if your code is runnable.

If the PR is merged, you will be graded immediately for the tasks and get this 20%.

The results could be seen [here](https://pythonhomework.netlify.com/)

If you are not satisfied with your score, you could send another PR.

However, each following make-up PR would result in *10 points off*.


### Pass the tests for each task (60%)

You could use `python autograder.py -student_id <student ID>` to see if you pass all the tasks for the public data.

You will know the score for the private data once the PR is merged.

### Pass the Flake8 checker (10%)

Please use `flake8 src/<student ID>.py` to see if your file has passed the Flake8 checker.

### Write readable code and commit message (10%)

Please write readable code and commit message.

Some examples: 
* [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).
* [zedr/clean-code-python](https://github.com/zedr/clean-code-python)

### Bonus (up to 50%)

* Rebase before the Pull Request (10%)

* Create an issue for a bug / unclear part of this repository (10%)

* Create an issue for a technical problem that could not be solved easily (e.g. by Google) (10%)

* Answer an issue that could not be solved easily (10%)

* Send a PR and solve a bug in this repository (30%)


## Liscence

MIT

## Author

Ya-Liang Chang (Allen) [amjltc295](https://github.com/amjltc295) - **Homework design, backend, frontend, CI/CD**
