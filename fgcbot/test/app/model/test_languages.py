# -*- coding: utf-8 -*-

import unittest
from ....app.model.languages import Languages


class Test_Languages(unittest.TestCase):

	def test_Languages_simple_init(self):
		#Arrange#
		languages = Languages()
		#Action

		#Assert#
		self.assertTrue(languages.messages != [])
		self.assertTrue(languages.messages != [])