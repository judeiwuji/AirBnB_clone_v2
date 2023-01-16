#!/usr/bin/python3
""" Module for testing DbStorage"""
import unittest
import MySQLdb
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models import storage
from os import getenv


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "DBStorage is required")
class TestDBStorage(unittest.TestCase):
    """ Class to test the DbStorage method """

    def setUp(self):
        """ Set up test environment """
        DB_USER = getenv('HBNB_MYSQL_USER')
        DB_PASS = getenv('HBNB_MYSQL_PWD')
        DB_HOST = getenv('HBNB_MYSQL_HOST')
        DB_NAME = getenv('HBNB_MYSQL_DB')
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER,
                             passwd=DB_PASS, db=DB_NAME)
        self.cursor = db.cursor()

    def tearDown(self):
        """ Remove storage file at end of tests """
        self.cursor.close()

    def test_new(self):
        """ New object is correctly added to db """
        new = State(name="Lagos")
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_save(self):
        """ DBStorage save method """
        new = State(name="Edo")
        new.save()
        storage.save()
        self.assertIsInstance(storage.all(State), dict)

    def test_reload(self):
        """ DBStorage db is successfully loaded """
        new = State(name="Imo")
        new.save()
        storage.reload()
        for obj in storage.all(State).values():
            loaded = obj
        self.assertIsInstance(loaded, State)

    def test_user_save(self):
        """ User save method calls storage save """
        new = User(first_name="john", last_name="doe",
                   email="doe@test", password="doesecret")
        new.save()
        sql = "SELECT * FROM users WHERE id=%s"
        self.cursor.execute(sql, (new.id,))
        self.assertIsInstance(self.cursor.fetchone(), tuple)

    def test_db_storage_all(self):
        """ Confirm all returns a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = State(name="Abuja")
        new.save()
        _id = new.to_dict()['id']
        for key, value in storage.all(State).items():
            temp_key = key
            temp_value = value
        self.assertEqual(temp_key, 'State' + '.' + temp_value.id)

    def test_storage_var_created(self):
        """ DBStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)


if __name__ == "__main__":
    unittest.main(TestDBStorage)
