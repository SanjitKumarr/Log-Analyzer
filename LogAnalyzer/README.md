## LOG ANALYSER

Analyzes log files with specific format and assumptions.(Assumptions are mentioned in `Assumptions` file. Refer that file to understand the limitations)

### Requirements:

Python3 is expected as the interpreter. Below are the breif requirements:

1. flask
2. pandas
3. plotly
4. ipython
5. tabulate

`requirements.txt` already contains all the specific requirements. To install them, run:
`pip3 install -r requirements.txt`
Although you can run this straightaway, it is recommended to have it installed on a `virtualenv` for maintaining isolation from global environment.

### Running the server:

1. To start the flask server, run:
   `python3 main.py`
2. Visit `127.0.0.1:5000`, upload the log file, pass in some queries you want to see and you have your results.

All your log files that are uploaded are present in `tmp/` folder.

`Logfiles/` contains `TestFileGenerator.py` which generates a test log file with all the assumptions in mind.
Run below command with `logs` being the number of logs for in the file:
`python3 TestFileGenerator.py <logs>`
