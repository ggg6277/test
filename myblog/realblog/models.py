from django.db import models

# Create your models here.

class Contents(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField(max_length=300, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    contents = models.ForeignKey('Contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.author

