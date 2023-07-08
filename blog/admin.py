from .models import Categoria, Post
from django.contrib import admin

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

# Register your models here.
