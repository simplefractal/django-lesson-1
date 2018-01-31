from django.test import TestCase
from django.test import Client as RequestClient
from model_mommy import mommy

from client.models import Client


class TestClientEndpoints(TestCase):
	def setUp(self):
		self.client = RequestClient()

		mommy.make(
			Client,
			name="Mosaic",
			email="mosaic@lifecoded.com",
			industry="Productivity")

		mommy.make(
			Client,
			name="Heidrick",
			email="heidrick@heidrick.com",
			industry="Consulting")


	def tearDown(self):
		Client.objects.all().delete()

	def test_client_endpoint_returns_correct_data_and_is_200(self):
		response = self.client.get('/clients/')
		clients = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(clients), 2)
		expected_keys = ['id', 'name', 'email', 'industry', 'code', 'industry_code']
		self.assertEqual(
			list(clients[0].keys()),
			expected_keys)
