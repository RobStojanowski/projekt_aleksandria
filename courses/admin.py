from django.contrib import admin
from .models import  Course, Enrollment, Review

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'start_data', 'end_data']

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)
admin.site.register(Review)
