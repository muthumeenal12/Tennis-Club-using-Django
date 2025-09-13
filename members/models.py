from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    join_date = models.DateField(auto_now_add=True)
    age = models.IntegerField(null=False)
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)
    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email} - {self.phone} - {self.join_date}"

class JoinRequest(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)  # optional
    message = models.TextField(blank=True, default="I want to join the club.")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email} - {self.phone} - {self.message} - {self.created_at}"