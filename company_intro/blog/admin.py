from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'excerpt', 'content')
    list_editable = ('is_published',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fields = ('title', 'excerpt', 'content', 'image', 'is_published')
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()