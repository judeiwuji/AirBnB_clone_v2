#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes a session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Return all states and cities formatted in HTML"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda d: d.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda d: d.name)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
