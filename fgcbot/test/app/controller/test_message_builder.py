# -*- coding: utf-8 -*-
import unittest
from mock import MagicMock
from mock import patch

from ....app.controller.message_builder import Message_Builder
from ....app.constants import *

class Test_Message_Builder(unittest.TestCase):
	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_simple_init(self, lang_patch):
		#Arrange#
		mb = Message_Builder()

		#Action

		#Assert#
		self.assertIs(mb.languages, lang_patch())

	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_get_message_by_id_with_id(self, lang_patch):
		#Arrange#
		language_mock = MagicMock()
		language_mock.messages.__getitem__.return_value = [u'Texto 1', u'Text 1', u'Text1']
		lang_patch.return_value = language_mock
		mb = Message_Builder()
		#Action
		message = mb.get_message_by_id(2)
		#Assert#
		language_mock.messages.__getitem__.assert_called_once_with(2)
		self.assertEqual(message, u'Text1')


	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_get_message_by_id_with_id_and_language(self, lang_patch):
		#Arrange#
		language_mock = MagicMock()
		language_mock.messages.__getitem__.return_value = [u'Texto 1', u'Text 1', u'Text1']
		lang_patch.return_value = language_mock
		mb = Message_Builder()

		#Action
		message = mb.get_message_by_id(2, 0)

		#Assert
		language_mock.messages.__getitem__.assert_called_once_with(2)
		self.assertEqual(message, u'Texto 1')

	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_get_message_by_id_with_id_and_language_and_text(self, lang_patch):
		#Arrange#
		language_mock = MagicMock()
		language_mock.messages.__getitem__.return_value = [u'Texto 1{0}', u'Text 1{0}', u'Text1{0}']
		lang_patch.return_value = language_mock
		mb = Message_Builder()

		#Action
		message = mb.get_message_by_id(2, 0, 'added')

		#Assert
		language_mock.messages.__getitem__.assert_called_once_with(2)
		self.assertEqual(message, u'Texto 1added')

	@patch('fgcbot.app.controller.message_builder' + '.datetime', autospec=True)
	@patch('fgcbot.app.controller.message_builder' + '.Languages')
	def test_Message_Builder_get_buttons_text_list_without_params(self, lang_patch, date_patch):
		#Arrange#
		from datetime import datetime
		date_patch.now.return_value=datetime(2010, 7, 6, 5, 27, 23)
		lang_mock = MagicMock()
		lang_mock.buttons_text.__getitem__.return_value = [u'Texto 0', u'Text 0', u'Text0']
		lang_patch.return_value = lang_mock
		mb = Message_Builder()

		#Action
		button_list = mb.get_buttons_text_list()

		#Assert#
		self.assertEqual(lang_mock.buttons_text.__getitem__.call_count, 4) 
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.LANGUAGE)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.ORIGIN)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.DESTINY)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.GO)
		self.assertEqual(date_patch.now.call_count, 2) 

		self.assertEqual(button_list[0], BUTTON.ICON.ORIGIN + u' Text0')
		self.assertEqual(button_list[1], BUTTON.ICON.DESTINY + u' Text0')
		self.assertEqual(button_list[2], BUTTON.ICON.GO + u' Text0')
		self.assertEqual(button_list[3], BUTTON.ICON.LANGUAGE + u' Text0')	
		self.assertEqual(button_list[4], BUTTON.ICON.TIME + u' 05:27')	
		self.assertEqual(button_list[5], BUTTON.ICON.DATE + u' 06/07/2010')	

	@patch('fgcbot.app.controller.message_builder' + '.datetime', autospec=True)
	@patch('fgcbot.app.controller.message_builder' + '.Languages')
	def test_Message_Builder_get_buttons_text_list_with_origin(self, lang_patch, date_patch):
		#Arrange#
		from datetime import datetime
		date_patch.now.return_value=datetime(2010, 7, 6, 5, 27, 23)
		lang_mock = MagicMock()
		lang_mock.buttons_text.__getitem__.return_value = [u'Texto 0', u'Text 0', u'Text0']
		lang_patch.return_value = lang_mock
		mb = Message_Builder()

		#Action
		button_list = mb.get_buttons_text_list('test_origin')

		#Assert#
		self.assertEqual(lang_mock.buttons_text.__getitem__.call_count, 3) 
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.LANGUAGE)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.DESTINY)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.GO)
		self.assertEqual(date_patch.now.call_count, 2) 

		self.assertEqual(button_list[0], BUTTON.ICON.ORIGIN + u' test_origin')
		self.assertEqual(button_list[1], BUTTON.ICON.DESTINY + u' Text0')
		self.assertEqual(button_list[2], BUTTON.ICON.GO + u' Text0')
		self.assertEqual(button_list[3], BUTTON.ICON.LANGUAGE + u' Text0')	
		self.assertEqual(button_list[4], BUTTON.ICON.TIME + u' 05:27')	
		self.assertEqual(button_list[5], BUTTON.ICON.DATE + u' 06/07/2010')	

	@patch('fgcbot.app.controller.message_builder' + '.datetime', autospec=True)
	@patch('fgcbot.app.controller.message_builder' + '.Languages')
	def test_Message_Builder_get_buttons_text_list_with_date(self, lang_patch, date_patch):
		#Arrange#
		from datetime import datetime
		date_patch.now.return_value=datetime(2010, 7, 6, 5, 27, 23)
		lang_mock = MagicMock()
		lang_mock.buttons_text.__getitem__.return_value = [u'Texto 0', u'Text 0', u'Text0']
		lang_patch.return_value = lang_mock
		mb = Message_Builder()

		#Action
		button_list = mb.get_buttons_text_list(date='10/02/2000')

		#Assert#
		self.assertEqual(lang_mock.buttons_text.__getitem__.call_count, 4) 
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.LANGUAGE)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.ORIGIN)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.DESTINY)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.GO)
		self.assertEqual(date_patch.now.call_count, 1) 

		self.assertEqual(button_list[0], BUTTON.ICON.ORIGIN + u' Text0')
		self.assertEqual(button_list[1], BUTTON.ICON.DESTINY + u' Text0')
		self.assertEqual(button_list[2], BUTTON.ICON.GO + u' Text0')
		self.assertEqual(button_list[3], BUTTON.ICON.LANGUAGE + u' Text0')	
		self.assertEqual(button_list[4], BUTTON.ICON.TIME + u' 05:27')	
		self.assertEqual(button_list[5], BUTTON.ICON.DATE + u' 10/02/2000')	

	@patch('fgcbot.app.controller.message_builder' + '.datetime', autospec=True)
	@patch('fgcbot.app.controller.message_builder' + '.Languages')
	def test_Message_Builder_get_buttons_text_list_with_full_params(self, lang_patch, date_patch):
		#Arrange#
		from datetime import datetime
		date_patch.now.return_value=datetime(2010, 7, 6, 5, 27, 23)
		lang_mock = MagicMock()
		lang_mock.buttons_text.__getitem__.return_value = [u'Texto 0', u'Text 0', u'Text0']
		lang_patch.return_value = lang_mock
		mb = Message_Builder()

		#Action
		button_list = mb.get_buttons_text_list('test origin', 'test destiny', 0, '09:30', '10/02/2000')

		#Assert#
		self.assertEqual(lang_mock.buttons_text.__getitem__.call_count, 2) 
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.LANGUAGE)
		lang_mock.buttons_text.__getitem__.assert_any_call(BUTTON.ID.GO)
		self.assertEqual(date_patch.now.call_count, 0) 

		self.assertEqual(button_list[0], BUTTON.ICON.ORIGIN + u' test origin')
		self.assertEqual(button_list[1], BUTTON.ICON.DESTINY + u' test destiny')
		self.assertEqual(button_list[2], BUTTON.ICON.GO + u' Texto 0')
		self.assertEqual(button_list[3], BUTTON.ICON.LANGUAGE + u' Texto 0')	
		self.assertEqual(button_list[4], BUTTON.ICON.TIME + u' 09:30')	
		self.assertEqual(button_list[5], BUTTON.ICON.DATE + u' 10/02/2000')	

	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_get_modify_button_message_with_button(self, lang_patch):
		#Arrange#
		language_mock = MagicMock()
		language_mock.messages.__getitem__.return_value = [u'Texto {0}', u'Text {0}', u'Text{0}']
		language_mock.buttons_text.__getitem__.return_value = [u'button 0', u'button 1', u'button 2']
		lang_patch.return_value = language_mock
		mb = Message_Builder()

		#Action
		message = mb.get_modify_button_message(5)

		#Assert
		language_mock.messages.__getitem__.assert_called_once_with(MESSAGE.MODIFY)
		language_mock.buttons_text.__getitem__.assert_called_once_with(5)
		self.assertEqual(message, u'Textbutton 2')

	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_get_modify_button_message_with_button_language(self, lang_patch):
		#Arrange#
		language_mock = MagicMock()
		language_mock.messages.__getitem__.return_value = [u'Texto {0}', u'Text {0}', u'Text{0}']
		language_mock.buttons_text.__getitem__.return_value = [u'button 0', u'button 1', u'button 2']
		lang_patch.return_value = language_mock
		mb = Message_Builder()

		#Action
		message = mb.get_modify_button_message(3, 0)

		#Assert
		language_mock.messages.__getitem__.assert_called_once_with(MESSAGE.MODIFY)
		language_mock.buttons_text.__getitem__.assert_called_once_with(3)
		self.assertEqual(message, u'Texto button 0')

	@patch('fgcbot.app.controller.message_builder'+'.Languages')
	def test_Message_Builder_get_retry_message_with_mandatory_params(self, lang_patch):
		#Arrange#
		language_mock = MagicMock()
		language_mock.messages.__getitem__.return_value = [u'Texto: {0}', u'Text: {0}', u'Text: {0}']
		lang_patch.return_value = language_mock
		mb = Message_Builder()
		text_list = [[0, 'item1'], [0, 'item2'], [0, 'item3']]

		#Action
		message = mb.get_retry_message(6, text_list)

		#Assert
		language_mock.messages.__getitem__.assert_called_once_with(6)
		

		self.assertEqual(message, u'Text: item1, item2, item3')

	#TO DO: unit for tunction get_trip_schedule_message

if __name__ == '__main__':
	unittest.main()
