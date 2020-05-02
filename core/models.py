from django.db import models
from django.urls import reverse


class Run(models.Model):
    code = models.TextField()

    def get_absolute_url(self):
        return reverse('run', kwargs={'pk': self.pk})

class Job(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    python_version = models.CharField(max_length=255)
    output = models.TextField()