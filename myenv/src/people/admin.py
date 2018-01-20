from django.contrib import admin
from . import models

# Register your models here.
# Customizing how my models are displayed in Admin
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'studied', 'stream', 'location')
	search_fields = ['name']
	ordering = ['-name']
	date_hierarchy = 'timestamp'

admin.site.register(models.Student, StudentAdmin)