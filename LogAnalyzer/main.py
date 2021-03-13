'''
Main file for flask to run.
Runs a local server on 127.0.0.1.

Only the necessary packages/functions are imported
'''

from flask import Flask, render_template, request, redirect
from lib.logAnalyser import parseFile
from werkzeug.utils import secure_filename
from json import dumps
from lib.query import plotter
from os.path import join
from time import perf_counter


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'tmp'


@app.route('/')
def home():
    return render_template('homePage.html')


@app.route('/query', methods=['POST'])
def query():
    '''
    Converts the input file from .log to .csv.
    the log file is stored in tmp folder.
    You can clear the tmp folder regularly if the log files are taking too much space.
    the csv file is stored in output file
    '''
    # Checks the validity of input file-name
    try:
        f = request.files['file']
    except:
        return redirect('http://127.0.0.1:5000')
    if f.filename == '' or f.filename.split('.')[-1] != 'log':
        return redirect('http://127.0.0.1:5000')

    x = perf_counter()
    # Saves to tmp folder
    f.save(join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    print(f'{perf_counter()-x}s for saving the file.')

    parseFile(f.filename)
    return render_template('queryingPage.html')


@app.route('/output', methods=['POST'])
def output():
    '''
    Plotting the graph using query from lib folder
    '''
    jsonObj = dict()
    for key, value in request.form.items():
        if value != '':
            jsonObj[key] = value
    del jsonObj['submit2']
    # filtering the necessary key value pairs
    jsonObj = dumps(jsonObj, indent=2)
    # plots the table on a new page
    plotter(jsonObj)
    return '<center>Go back to query again.</center>'


if __name__ == "__main__":
    app.run()
