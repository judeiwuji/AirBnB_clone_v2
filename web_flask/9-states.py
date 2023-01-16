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


@app.route("/states", strict_slashes=False)
@app.route("/states/<string:id>", strict_slashes=False)
def states(id=""):
    """Return all states formatted in HTML"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda d: d.name)
    if id != "":
        state = None
        for d in states:
            if d.id == id:
                state = d
                break
        if state is not None:
            state.cities = sorted(state.cities, key=lambda d: d.name)
        return render_template("9-states.html", state=state)
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
