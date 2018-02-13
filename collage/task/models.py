from django.db import models


class Task(models.Model):
	client = models.ForeignKey(
		'client.Client',
		on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	assignees = models.ManyToManyField('account.Account')
	tags = models.ManyToManyField('task.TaskTag')

	@property
	def needs_assignment(self):
		return not self.assignees.all().count() 

	@property
	def is_urgent(self):
		return "Urgent" in [tag.name for tag in self.tags.all()]


class TaskTag(models.Model):
	name = models.CharField(max_length=100)
