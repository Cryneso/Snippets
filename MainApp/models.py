from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    public = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.lang} user:{self.user}"
    
    


class Comment(models.Model):
   text = models.TextField(max_length=1000)
   author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
   snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
