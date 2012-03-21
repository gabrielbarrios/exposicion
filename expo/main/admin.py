from django.contrib import admin
from main.models import Student, Pet


class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'number')

class PetAdmin(admin.ModelAdmin):
	list_display = ('name', 'decription',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Pet, PetAdmin)
