from django.contrib import admin

from .models import Address, Author, Book, Country


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    list_filter = ("name", "code")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country, CountryAdmin)
