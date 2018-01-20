from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Student(models.Model):
	owner		=	models.ForeignKey(User)
	name		=	models.CharField(max_length=100)
	location	=	models.CharField(max_length=150, blank=True)
	timestamp   =   models.DateTimeField(auto_now_add=True)
	updated     =   models.DateTimeField(auto_now=True)
	eduChoices	=	(
		('Masters', 'MASTERS'),
		('Bachelors', 'BACHELORS'),
		('Engineering', 'ENGINEERING'),
		('Intermediate', 'INTERMEDIATE'),
		('SSC', 'SSC'),
		)
	studied		=	models.CharField(max_length=200, choices=eduChoices)
	stream		= 	models.CharField(max_length=150, blank=False, default='Computers')
	college		=	models.CharField(max_length=250, default='college')
	marks		=	models.IntegerField()

	def __str__(self):
		return self.name