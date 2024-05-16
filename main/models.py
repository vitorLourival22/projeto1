from django.db import models

# Create your models here.
class Todo(models.Model):
    cheate_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
class item(models.Model):
     cheate_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)
     todo = models.ForeignKey(Todo, on_delete=models.CASCADE,related_name="items")
     text = models.TextField()
     complete = models.BooleanField(default=False)