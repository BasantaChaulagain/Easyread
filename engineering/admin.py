from django.contrib import admin
from .models import Faculty, Subject, Matchtable, Book

class MatchTableAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'semester', 'faculty')
    list_filter = ['semester']
    search_fields = ['subject']
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'matchtable')
    list_filter = ['price']
    search_fields = ['title']
    
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Matchtable, MatchTableAdmin)
admin.site.register(Book, BookAdmin)