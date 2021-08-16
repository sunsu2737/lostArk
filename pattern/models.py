from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Boss(models.Model):
    boss=models.TextField(null=False,default='',max_length=20)
class Pattern (models.Model):
    boss_object=Boss.objects.all()
    modes=['노말','하드','헬','리허설','어비스']
    phases=['1','2','3','4','5','6','7']
    boss_choice=[(boss_name.boss,boss_name.boss) for boss_name in boss_object]
    mode_choice=[(mode_name,mode_name) for mode_name in modes]
    phase_choice=[(phase_name,phase_name) for phase_name in phases]
    boss=models.CharField(choices=boss_choice,default='',max_length=20)
    mode=models.CharField(choices=mode_choice,default=modes[0],max_length=10)
    phase=models.CharField(choices=phase_choice,default=phases[0],max_length=2)
    guide=RichTextField(blank=True,null=True,config_name='awesome_ckeditor')
