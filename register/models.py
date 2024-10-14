from django.db import models

# Create your models here.
class Participants(models.Model):
    name = models.CharField(max_length=50)
    form_number = models.BigIntegerField(unique=True)
    email = models.EmailField()
    score = models.IntegerField(default=0)
    def update_total_score(self):
        # Calculate the sum of all submission scores for this participant
        total_score = self.submission_set.aggregate(total=models.Sum('score'))['total'] or 0
        self.score = total_score
        self.save()  # Save the updated score
    def __str__(self):
        return self.name
