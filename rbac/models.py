from django.db import models
from django.utils import timezone
# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=11,null=True)
    email = models.CharField(max_length=32,null=True)
    card_id = models.CharField(max_length=18,null=True)
    address = models.CharField(max_length=64,null=True)
    gender_choices = ((1,'男'),(2,'女'))
    gender = models.IntegerField(choices=gender_choices,default=1)
    entry_time = models.DateTimeField(default = timezone.now)
    state_choice = ((1,'试用期'),(2,'在职'),(3,'离职'))
    state = models.IntegerField(choices=state_choice,default=2)
    roles = models.ManyToManyField(to='Role',null=True)
    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=32)
    permission = models.ManyToManyField(to='Permission')
    def __str__(self):
        return self.title


class Permission(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)

    def __str__(self):
        return self.title