from django.db import models
import random

# Create your models here.


class NumData(models.Model):
    val = models.FloatField()
    create_at = models.DateTimeField("create time", auto_now_add=True)

    class Meta:
        app_label = 'app1'
        abstract = True


class RealTimeNum(NumData):

    @classmethod
    def create_10_nums(cls):
        return cls.objects.bulk_create([cls(val=random.random()) for x in range(10)])


class SavedNum(NumData):
    pass
