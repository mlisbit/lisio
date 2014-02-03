from django.db import models
from django.contrib.auth.models import User
from time import time
from datetime import datetime
import django.utils.timezone


def get_upload_file_name(instance, filename):
	return "/project_imgs/%s_%s" % (str(time()).replace('.','_'), filename)


class Language(models.Model):
	name = models.CharField(max_length=200)

class Link(models.Model):
	label = models.CharField(max_length=200)
	location = models.CharField(max_length=400)

class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	event_img = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
	languages = models.ManyToManyField(Language, blank=True, null=True)
	links = models.ManyToManyField(Link, blank=True, null=True)
	#determines how close to the top you want this project
	priority = models.IntegerField(max_length=5, null=True, blank=True)

	def __unicode__(self):
		return self.name
