from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Candidate"
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"
    
    class Meta:
        verbose_name_plural = "Vote"