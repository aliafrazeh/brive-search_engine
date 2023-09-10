from django.db import models

# Create your models here.
class serachArticle(models.Model):
    titlesearceh = models.CharField(verbose_name="title-search",max_length=75)
    title = models.CharField(verbose_name="title",max_length=75)
    description = models.TextField(verbose_name="description",max_length=175)
    url = models.URLField(verbose_name="URL",max_length=157)
    status = models.BooleanField(default=False,verbose_name="STATUS")
    def __str__(self):
        return self.titlesearceh + " | " + self.title