from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=65)
    content = models.TextField(max_length=255, null=True, blank=True)
    content_image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        if not (self.content or self.content_image):
            raise ValidationError("We need something here")