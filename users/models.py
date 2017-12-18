from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户数据表继承django默认user类，作为user个人信息的表
    """
    # 用户昵称
    nick_name = models.CharField(max_length=50,
                                 verbose_name="昵称",
                                 default="")
    # 生日
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 性别
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="female", max_length=5)
    # 地址
    address = models.CharField(max_length=100, default="")
    # 手机号
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
