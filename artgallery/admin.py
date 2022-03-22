from django.contrib import admin

from .models import  Colour, Cross, Doodle, Graphite

# Register your models here.
admin.site.register(Graphite)
admin.site.register(Colour)
admin.site.register(Doodle)
admin.site.register(Cross)