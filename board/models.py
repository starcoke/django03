from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    content = models.TextField()
    likey = models.ManyToManyField(User, blank=True, related_name="likey")
                 # User를 가리키는 게 두 개이기 때문에 related name을 지정해준다.
    pubdate = models.DateTimeField()

    def __str__(self):
        return f"{self.subject} written by {self.writer}"

    def summary(self):
        if len(self.content) > 100:
            return f"{self.content[:100]} ..."
        return self.content
    
    def hot(self):
        if len(self.likey.all()) > 100:
            return True
        return False

class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board}_{self.replyer}"