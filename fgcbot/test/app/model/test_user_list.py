# -*- coding: utf-8 -*-

import unittest
from ....app.model.user_list import User_List


class Test_User_List(unittest.TestCase):

	def test_User_List_simple_init(self):
		#Arrange#
		user_list = User_List()
		#Action

		#Assert#
		self.assertEqual(user_list.user_dict, {})

	def test_User_List_new_user_first_user(self):
		#Arrange#
		user_list = User_List()
		id_user = "user1"
		#Action
		user_list.new_user(id_user)
		#Assert#
		self.assertEqual(len(user_list.user_dict), 1)
		self.assertTrue(id_user in user_list.user_dict.keys())

	def test_User_List_new_user_existing_user(self):
		#Arrange#
		user_list = User_List()
		id_user = "user1"		
		user_list.user_dict[id_user] = object
		#Action
		user_list.new_user(id_user)
		#Assert
		self.assertEqual(len(user_list.user_dict), 1)
		self.assertTrue(id_user in user_list.user_dict.keys())

	def test_User_List_get_user_inexisting_user(self):
		#Arrange#
		user_list = User_List()
		id_user = "user1"
		#Action
		user = user_list.get_user(id_user)
		#Assert
		self.assertEqual(len(user_list.user_dict), 1)
		self.assertTrue(id_user in user_list.user_dict.keys())

	def test_User_List_get_user_existing_user(self):
		#Arrange#
		user_list = User_List()
		id_user = "user1"		
		user_list.user_dict[id_user] = object
		#Action
		user = user_list.get_user(id_user)
		#Assert
		self.assertEqual(len(user_list.user_dict), 1)
		self.assertTrue(id_user in user_list.user_dict.keys())
		self.assertIs(user, object)

		