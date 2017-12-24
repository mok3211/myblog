from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#分类
class Category(models.Model):
    '''Django 的模型继承'''
    #存储比较短的字符串CharField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#文章
class Post(models.Model):
    '''文章属性'''
    #文章标题
    title = models.CharField(max_length=100)
    #文章正文 用TextField()来存储大段文本
    body = models.TextField()
    #分别表示创建时间和最后一次修改时间
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #文章摘要 注意 默认情况下CharField不为空,指定CharField的blank=True 参数值后就可以允许空值
    excerpt = models.CharField(max_length=200,blank=True)
    #关系 Foreignkey 一对多关系 ManyToManyField 多对多关系
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    #User从django.contrib.auth.models引入
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs = {'pk':self.pk})
    class Meta:
        ordering = ['-create_time']
