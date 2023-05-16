#!/usr/bin/python3
"""Testing users"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
	"""This is test for place class"""
	place = Place()
	def test_place(self):
		"""testing place class"""
		self.assertTrue(Place())
	
	def test_attr(self):
		"""testing the attributes of place class"""
		self.assertTrue(hasattr(self.place, "city_id"))
		self.assertTrue(hasattr(self.place, "user_id"))
		self.assertTrue(hasattr(self.place, "name"))
		self.assertTrue(hasattr(self.place, "description"))
		self.assertTrue(hasattr(self.place, "number_rooms"))
		self.assertTrue(hasattr(self.place, "number_bathrooms"))
		self.assertTrue(hasattr(self.place, "max_guest"))
		self.assertTrue(hasattr(self.place, "price_by_night"))
		self.assertTrue(hasattr(self.place, "latitude"))
		self.assertTrue(hasattr(self.place, "longitude"))
		self.assertTrue(hasattr(self.place, "amenity_ids"))
