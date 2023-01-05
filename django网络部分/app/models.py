from django.db import models
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    tel = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    class Meta:
        verbose_name_plural = '系统用户表'  # 此时，admin中表的名字就是‘用户表‘
    def __str__(self):
        return self.name


class Breast(models.Model):
    id = models.AutoField(primary_key=True)
    perimeter_worst = models.FloatField(verbose_name='最差周长')
    concave_points_worst = models.FloatField(verbose_name='最差凹点')
    area_mean = models.FloatField(verbose_name='平均区域')
    radius_worst = models.FloatField(verbose_name='最差半径')
    area_worst = models.FloatField(verbose_name='最差区域')
    perimeter_mean = models.FloatField(verbose_name='平均周长')
    concave_points_mean = models.FloatField(verbose_name='平均凹点')
    radius_mean = models.FloatField(verbose_name='平均半径')
    concavity_mean = models.FloatField(verbose_name='平均凹度')
    concavity_worst = models.FloatField(verbose_name='最差凹度')
    compactness_worst = models.FloatField(verbose_name='最差紧密度')
    area_se = models.FloatField(verbose_name='区域')
    smoothness_worst = models.FloatField(verbose_name='最差平滑度')
    radius_se = models.FloatField(verbose_name='半径')
    texture_worst = models.FloatField(verbose_name='最差纹理')
    diagnosis = models.IntegerField(verbose_name='是否为癌症')

    class Meta:
        verbose_name_plural = '乳腺癌信息表'  # 此时，admin中表的名字就是‘用户表‘








