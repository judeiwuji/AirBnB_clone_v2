#!/usr/bin/python3
"""Contains unit test cases for console.py"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review


class TestHBNBCommandDoCreate(unittest.TestCase):
    def setUp(self):
        if os.path.exists("file.json"):
            os.unlink('file.json')

    def tearDown(self):
        if os.path.exists("file.json"):
            os.unlink('file.json')

    def test_create_user(self):
        """Test create user"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User first_name="john"\
                                  last_name="doe" email="john@doe"\
                                  password="doesecret"')
            obj_id = f.getvalue().strip()
            obj = storage.all().get('User.{}'.format(obj_id), None)
            self.assertIsInstance(obj, User)
            self.assertEqual(obj.first_name, "john")
            self.assertEqual(obj.last_name, "doe")

    def test_create_state(self):
        """Test create state"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Lagos"')
            obj_id = f.getvalue().strip()
            obj = storage.all().get('State.{}'.format(obj_id), None)
            self.assertIsInstance(obj, State)
            self.assertEqual(obj.name, "Lagos")

    def test_create_city(self):
        """Test create city"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Abuja"')
            state_id = f.getvalue().strip()
            cmd = 'create City name="gwagwalanda" state_id={}'.\
                  format(state_id)
            HBNBCommand().onecmd(cmd)
            obj_id = f.getvalue().strip().splitlines()[-1]
            obj = storage.all().get('City.{}'.format(obj_id), None)
            self.assertIsInstance(obj, City)
            self.assertEqual(obj.name, "gwagwalanda")

    def test_create_place(self):
        """Test create place"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Umuahaia"')
            state_id = f.getvalue().strip()
            cmd = 'create City name="aba" state_id={}'.\
                  format(state_id)
            HBNBCommand().onecmd(cmd)
            city_id = f.getvalue().strip().splitlines()[-1]
            cmd = 'create User first_name="jane"\
                  last_name="doe" email="jane@doe"\
                  password="janesecret"'
            HBNBCommand().onecmd(cmd)
            user_id = f.getvalue().strip().splitlines()[-1]

            HBNBCommand().onecmd('create Place city_id="{}" user_id="{}"\
                name="My_little_house" number_rooms=4 number_bathrooms=2\
                max_guest=10 price_by_night=300 latitude=37.773972\
                longitude=-122.431297'.format(city_id, user_id))
            obj_id = f.getvalue().strip().splitlines()[-1]

            obj = storage.all().get('Place.{}'.format(obj_id), None)
            self.assertIsInstance(obj, Place)
            self.assertEqual(obj.city_id, city_id)
            self.assertEqual(obj.user_id, user_id)
            self.assertEqual(obj.name, "My little house")
            self.assertEqual(obj.number_rooms, 4)
            self.assertEqual(obj.number_bathrooms, 2)
            self.assertEqual(obj.max_guest, 10)
            self.assertEqual(obj.price_by_night, 300)
            self.assertAlmostEqual(obj.latitude, 37.773972, 2)
            self.assertAlmostEqual(obj.longitude, -122.431297, 2)

    def test_create_review(self):
        """Test create review"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Edo"')
            state_id = f.getvalue().strip()
            cmd = 'create City name="Benin" state_id={}'.\
                  format(state_id)
            HBNBCommand().onecmd(cmd)
            city_id = f.getvalue().strip().splitlines()[-1]
            cmd = 'create User first_name="john"\
                  last_name="smith" email="john@smith"\
                  password="johnsecret"'
            HBNBCommand().onecmd(cmd)
            user_id = f.getvalue().strip().splitlines()[-1]

            HBNBCommand().onecmd('create Place city_id="{}" user_id="{}"\
                name="My_little_house" number_rooms=4 number_bathrooms=2\
                max_guest=10 price_by_night=300 latitude=37.773972\
                longitude=-122.431297'.format(city_id, user_id))
            place_id = f.getvalue().strip().splitlines()[-1]

            HBNBCommand().onecmd('create Review place_id="{}" user_id="{}"\
                                  text="nice_place"'.format(place_id, user_id))
            obj_id = f.getvalue().strip().splitlines()[-1]

            obj = storage.all().get('Review.{}'.format(obj_id), None)
            self.assertIsInstance(obj, Review)
            self.assertEqual(obj.place_id, place_id)
            self.assertEqual(obj.user_id, user_id)
            self.assertEqual(obj.text, "nice place")


if __name__ == "__main__":
    unittest.main(TestHBNBCommandDoCreate)
