from pandas import read_csv
from plotly import graph_objects as go
from json import loads
from os.path import join


def plotter(obj):
    '''
    Shows a table with the query that the user sent on another page.
    '''
    dataObj = read_csv(join('outputFiles', 'output.csv'))

    jsondict = loads(obj)
    # Query on the dataframe
    for key, value in jsondict.items():
        dataObj = dataObj.query(f'{key} == @value')
    # Writing the filtered output to an output CSV file in outputFiles directory
    dataObj.to_csv(join('outputFiles', 'filtered_output.csv'))
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(dataObj.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[dataObj.IPAddress, dataObj.UserAgent, dataObj.RequestType, dataObj.API, dataObj.UserName, dataObj.EnterpriseID, dataObj.EnterpriseName, dataObj.StatusCode],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.show()
