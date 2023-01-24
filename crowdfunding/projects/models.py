from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    liked_by = models.ManyToManyField(
        User,
        related_name='liked_projects'
    )
    # @property & annotations
    # insert this to count the sum the amount of pledges to calculate

    @property
    def total(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
