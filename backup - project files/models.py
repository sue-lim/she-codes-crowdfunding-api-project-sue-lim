from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.conf import settings

User = get_user_model()

'''Projects Model'''


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    # # liked_by = models.ManyToManyField(
    # #     User, blank=True, null=True,
    # #     related_name='liked_projects'
    # )
    # @property & annotations
    # insert this to count the sum the amount of pledges to calculate

    @property
    def sum_pledges(self):
        pledge_sum = self.pledges.aggregate(sum=models.Sum("amount"))["sum"]
        if pledge_sum == None:
            return 0
        else:
            return pledge_sum

    @property
    def goal_balance(self):
        return self.goal - self.sum_pledges

    # code to return title name in the drop down
    def __str__(self):
        return self.title


'''Comments Model'''


class Comment(models.Model):

    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    project = models.ForeignKey(
        'Project',  on_delete=models.CASCADE, related_name='comments')
    commentator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commentator_comment')


'''Pledge Model'''


class Pledge(models.Model):
    date_pledged = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    comment = models.TextField()
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='pledges')
    supporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='supporter_pledges')


'''Category Model'''


class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


'''Favourites Model 
***TO BE IMPLEMENTED*** '''


class Favourite(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner_favourites',)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='projects_favourites')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'project')
