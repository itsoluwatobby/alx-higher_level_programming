#!/usr/bin/python3
'''
Test module for the rectangle.py file
'''
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def setUp(self):
        '''
        Create an instance of a Rectangle to be used across the tests
        '''
        self.rec = Rectangle(20, 5, 0, 0, 25)
        self.rec1 = Rectangle(8, 2)

    def tearDown(self):
        '''
        Deletes the instance used for testing
        '''
        del self.rec
        del self.rec1

    def test_2_pars(self):
        # Will be 3 because in the base tests we created two instances
        self.assertEqual(self.rec.width, 20)
        self.assertEqual(self.rec.height, 5)

    def test_no_attributes(self):
        '''
        When no argument is passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_validators(self):
        # When more than five arguments are passed
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 4, 5, 5, 6)

    def test_width_length_validator(self):
        '''
        When non int type is passed as a parameter
        '''
        with self.assertRaises(TypeError):
            r = Rectangle("a", "b")

        with self.assertRaises(TypeError):
            r = Rectangle(5, "b")

        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, "a", "b")

        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, 6, "b")

    def test_parameter_value(self):
        '''
        When values that are less than or equal to 0 are passed as parameters
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(6, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(-2, -3)

        with self.assertRaises(ValueError):
            r = Rectangle(4, -4)

        with self.assertRaises(ValueError):
            r = Rectangle(7, 8, -4, -3)

        with self.assertRaises(ValueError):
            r = Rectangle(7, 8, 4, -3)

    def test_id(self):
        '''
        Check that the correct id is asigned
        '''
        self.assertEqual(self.rec.id, 25)

    def test_attributes_getter(self):
        '''
        Test that the attributes have been set
        '''
        self.assertEqual(self.rec.width, 20)
        self.assertEqual(self.rec.height, 5)
        self.assertEqual(self.rec.x, 0)
        self.assertEqual(self.rec.y, 0)

    def test_attributes_setters(self):
        '''
        Test that setter methods work correctly
        '''
        self.rec.width = 5
        self.assertEqual(self.rec.width, 5)
        self.rec.height = 20
        self.assertEqual(self.rec.height, 20)
        self.rec.x = 34
        self.assertEqual(self.rec.x, 34)
        self.rec.y = 4
        self.assertEqual(self.rec.y, 4)

    def test_attribute_setters_validation(self):
        '''
        Test that validation is properly done with setters
        '''
        with self.assertRaises(TypeError):
            self.rec.width = "r"

        with self.assertRaises(TypeError):
            self.rec.height = "r"

        with self.assertRaises(TypeError):
            self.rec.x = "r"

        with self.assertRaises(TypeError):
            self.rec.x = "r"

        with self.assertRaises(ValueError):
            self.rec.width = 0

        with self.assertRaises(ValueError):
            self.rec.height = 0

        with self.assertRaises(ValueError):
            self.rec.width = -25

        with self.assertRaises(ValueError):
            self.rec.height = -120

        with self.assertRaises(ValueError):
            self.rec.x = -21

        with self.assertRaises(ValueError):
            self.rec.y = -80

    def test_area(self):
        '''
        Test that the correct area is returned
        '''
        self.assertEqual(self.rec1.area(), 16)

    def test_display(self):
        '''
        Test that display works corectly
        '''
        pass
