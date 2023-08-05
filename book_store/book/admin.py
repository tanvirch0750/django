from django.contrib import admin

from . import models

# Register your models here.
# admin.site.register(models.BookStoreModel)

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category', 'first_pub', 'last_pub')
    
admin.site.register(models.BookStoreModel, BookStoreModelAdmin)


