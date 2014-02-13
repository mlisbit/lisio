from django.db import models

class Statement(models.Model):
	text = models.CharField(max_length=600)

	def __unicode__(self):
		return self.text