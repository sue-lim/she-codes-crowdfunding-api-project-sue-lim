from django.contrib import admin


from .import models
# Register your models here.


class Projects(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'goal', 'is_open', 'date_created')


class Pledges(admin.ModelAdmin):
    list_display = ('supporter', 'comment', 'project', 'amount')


class Comments(admin.ModelAdmin):
    list_display = ('comment', 'comment_author_projects')


admin.site.register(models.Project)
admin.site.register(models.Pledge)
admin.site.register(models.Comment)

admin.site.register(models.Category)
admin.site.register(models.Favourite)
