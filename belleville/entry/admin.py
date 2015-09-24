from django.contrib import admin

from .models import Post, Category, PostCategory

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('title', 'publish', 'created_at',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        PostCategoryInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
