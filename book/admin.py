from django.contrib import admin
from . models import Book, Review 

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','description','author','book_cover')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','stars','comment','review_date')


admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
