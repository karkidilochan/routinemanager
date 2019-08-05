from django.contrib import admin
from .models import Departments, Programs, Teachers, Rooms, Subjects

# Register your models here.
admin.site.register(Departments)
admin.site.register(Programs)
admin.site.register(Teachers)
admin.site.register(Rooms)
admin.site.register(Subjects)
