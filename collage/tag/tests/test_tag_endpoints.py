from django.test import TestCase
from django.test import Client as RequestClient
from model_mommy import mommy

from tag.models import Tag


class TestClientEndpoints(TestCase):
	def setUp(self):
		self.client = RequestClient()

		mommy.make(Tag,	name="Meeting")
		mommy.make(Tag, name="Coffee")

	def tearDown(self):
		Tag.objects.all().delete()

	def test_tag_endpoint_returns_correct_data_and_is_200(self):
		response = self.client.get('/tags/')
		tags = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(tags), 2)
		expected_keys = ['id', 'name']
		self.assertEqual(
			list(tags[0].keys()),
			expected_keys)
