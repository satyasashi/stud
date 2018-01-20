from django import forms
# import ValidationError if Validation fails in 'clean' method
from django.core.exceptions import ValidationError
from .models import Student

class StudentForm(forms.Form):
	name 		=	forms.CharField()
	college		=	forms.CharField()
	stream		=	forms.CharField()
	location	=	forms.CharField(required=False)
	studied		=	forms.CharField()
	marks		= 	forms.IntegerField()

	def clean_name(self):
		name 	=	self.cleaned_data['name']
		name_l	=	name.lower()

		if name_l == 'admin' or name_l == 'student':
			raise ValidationError("Student name can't be 'admin/student' ")

		return name



	def save(self):
		new_student = Student.objects.create(
			name = self.cleaned_data['name'],
			college = self.cleaned_data['college'],
			stream = self.cleaned_data['stream'],
			location = self.cleaned_data['location'],
			studied = self.cleaned_data['studied'],
			marks = self.cleaned_data['marks'],
			)
		return new_student