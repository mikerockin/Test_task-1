from django.contrib import admin
from .models import Employe, Position, Subdivision, Department

admin.site.register(Employe)
admin.site.register(Position)
admin.site.register(Subdivision)
admin.site.register(Department)