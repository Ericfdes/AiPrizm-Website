from django.contrib import admin
from .models import Blog, Author, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}




# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Category)