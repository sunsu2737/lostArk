from django.db import models

# Create your models here.


class Pattern (models.Model):
    boss=models.TextField(null=False,default='',max_length=20)
    mode=models.TextField(null=False,default='',max_length=20)
    phase=models.TextField(null=False,default='1',max_length=1)
    guide=models.TextField(null=True,default='공략없음',max_length=1000)
class Boss(models.Model):
    boss=models.TextField(null=False,default='',max_length=20)
