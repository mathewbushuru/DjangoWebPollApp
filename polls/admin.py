from django.contrib import admin

#superuser: username-admin, pw=polladmin2021

# Register your models here.
from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)

