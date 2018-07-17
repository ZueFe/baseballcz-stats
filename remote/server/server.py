"""
Flask app created to run on remote server.
Its purpose is to send data from FTP server to the client,
withou client needing to know the address of the FTP server.
"""

from flask import Flask, make_response, request
import requests
import constants as cs
import os

app = Flask(__name__)

@app.route('/')
def get_data():
    """
    Main page of the Flask app. Requires to recieve parameters
    to identify which file is being requested.

    URL parameters:
        * *category* - bat, field, pitcher, catcher
        * *type* - 0 for individual, 2 for team statistics

    :returns: Flask response containing data and information about file creation in text/csv format
    """
    category = request.args.get('category')
    t = request.args.get('type')

    if t == '0':   # INDIVIDUAL
        if category == 'bat':
            return get_csv(cs.IND_BATTER)
        elif category == 'field':
            return get_csv(cs.IND_FIELD)
        elif category == 'pitcher':
            return get_csv(cs.IND_PITCHER)
        elif category == 'catcher':
            return get_csv(cs.IND_CATCHER)
    elif t == '2':     # TEAM
        if category == 'bat':
            return get_csv(cs.TEAM_BATTER)
        elif category == 'field':
            return get_csv(cs.TEAM_FIELD)
        elif category == 'pitcher':
            return get_csv(cs.TEAM_PITCHER)
        elif category == 'catcher':
            return get_csv(cs.TEAM_CATCHER)

    return "Nothing to see here..."

def get_csv(f):
    """
    Fetches data from FTP server (defined in `constants <constants.html>`_) and
    return it as a response.

    :param f: File name to be retrieved
    :returns: Flask response containing data and information about file creation in text/csv format
    """
    r = requests.get('http://{}/{}'.format(os.environ['FTP_NAME'], f))
    response = make_response(r.content)
    cd = 'attachment; filename={}'.format(f)
    response.headers['Content-Disposition'] = cd
    response.headers['last-modified'] = r.headers['last-modified']
    response.mimetype='text/csv'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
