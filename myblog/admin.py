from django.contrib import admin
from myblog.models import Post, Category

class CategorizedInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    inlines = [CategorizedInline,]
    list_display = ('title', 'text', 'author')
    fields = ('title', 'text', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

