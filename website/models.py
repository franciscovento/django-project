from django.db import models

# Create your models here.



class Member(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  document = models.CharField(max_length=200)

class Conventions(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)

class Profile(models.Model):
  document = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  full_name = models.CharField(max_length=200)

class Vote(models.Model): 
  name = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  convention = models.ForeignKey(Conventions, on_delete=models.CASCADE)
  voted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)