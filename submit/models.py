#models.py File

from django.db import models


class Post(models.Model):
    name= models.CharField(max_length=300, unique=True) # tên
    yourclass = models.CharField(max_length=50) # lớp
    content= models.TextField() # lời cảm ơn(content cho nó gọn)
    def __str__(self):
        return f"{self.name}"