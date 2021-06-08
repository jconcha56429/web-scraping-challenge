from flask import Flask, render_template
app = Flask(__name__)
from mission_to_mars  import scrape
import json
app = Flask(__name__)

@app.route('/')
def echo():
    return(scrape())

if __name__ == '__main__':
    app.run(debug=True)