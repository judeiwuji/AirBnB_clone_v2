#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Return all states formatted in HTML"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """closes a session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
