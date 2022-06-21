from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    list_display = ('author', 'title', 'status')
