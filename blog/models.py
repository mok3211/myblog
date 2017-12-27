from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
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
    def save(self,*args,**kwargs):
        #如果没有填写摘要
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:50]
            super(Post,self).save(*args,**kwargs)
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
    #新增views字段记录阅读量
    views = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs = {'pk':self.pk})
    class Meta:
        ordering = ['-create_time']
