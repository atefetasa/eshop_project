from django.contrib import admin
from . import models


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'is_active', 'parent']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'auther']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        # the following line means that the obj.ather attribute will be set
        # when you create the article for the first time
        if not change:
            obj.auther = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)

# Register your models here.
