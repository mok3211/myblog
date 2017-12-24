from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm
def post_comment(request,post_pk):
    #先获取被评论的文章
    post = get_object_or_404(Post,pk = post_pk)
    #使用Post提交数据
    if request.method == 'Post':
        '''用户提交的数据存在request.POST 中，这是一个类字典操'''
        form = CommentForm(request.Post)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,'form':form,'comment_list':comment_list}
            return render(request,'blog/detail.html',context=context)
    return redirect(post)




