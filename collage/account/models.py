from django.db import models

class Account(models.Model):
	name = models.CharField(max_length=250)
	tag = models.ForeignKey(
		'tag.Tag',
		null=True,
		blank=True,
		on_delete=models.CASCADE)

	@property
	def initials(self):
		return "".join(
			[
				word[0].upper()
				for word in self.name.split()
			])
