#!/usr/bin/python3
"""
Defines unittests for base.py.
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def setup(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
