from django.contrib import admin

#superuser: username-admin, pw=polladmin2021

# Register your models here.
from .models import Question,Choice

#admin.site.register(Question)

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text','pub_date','was_published_recently')

admin.site.register(Question,QuestionAdmin)

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

admin.site.register(Choice)

