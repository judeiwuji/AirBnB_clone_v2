#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes a session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters(id=""):
    """Return all states formatted in HTML"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    states = sorted(states, key=lambda d: d.name)
    amenities = sorted(amenities, key=lambda d: d.name)

    return render_template("0-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
