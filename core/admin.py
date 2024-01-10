from django.contrib import admin
from core.models import UserModel, ContactModel, AboutModel, BlogModel, CommentModel, CategoryModel

# Register your models here.

class BlogModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register([UserModel, ContactModel, AboutModel, CommentModel, CategoryModel])