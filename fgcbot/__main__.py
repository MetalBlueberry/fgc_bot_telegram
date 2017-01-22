# -*- coding: utf-8 -*-
import telebot
from telebot import types

from config import *
from app.controller.core import Core
from app.constants import BUTTON

fgc_bot = telebot.TeleBot(TOKEN)
core = Core()

#command received#
@fgc_bot.message_handler(commands=['start'])
def command_start(input_message):
	output_message, buttons_list = core.start_chat(input_message.from_user.id)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")
	#TO DO: Return gif with instructions

@fgc_bot.message_handler(commands=['fgc'])
def command_fgc(message):
	fgc_bot.send_message(message.chat.id, "command fgc")	

#button pressed#
@fgc_bot.message_handler(func=lambda input_message: input_message.text.startswith(BUTTON.ICON.ORIGIN) )
def button_origin(input_message):
	output_message = core.press_modifiable_button(input_message.from_user.id, BUTTON.ID.ORIGIN)
	markup = types.ForceReply()
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup,  parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: input_message.text.startswith(BUTTON.ICON.DESTINY) )
def button_destiny(input_message):
	output_message = core.press_modifiable_button(input_message.from_user.id, BUTTON.ID.DESTINY)
	markup = types.ForceReply()
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup,  parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: input_message.text.startswith(BUTTON.ICON.GO) )
def button_go(input_message):
	output_message, buttons_list = core.press_go_button(input_message.from_user.id)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: input_message.text.startswith(BUTTON.ICON.LANGUAGE) )
def button_language(input_message):
	output_message = core.press_modifiable_button(input_message.from_user.id, BUTTON.ID.LANGUAGE)
	markup = types.ForceReply()
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup,  parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: input_message.text.startswith(BUTTON.ICON.TIME) )
def button_time(input_message):
	output_message = core.press_modifiable_button(input_message.from_user.id, BUTTON.ID.TIME)
	markup = types.ForceReply()
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup,  parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: input_message.text.startswith(BUTTON.ICON.DATE) )
def button_date(input_message):
	output_message = core.press_modifiable_button(input_message.from_user.id, BUTTON.ID.DATE)
	markup = types.ForceReply()
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup,  parse_mode="HTML")

#text received#
@fgc_bot.message_handler(func=lambda input_message: core.is_current_button(input_message.from_user.id, BUTTON.ID.ORIGIN))
def text_origin(input_message):
	output_message, buttons_list = core.set_station(input_message.from_user.id, input_message.text)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: core.is_current_button(input_message.from_user.id, BUTTON.ID.DESTINY))
def text_destiny(input_message):
	output_message, buttons_list = core.set_station(input_message.from_user.id, input_message.text)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: core.is_current_button(input_message.from_user.id, BUTTON.ID.LANGUAGE))
def text_language(input_message):
	output_message, buttons_list = core.set_language(input_message.from_user.id, input_message.text)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: core.is_current_button(input_message.from_user.id, BUTTON.ID.TIME))
def text_time(input_message):
	output_message, buttons_list = core.set_time(input_message.from_user.id, input_message.text)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")

@fgc_bot.message_handler(func=lambda input_message: core.is_current_button(input_message.from_user.id, BUTTON.ID.DATE))
def text_time(input_message):
	output_message, buttons_list = core.set_date(input_message.from_user.id, input_message.text)
	markup = create_buttons_markup(buttons_list)
	fgc_bot.send_message(input_message.chat.id, output_message, reply_markup=markup, parse_mode="HTML")


#any#



#support functions#

def create_buttons_markup (buttons_text_list):
	markup = types.ReplyKeyboardMarkup()
	btn_origin = types.KeyboardButton(buttons_text_list[0])
	btn_destiny = types.KeyboardButton(buttons_text_list[1])
	btn_go = types.KeyboardButton(buttons_text_list[2])
	btn_language = types.KeyboardButton(buttons_text_list[3])
	btn_time = types.KeyboardButton(buttons_text_list[4])
	btn_day = types.KeyboardButton(buttons_text_list[5])
	#btn_help = types.KeyboardButton(buttons_text_list[6])
	markup.row(btn_origin, btn_destiny)
	markup.row(btn_go)
	markup.row(btn_language, btn_time, btn_day)
	return markup

fgc_bot.polling(none_stop=True, timeout=100)