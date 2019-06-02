from django.db import models


class StudentData(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=100)
    sloc = models.CharField(max_length=100)
    sfee = models.IntegerField()
