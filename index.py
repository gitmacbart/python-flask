from flask import Flask, Response, __version__
app = Flask(__name__)
source = 'https://github.com/zeit/now-examples/tree/master/python-flask'
css = '<link rel="stylesheet" href="/css/style.css" />'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("%s<h1>Flask for Arnaud version 2</h1><p>You are viewing a Flask application written in Python running on Now 2.0.</p><p>GO and Visit the <a href='./about'>about</a> page or view the <a href='%s'>source code</a>.</p>" % (css, source), mimetype='text/html')
