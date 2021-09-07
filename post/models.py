from django.contrib.auth import get_user_model
from django.db import models
from django.utils import  timezone
import datetime
billingMonth2 = models.DateTimeField(default=datetime.date, null=True, blank=True)
now = timezone.now()
class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
