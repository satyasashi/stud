from django import template
from django.shortcuts import render
from django.http import HttpResponse
# Import models.py
from .models import Student
# Import forms.py
from .forms import StudentForm

# Create your views here.

def student_list(request):
	students = Student.objects.all()
	context = {'students': students}
	return render(request, 'people/welcome.html', context)

def student_detail(request, id):
	student = Student.objects.get(id=id)
	context = {'student': student,}
	return render(request, 'people/student_detail.html', context)


def student_create(request):
	form = StudentForm(request.POST or None)
	errors = None

	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/login/')

	if form.errors:
		errors = form.errors

	context = {'form': form, 'errors': errors}
	return render(request, 'people/form.html', context)