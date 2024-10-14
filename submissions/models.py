from django.db import models
from register.models import Participants  # Import the Participant model

class Submission(models.Model):
    participant = models.ForeignKey(Participants, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    githuburl = models.URLField()
    problemStatement = models.TextField()
    score = models.IntegerField(default=0)  # New field to store submission score

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the submission first
        self.participant.update_total_score() 

    def __str__(self):
        return f'Submission by {self.participant}({self.participant.form_number})'
    
class SiteSetting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.BooleanField(default=True)  # Store boolean value

    def __str__(self):
        return f"{self.key}: {self.value}"
