# -*- coding: utf-8 -*-
import unittest
from mock import MagicMock
from mock import patch

from ....app.controller.core import Core

class Test_Core (unittest.TestCase):
	@patch('fgcbot.app.controller.core'+'.Logger')
	@patch('fgcbot.app.controller.core'+'.Persistance')
	@patch('fgcbot.app.controller.core'+'.Message_Builder')
	@patch('fgcbot.app.controller.core'+'.User_List')
	def test_Core_simple_init(self, user_patch, msg_patch, pers_patch, log_patch):
		#Arrange#
		c = Core()

		#Action

		#Assert#
		self.assertIs(c.persistance, pers_patch())
		self.assertIs(c.message_builder, msg_patch())
		self.assertIs(c.user_list, user_patch())
		self.assertIs(c.logger, log_patch())

if __name__ == '__main__':
	unittest.main()
