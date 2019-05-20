from django.db import models


# Create your models here.

class Poll(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    questions = models.TextField(verbose_name='问题')
    option_one = models.CharField(max_length=50, verbose_name='第一个选项')
    option_two = models.CharField(max_length=50, verbose_name='第二个选项')
    poll_one = models.IntegerField(default=0, verbose_name='第一个票数')
    poll_two = models.IntegerField(default=0, verbose_name='第二个票数')

    class Meta:
        verbose_name = '问题'

    # def __str__(self):
    #     return self.id


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=50, verbose_name='用户账号')
    pwd = models.CharField(max_length=50, verbose_name='用户密码')

    class Meta:
        verbose_name = '用户'
