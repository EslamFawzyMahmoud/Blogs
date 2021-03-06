from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# title -user -image-body-Created-content

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='post_img/',default='post_img/defualt.png')
    content=models.TextField(default=' ')
    created=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title