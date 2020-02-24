from django.db import models


class UpPost(models.Model):
    topic = models.CharField(max_length=400)
    content = models.CharField(max_length=2000)
    startdate = models.DateField()
    starttime = models.DateTimeField(auto_now_add=True)
    endtime =  models.DateTimeField(auto_now_add=True)
    startaddress = models.CharField(max_length = 200)
    endaddress = models.CharField(max_length = 200)
    coachbox = models.IntegerField()
    transposts= models.CharField(max_length = 300)
    image = models.ImageField(upload_to='stactic/image')