from django.db import models

# Create your models here.
class Voter(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True,blank=False)
    email = models.CharField(max_length=100,null=False,unique=True,blank=False)
    has_voted = models.BooleanField(default=False)

    class Meta:
        db_table = "Voter"

class Candidate(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True,blank=False)
    party = models.CharField(max_length=100,null=True)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = "Candidate"

class Vote(models.Model):
    voter_id = models.ForeignKey(Voter,on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    class Meta:
        db_table = "Vote"