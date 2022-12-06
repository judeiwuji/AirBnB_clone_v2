#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.user import User
from models.state import State
from models.city import City


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         description="")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         number_rooms=0)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         number_bathrooms=0)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         max_guest=0)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         price_by_night=0)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         latitude=0.0)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test",
                         longitude=0.0)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        user = User(first_name="test", last_name="test", email="t@t",
                    password="test")
        state = State(name="test")
        city = City(name="test city", state_id=state.id)
        new = self.value(user_id=user.id, city_id=city.id, name="test")
        self.assertEqual(type(new.amenity_ids), list)
