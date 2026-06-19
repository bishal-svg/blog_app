from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=44)
    description=models.TextField(max_length=555)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(blank=True)

    def __str__(self):
        return self.title

   