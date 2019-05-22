from django.db import models

# Create your models here.


class Gallery(models.Model): # model改了一定要重新迁移到数据库中
    description = models.CharField(default='这里写作品介绍',max_length=100)
    image = models.ImageField(default='default.png',upload_to='images/')
    tital = models.CharField(default='作品标题',max_length=50)

    def __str__(self):
        return self.tital
