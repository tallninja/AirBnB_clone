#!/usr/bin/python3
"""
test module for testing file storage
"""

import datetime
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """test class for testing file storage
    """
    temp_file = ""

    @staticmethod
    def move_file(source, dest):
        with open(source, 'r', encoding='utf-8') as myFile:
            with open(dest, 'w', encoding='utf-8') as tempFile:
                tempFile.write(myFile.read())
        os.remove(source)

    def setUp(self):
        self.temp_file = storage.parent_directory + '/temp_store.json'
        self.move_file(storage.get_filepath(), self.temp_file)
        self.temp_objs = [BaseModel(), BaseModel(), BaseModel()]
        for obj in self.temp_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        self.move_file(self.temp_file, storage.get_filepath())
        del self.temp_objs

    def test_type(self):
        """type checks for FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_save(self):
        """tests save functionality for FileStorage
        """
        with open(storage.get_filepath(), 'r', encoding='utf-8') as myFile:
            dump = myFile.read()
        self.assertNotEqual(len(dump), 0)
        temp_d = eval(dump)
        key = self.temp_objs[0].__class__.__name__ + '.'
        key += str(self.temp_objs[0].id)
        self.assertNotEqual(len(temp_d[key]), 0)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(temp_d[key2], KeyError)
        except:
            pass

    def test_reload(self):
        """tests reload functionality for FileStorage
        """
        storage.reload()
        obj_d = storage.all()
        key = self.temp_objs[1].__class__.__name__ + '.'
        key += str(self.temp_objs[1].id)
        self.assertNotEqual(obj_d[key], None)
        self.assertEqual(obj_d[key].id, self.temp_objs[1].id)
        key2 = 'State.412409120491902491209491024'
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_delete_basic(self):
        """tests delete basic functionality for FileStorage
        """
        self.assertEqual(storage.delete(BaseModel()), True)
        self.assertEqual(storage.delete(self.temp_objs[2]), True)
        obj_d = storage.all()
        key2 = self.temp_objs[2].__class__.__name__ + '.'
        key2 += str(self.temp_objs[2].id)
        try:
            self.assertRaises(obj_d[key2], KeyError)
        except:
            pass

    def test_delete_badinput(self):
        """tests delete bad input functionality for FileStorage
        """
        self.assertEqual(storage.delete(None), False)
        self.assertEqual(storage.delete('mymodel'), False)

    def test_new_basic(self):
        """tests new basic functionality for FileStorage
        """
        obj = BaseModel()
        storage.new(obj)
        obj_d = storage.all()
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.assertEqual(obj_d[key] is obj, True)

    def test_new_badinput(self):
        """tests new bad input functionality for FileStorage
        """
        try:
            self.assertRaises(storage.new('jwljfef'), TypeError)
            self.assertRaises(storage.new(None), TypeError)
        except:
            pass
