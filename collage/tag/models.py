from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=250, null=True, blank=True)
	uuid = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name
