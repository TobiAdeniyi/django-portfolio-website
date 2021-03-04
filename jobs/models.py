from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    github_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
