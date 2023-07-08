from django.db import models

# Create your models here.

class SongModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class PointModel(models.Model):
    point = models.IntegerField()
    duedate = models.DateField()
    songmodel = models.ForeignKey(SongModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.point)
