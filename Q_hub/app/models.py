from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SubjectCode(models.Model):
	name = models.CharField(max_length=32, unique=True)
	code = models.CharField(max_length=32, unique=True)


class QuestionDetail(models.Model):
	owner = models.ForeignKey(User)
	date_created = models.DateTimeField(auto_now_add=True)
	question = models.TextField()
	marks = models.IntegerField()
	unit = models.IntegerField()
	n_used = models.IntegerField()
	imp = models.BooleanField(default=False)

	