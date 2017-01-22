# -*- coding: utf-8 -*-

import unittest
from ....app.model.user import User


class Test_User(unittest.TestCase):
	def test_User_simple_init_empty(self):
		#Arrange#
		user = User()
		#Action

		#Assert#
		self.assertEqual(user.origin, None)
		self.assertEqual(user.origin_id, None)
		self.assertEqual(user.destiny, None)
		self.assertEqual(user.origin_id, None)
		self.assertEqual(user.language, None)
		self.assertEqual(user.date, None)
		self.assertEqual(user.time, None)
		self.assertEqual(user.current_button, None)