from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title, self.text)
