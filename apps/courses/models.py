from django.db import models
from datetime import datetime
# Create your models here.


class Course(models.Model):
    """
    课程基本信息
    """
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=(("junior", "初级"), ("middle", "中级"), ("super", "高级")), max_length=10,
                              verbose_name="难度等级")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    """
    章节基本信息模型
    """
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加章节时间")

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name


class Video(models.Model):
    """
    课程单节视频模型
    """
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加视频时间")

    class Meta:
        verbose_name = "章节视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加资源时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name


