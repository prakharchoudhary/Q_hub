from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class SubjectCode(models.Model):
	name = models.CharField(max_length=32, unique=True)
	code = models.CharField(max_length=32, unique=True)


class QuestionDetail(models.Model):
	owner = models.ForeignKey(User)
	date_created = models.DateTimeField(auto_now_add=True)
	branch = models.CharField(max_length=40, null=True)
	question = RichTextField()
	subject = models.ForeignKey(SubjectCode, null=True)
	marks = models.IntegerField()
	unit = models.IntegerField()
	n_used = models.IntegerField(default=0)
	co = models.IntegerField(default=1)
	imp = models.BooleanField(default=False)

class Filter(models.Model):
	CSE = 'CSE'
	IT = 'IT'
	EE = 'EE'
	ECE = 'ECE'
	EEE = 'EEE'
	CE = 'CE'
	IC = 'IC'
	ME = 'ME'
	N = 'Select Branch'

	BRANCH = (
		(CSE, 'Computer Science'),
		(IT, 'Information Technology'),
		(EE, 'Electrical Engineering'),
		(EEE, 'Electrical and Electronics Engineering'),
		(ME, 'Mechanical Engineering'),
		(ECE, 'Electronics and Communication'),
		(IC, 'Instrumentation and Control'),
		(CE, 'Civil Engineering'),
		(N, 'Select Branch')
	)

	FIRST = '1'
	SECOND = '2'
	THIRD = '3'
	FOURTH = '4'
	M = 'Select Year'
	ALL = 'ALL'
	YEAR = (
		(FIRST, '1'),
		(SECOND, '2'),
		(THIRD, '3'),
		(FOURTH, '4'),
		(ALL, 'ALL'),
		(M, 'Select Year')
	)

	DSGT = 'DSGT'
	DS = 'DS'
	MATHS3 = 'MATHS3'
	CBNST = 'CBNST'
	OS = 'OS'
	MUL = 'MUL'
	TOFL = 'TOFL'
	O = 'Select Subject'
	SUBJECT = (
		(DSGT, 'DSGT'),
		(DS, 'DS'),
		(MATHS3, 'MATHS3'),
		(CBNST, 'CBNST'),
		(OS, 'OS'),
		(MUL, 'MUL'),
		(TOFL, 'TOFL'),
		(O, 'Select Subject')
	)

	branch = models.CharField(max_length = 20, choices = BRANCH, default = N)

	year = models.CharField(max_length = 5, choices = YEAR, default = M)

	subject = models.CharField(max_length = 12, choices = SUBJECT, default = O)


class ActiveSession(models.Model):

	user = models.ForeignKey(User)
	branch = models.CharField(max_length = 20)
	year = models.CharField(max_length = 5)
	subject = models.CharField(max_length = 12)