# -*- coding: utf-8 -*-
import sqlite3, os
from datetime import datetime

class Logger (object):
	def __init__(self):
		dirname = os.path.dirname
		database_path = os.path.join(dirname(dirname(dirname(__file__))), 'data', 'Requests.db')
		self.database = sqlite3.connect(database_path,check_same_thread=False)
		self.read_all = u'SELECT rowid, * FROM Requests ORDER BY timestamp'
		self.insert = u"INSERT INTO Requests VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"
		self.cursor = self.database.cursor()
		try:
			self.cursor.execute("""CREATE TABLE Requests (timestamp, user_id, origin, destiny, time, date) 
				""")
		except Exception as error:
			pass
	def write_entry(self, user_id, origin, destiny, time = None, date = None):
		try:
			timestamp = datetime.now()
			if time == None:
				time = datetime.now().strftime('%H:%M')
			if date == None:
				date = datetime.now().strftime('%d/%m/%Y')
			#print self.insert.format(timestamp,user_id,origin,destiny,time,date)
			self.cursor.execute(self.insert.format(timestamp,user_id,origin,destiny,time,date))
			self.database.commit()
		except Exception as error:
			print "Error when logging the message"
			print error
		
	def get_last_entries(self, number_of_rows=10):
		try:
			rows = self.cursor.execute(self.read_all)
			if len(rows) < number_of_rows:
				number_of_rows = len(rows)
			output_message = u""
			for row in rows:
				output_message +=  rows + u"\n"
			return output_message
		except Exception as error:
			print "Error when reading the DB"
			print error