# -*- coding: utf-8 -*-

from .user import User
import cPickle as pickle
import os


class User_List (object):
	def __init__(self):
		dirname = os.path.dirname
		self.path_users_file =  os.path.join(dirname(dirname(dirname(__file__))), 'data', 'fgc_user_data.p')
		try:			
			with open(self.path_users_file, 'rb') as pickle_file:
				self.user_dict = pickle.load( pickle_file )
		except Exception as error:
			print error
			print "error loading users configuration"
			self.user_dict = {}

	def new_user(self, user_id):
			self.user_dict[user_id] = User()

	def get_user(self, user_id):
		if not user_id in self.user_dict:
			self.user_dict[user_id] = User()
		return self.user_dict[user_id]
	def save_users(self):
		try:			
			pickle.dump( self.user_dict, open( self.path_users_file, "wb" ))
		except Exception as error:
			print error
			print "error loading users configuration"