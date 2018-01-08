# coding:utf8
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
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
    gender = models.CharField(choices=(("male", "男"), ("female", "女")),
                              default="female", max_length=7)
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


class EmailVerifyRecord(models.Model):
    """
    邮箱验证模型
    """
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")), max_length=10,
                                 verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    """
    首页轮播图模型
    """
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name


