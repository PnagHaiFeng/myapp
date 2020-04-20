from django.db import models
from django.contrib.auth.models import User



class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=20,verbose_name="标题")
    content = models.TextField()
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    last_updated_time = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_updated_time']
