# -*- coding: utf-8 -*-

import unittest
from ....app.model.data import Data


class Test_Data(unittest.TestCase):

	def test_Data_simple_init(self):
		#Arrange#
		data = Data()
		#Action

		#Assert#
		self.assertTrue('stations' in data.data.keys())
		self.assertTrue('languages' in data.data.keys())