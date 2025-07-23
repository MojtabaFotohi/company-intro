from django.contrib import admin
from .models import Project, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'categories')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    filter_horizontal = ('categories',)
    fields = ('title', 'description', 'image', 'categories', 'is_published')