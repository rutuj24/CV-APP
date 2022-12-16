from django.contrib import admin

# Register your models here.
from .models import std, resume

admin.site.register(std)
admin.site.register(resume)