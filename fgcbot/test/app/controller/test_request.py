# -*- coding: utf-8 -*-
import unittest
from mock import MagicMock
from mock import patch

from ....app.controller.request import Request

class Test_Request (unittest.TestCase):
	def test_Request_simple_init(self):
		#Arrange#
		req = Request()

		#Action

		#Assert#
		self.assertEqual(req.fgc_base_url, 'https://www.fgc.cat/cercador/cerca.asp?')

	def test_Request_get_url(self):
		#Arrange#
		req = Request()
		expected_url = 'https://www.fgc.cat/cercador/cerca.asp?liniasel=1&estacio_origen=origin&estacio_desti=destiny&tipus=S&dia=10%2F10%2F2000&horas=16&minutos=20'
		#Action
		url = req.get_url('1', 'origin', 'destiny', '16:20', '10/10/2000')

		#Assert#
		self.assertEqual(url, expected_url)

	@patch('fgcbot.app.controller.request'+'.requests')
	def test_Request_send_data(self, req_patch):
		#Arrange#
		mock_data = MagicMock()
		mock_data.json.return_value = [[{'Key':'value'}]]
		req = Request()
		url = 'https://www.fgc.cat'
		req_patch.post.return_value = mock_data

		#Action
		response = req.send_data(url)

		#Assert#
		req_patch.post.assert_called_once_with(url)
		self.assertEqual(response, {'Key':'value'})

if __name__ == '__main__':
	unittest.main()
