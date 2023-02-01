from django.contrib import admin
from .models import Book, Publisher, Contributor, BookContributor, Review

@admin.register(Review)
class AdminRegister(admin.ModelAdmin):
    list_display = ('book', 'content', 'rating', 'date_created', 'date_edited', 'creator')
    list_filter = ('content', 'rating', 'date_created')
    search_fields = ('content', 'book')



admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(BookContributor)

