from django.test import TestCase
from django.test import Client as RequestClient
from model_mommy import mommy

from client.models import Client


class TestClientEndpoints(TestCase):
	def setUp(self):
		self.client = RequestClient()
		mommy.make(Client, _quantity=3)

	def tearDown(self):
		Client.objects.all().delete()

	def test_client_endpoint_returns_correct_data(self):
		response = self.client.get('/clients/')
		import pdb; pdb.set_trace()
		print("YO")

