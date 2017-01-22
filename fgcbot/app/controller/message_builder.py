# -*- coding: utf-8 -*-
from datetime import datetime
from ..constants import *
from ..model.languages import Languages

class Message_Builder (object):
	def __init__(self):
 		self.languages = Languages()

	def get_message_by_id(self, message_id, language = None, text = u''):
		if language == None:
			language = DEFAULT.LANGUAGE

		return self.languages.messages[message_id][language].format(text)

	def get_buttons_text_list(self, origin = None, destiny = None, language = None, time = None, date = None):
		if language == None:
			language = DEFAULT.LANGUAGE

		lang = self.languages.buttons_text[BUTTON.ID.LANGUAGE][language]
		if not origin:
			origin = self.languages.buttons_text[BUTTON.ID.ORIGIN][language]
		if not destiny:
			destiny = self.languages.buttons_text[BUTTON.ID.DESTINY][language]
		if not time:
			time = datetime.now().strftime('%H:%M')
		if not date:
			date = datetime.now().strftime('%d/%m/%Y')

		go = self.languages.buttons_text[BUTTON.ID.GO][language]

		buttons_text_list = [origin, destiny, go, lang, time, date]
		buttons_icon_list = [BUTTON.ICON.ORIGIN, BUTTON.ICON.DESTINY, BUTTON.ICON.GO, BUTTON.ICON.LANGUAGE, BUTTON.ICON.TIME, BUTTON.ICON.DATE]

		return [icon + u' ' + text for icon, text in zip(buttons_icon_list, buttons_text_list)]

	def get_modify_button_message(self, button_id, language = None):
		if language == None:
			language = DEFAULT.LANGUAGE
		return self.languages.messages[MESSAGE.MODIFY][language].format(self.languages.buttons_text[button_id][language])

	def get_retry_message(self, message_id, text_list, language = None):
		if language == None:
			language = DEFAULT.LANGUAGE
		return self.languages.messages[message_id][language].format(', '.join(zip(*text_list)[1]))	

	def get_trip_schedule_message(self, origin_station, destiny_station, trip_data, language = None):
		if language == None:
			language = DEFAULT.LANGUAGE

		#TO DO: Move sentences to languages file and make nice the response
		output_message = self.languages.messages[MESSAGE.SCHEDULE.STATIONS][language].format(origin_station, destiny_station)
		for trip in trip_data:
			output_message += self.languages.messages[MESSAGE.SCHEDULE.HOURES][language].format(trip['origin']['time'], trip['destiny']['time'])
			
		if len(trip_data) > 0:
			if trip_data[0]['transfer']:
				output_message += self.languages.messages[MESSAGE.SCHEDULE.TRANSFER][language].format(', '.join(trip_data[0]['transfer']))
		return output_message
