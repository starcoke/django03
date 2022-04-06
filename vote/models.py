from django.db import models
from acc.models import User

# Create your models here.
class Topic(models.Model):
    subject = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maker')
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True, related_name="voter")
    #voter와 maker 둘다 User를 참조하기 때문에 related_name을 주어야 한다.
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) > 10:
            return f"{self.content[:10]} ..."
        return self.content 


class Sel(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sname = models.CharField(max_length=100)
    spic = models.ImageField(upload_to="vote/%y/%m")
    scon = models.TextField()
    choicer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.topic}_{self.sname}"
