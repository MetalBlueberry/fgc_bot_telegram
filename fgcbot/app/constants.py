#MESSAGES
class Meta_Constant_Messages(type):
	@property
	def WELCOME(cls):
		return cls._welcome
	@property
	def MODIFY(cls):
		return cls._modify

class Meta_Constant_Set(type):
	@property
	def OK(cls):
		return cls._ok
	@property
	def RETRY(cls):
		return cls._retry
	@property
	def WRONG(cls):
		return cls._wrong

class Meta_Constant_Trip(type):
	@property
	def EMPTY(cls):
		return cls._empty
	@property
	def SAME(cls):
		return cls._same	
	@property
	def LINE(cls):
		return cls._line

class Meta_Constant_Ok_Wrong(type):
	@property
	def OK(cls):
		return cls._ok
	@property
	def WRONG(cls):
		return cls._wrong

class Meta_Constant_Schedule(type):
	@property
	def STATIONS(cls):
		return cls._stations
	@property
	def HOURES(cls):
		return cls._houres
	@property
	def TRANSFER(cls):
		return cls._transfer

class MESSAGE(object):
	__metaclass__ = Meta_Constant_Messages
	_welcome = 0
	_modify = 1
	class STATION(object):
		__metaclass__ = Meta_Constant_Set
		_ok = 2
		_retry = 3
		_wrong = 4
	class TRIP(object):
		__metaclass__ = Meta_Constant_Trip
		_empty = 5
		_same = 6
		_line = 7
	class LANGUAGE (object):
		__metaclass__ = Meta_Constant_Set
		_ok = 8
		_retry = 9
		_wrong = 10
	class TIME(object):
		__metaclass__ = Meta_Constant_Ok_Wrong
		_ok = 11
		_wrong = 12
	class DATE(object):
		__metaclass__ = Meta_Constant_Ok_Wrong
		_ok = 13
		_wrong = 14
	class SCHEDULE(object):
		__metaclass__ = Meta_Constant_Schedule
		_stations = 15
		_houres = 16
		_transfer = 17

#Default Configs
class Meta_Constant_Defaults(type):
	@property
	def LANGUAGE(cls):
		return cls._language

class DEFAULT(object):
	__metaclass__ = Meta_Constant_Defaults
	_language = 2

#Buttons
class Meta_Constant_Buttons_id(type):
	@property
	def ORIGIN(cls):
		return cls._origin
	@property
	def DESTINY(cls):
		return cls._destiny
	@property
	def GO(cls):
		return cls._go
	@property
	def LANGUAGE(cls):
		return cls._language
	@property
	def TIME(cls):
		return cls._time
	@property
	def DATE(cls):
		return cls._date
	@property
	def HELP(cls):
		return cls._help

class Meta_Constant_Buttons_icons(type):
	@property
	def ORIGIN(cls):
		return cls._origin
	@property
	def DESTINY(cls):
		return cls._destiny
	@property
	def GO(cls):
		return cls._go
	@property
	def LANGUAGE(cls):
		return cls._language
	@property
	def TIME(cls):
		return cls._time
	@property
	def DATE(cls):
		return cls._date
	@property
	def HELP(cls):
		return cls._help

class BUTTON(object):
	class ID(object):
		__metaclass__ = Meta_Constant_Buttons_id
		_origin = 0
		_destiny = 1
		_go = 2
		_language = 3
		_time = 4
		_date = 5
		_help = 6
	class ICON(object):
		__metaclass__ = Meta_Constant_Buttons_icons
		_origin = u'\U0001F6A9'
		_destiny = u'\U0001F3C1'
		_go = u'\U0001F3C3 \U0001F687'
		_language = u'\U00002699'
		_time = u'\U0001F552'
		_date = u'\U0001F5D3'
		_help = u'\U00002753'
