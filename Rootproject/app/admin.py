from django.contrib import admin

# from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'enrollment_date')
    search_fields = ('name', 'email')
    list_filter = ('enrollment_date',)