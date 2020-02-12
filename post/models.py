from django.db import models

class UpPost(models.Model):
    post_topic = models.CharField(max_length=400)
    post_content = models.CharField(max_length=2000)
    post_startdate = models.DateField()
    post_starttime = models.DateTimeField()
    post_endtime =  models.DateTimeField()
    post_startaddress = models.CharField(max_length = 200)
    post_endaddress = models.CharField(max_length = 200)
    post_coachbox = models.IntegerField()
    post_transposts= models.CharField(max_length = 300)
    post_image = models.ImageField()