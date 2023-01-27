from django.contrib import admin
from .import models
# Register your models here.


class Projects(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_created', 'owner', 'liked_by')
    list_filter = ['author', 'title', 'date_created', 'owner', 'liked_by']
    # search = ['title', 'content']
    # actions = ['edit']


class Pledges(admin.ModelAdmin):
    list_display = ('supporter', 'comment', 'project')
    list_filter = ['supporter', 'comment', 'project']


class Comments(admin.ModelAdmin):
    list_display = ('comments', 'title')
    list_filter = ('comments', 'title')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(models.Project)
admin.site.register(models.Pledge)
admin.site.register(models.Comment)
