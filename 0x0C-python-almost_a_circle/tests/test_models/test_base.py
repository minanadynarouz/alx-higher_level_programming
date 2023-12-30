#!/usr/bin/python3
"""Tests for the Base class with unittest"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_instantiation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_exist(self):
        self.assertEqual(Base.to_json_string([{'id': 100}]), '[{"id": 100}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_exist(self):
        self.assertEqual(Base.from_json_string('[{ "id": 100 }]'), [{'id': 100}])


if __name__ == '__main__':
    unittest.main()
