from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=100)
	client = models.ForeignKey(
		'client.Client',
		on_delete=models.CASCADE)
	member = models.ManyToManyField('account.Account')
