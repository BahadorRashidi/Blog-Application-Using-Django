from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length = 100) # This is simply sets the length 
    content = models.TextField() # This is letting the text to be unlimitted
    date_posted = models.DateTimeField(default = timezone.now) # this is for taking the cuurent time for the post time
    author = models.ForeignKey(User, on_delete = models.CASCADE) # This is setting the foreig key for the author to be oneof the users


    def __str__(self):
        return self.title










