from django.contrib import admin
from .models import Cpu, Disk, Gpu, Ram, Cooler, Case, PSU, MB, Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    ordering = ['pk']
    list_display = [
        'pk',
        'choice_text',
        'question'
    ]
    list_filter = [
        'question'
    ]
    list_display_links = [
        'pk',
        'choice_text'
    ]
    search_fields = [
        'pk',
        'choice_text',
        'question__question_text'
    ]

class QuestionAdmin(admin.ModelAdmin):
    ordering = ['pk']
    list_display = [
        'pk',
        'question_text',
        'tag'
    ]
    list_filter = [
        'tag'
    ]
    list_display_links = [
        'pk',
        'question_text'
    ]
    search_fields = [
        'pk',
        'question_text',
        'tag'
    ]
# Register your models here.
admin.site.register(Cpu)
admin.site.register(Disk)
admin.site.register(Gpu)
admin.site.register(Ram)
admin.site.register(Cooler)
admin.site.register(Case)
admin.site.register(PSU)
admin.site.register(MB)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)