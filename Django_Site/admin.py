from django.contrib import admin
from .models import Author, CrosswordBase


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('nickname', 'surname')
    fields = ['nickname', ('name', 'surname', 'patronymic')]


@admin.register(CrosswordBase)
class CrosswordBaseAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Info', {
            'fields': (('author', 'name'), )
        }),
        ('File Info', {
            'fields': ('comment', 'file')
        })
    )
