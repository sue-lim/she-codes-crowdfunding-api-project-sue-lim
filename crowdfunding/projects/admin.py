
from django.contrib import admin


from .import models
# Register your models here.


class Projects(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_created', 'owner', 'liked_by')
    ordering = ['author', 'title', 'date_created', 'owner', 'liked_by']
    # search = ['title', 'content']
    # actions = ['edit']


class Pledges(admin.ModelAdmin):
    list_display = ('supporter', 'comment', 'project')
    ordering = ['supporter', 'comment', 'project']


class Comments(admin.ModelAdmin):
    list_display = ('comment', 'comment_author_projects')
    ordering = ('comment', 'comment_author_projects')


admin.site.register(models.Project)
admin.site.register(models.Pledge)
admin.site.register(models.Comment)

admin.site.register(models.Category)
admin.site.register(models.Favourite)
