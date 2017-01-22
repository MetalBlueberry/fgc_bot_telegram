# -*- coding: utf-8 -*-
import re
from ..constants import *
from ..model.user_list import User_List
from .message_builder import Message_Builder
from .persistance import Persistance
from .logger import Logger
from datetime import datetime

class Core (object):
	def __init__(self):
		self.persistance = Persistance()
		self.message_builder = Message_Builder()	
		self.user_list = User_List()
		self.logger = Logger()
	
	def start_chat(self, user_id):
		self.user_list.new_user(user_id)
		message = self.message_builder.get_message_by_id(MESSAGE.WELCOME)
		buttons_list = self.message_builder.get_buttons_text_list()
		return message, buttons_list

	def press_modifiable_button(self, user_id, button_id):
		user = self.user_list.get_user(user_id)
		user.current_button = button_id
		return self.message_builder.get_modify_button_message(button_id, user.language)

	def press_go_button(self, user_id):
		user = self.user_list.get_user(user_id)

		buttons_list = self.message_builder.get_buttons_text_list(user.origin, user.destiny, user.language, user.time, user.date)
		user.current_button = None

		if not user.origin_id or not user.destiny_id:
			output_message = self.message_builder.get_message_by_id(MESSAGE.TRIP.EMPTY, user.language)
		elif user.origin_id == user.destiny_id:
			output_message = self.message_builder.get_message_by_id(MESSAGE.TRIP.SAME, user.language)
		elif not self.persistance.is_same_line(user.origin_id, user.destiny_id):
			output_message = self.message_builder.get_message_by_id(MESSAGE.TRIP.LINE, user.language)
		else:
			response = self.persistance.calculate_trip(user.origin_id, user.destiny_id, user.time, user.date)
			output_message = self.message_builder.get_trip_schedule_message(user.origin, user.destiny, response, user.language)
			user.date = None
			user.time = None
		
		buttons_list = self.message_builder.get_buttons_text_list(user.origin, user.destiny, user.language, user.time, user.date)
		self.logger.write_entry(user_id, user.origin, user.destiny, user.time, user.date)
		return output_message, buttons_list

	def set_station(self, user_id, station_text):
		user = self.user_list.get_user(user_id)

		candidates = self.persistance.get_station_candidates(station_text)

		output_message = u''
		if len(candidates) == 0:
			output_message = self.message_builder.get_message_by_id(MESSAGE.STATION.WRONG, user.language, station_text)
		elif len(candidates) == 1:
			output_message = self.message_builder.get_message_by_id(MESSAGE.STATION.OK, user.language, candidates[0][1])
			if user.current_button == BUTTON.ID.ORIGIN:
				user.origin = candidates[0][1]
				user.origin_id = candidates[0][0]
			elif user.current_button == BUTTON.ID.DESTINY:
				user.destiny = candidates[0][1]
				user.destiny_id = candidates[0][0]
			user.current_button = None
			self.user_list.save_users()
		else:
			output_message = self.message_builder.get_retry_message(MESSAGE.STATION.RETRY, candidates, user.language) 

		buttons_list = self.message_builder.get_buttons_text_list(user.origin, user.destiny, user.language, user.time, user.date)
		
		return output_message, buttons_list

	def set_language(self, user_id, language_text):
		user = self.user_list.get_user(user_id)

		candidates = self.persistance.get_language_candidates(language_text)

		output_message = u''
		if len(candidates) == 0:
			output_message = self.message_builder.get_message_by_id(MESSAGE.LANGUAGE.WRONG, user.language, language_text)
		elif len(candidates) == 1:
			user.language = candidates[0][0]
			output_message = self.message_builder.get_message_by_id(MESSAGE.LANGUAGE.OK, user.language, candidates[0][1])
			user.current_button = None
			self.user_list.save_users()
		else:
			output_message = self.message_builder.get_retry_message(MESSAGE.LANGUAGE.RETRY, candidates, user.language) 

		buttons_list = self.message_builder.get_buttons_text_list(user.origin, user.destiny, user.language, user.time, user.date)
		
		return output_message, buttons_list

	def set_time(self, user_id, time_text):
		user = self.user_list.get_user(user_id)

		output_message = u''
		time_list = re.findall(r"[0-9]+", time_text)
		#TO DO: move messages to message_builder
		if len(time_list) == 1:
			user.time = ('0' + unicode(int(time_list[0])%24))[-2:] + u':00'
			output_message = self.message_builder.get_message_by_id(MESSAGE.TIME.OK, user.language)
		elif len(time_list) == 2:
			user.time = ('0' + unicode(int(time_list[0])%24))[-2:] + u':' + ('0' + unicode(int(time_list[1])%60))[-2:]
			output_message = self.message_builder.get_message_by_id(MESSAGE.TIME.OK, user.language)
			self.user_list.save_users()
		else:
			output_message = self.message_builder.get_message_by_id(MESSAGE.TIME.WRONG, user.language)
		
		buttons_list = self.message_builder.get_buttons_text_list(user.origin, user.destiny, user.language, user.time, user.date)
		return output_message, buttons_list

	def set_date(self, user_id, date_text):
		user = self.user_list.get_user(user_id)
		date_list = re.findall(r"[0-9]+", date_text)

		if len(date_list) == 1:
			date_text = date_list[0] + datetime.now().strftime('/%m/%Y')
		elif len(date_list) == 2:
			date_text = date_list[0] + date_list[1] + datetime.now().strftime('/%Y')
		elif len(date_list) == 3:
			date_text = '/'.join(date_list)

		#TO DO: move messages to message_builder

		output_message = u''
		try:
			datetime.strptime(date_text, '%d/%m/%Y')
			user.date = date_text
			output_message = self.message_builder.get_message_by_id(MESSAGE.DATE.OK, user.language)
			self.user_list.save_users()
		except ValueError:
			output_message = self.message_builder.get_message_by_id(MESSAGE.DATE.WRONG, user.language)
		
		buttons_list = self.message_builder.get_buttons_text_list(user.origin, user.destiny, user.language, user.time, user.date)
		return output_message, buttons_list

	def is_current_button(self, user_id, button_id):
		user = self.user_list.get_user(user_id)
		return user.current_button == button_id

if __name__ == '__main__':
	c = Core()
	print c.start_chat("aaaa")
