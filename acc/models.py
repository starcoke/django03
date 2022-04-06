from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    comment = models.TextField() # 자기소개
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="user/%y/%m")
                 #날짜별로 파일 자동생성해서 업로드

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.jpeg"
