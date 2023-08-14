from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post
# Create your views here.
def index(request):
    # return  HttpResponse("Hi There! This is the first message in Django!")
    all_post = Post.objects.all()
    to_ret = '<body>'
    for post in all_post:
        to_ret = to_ret + '<p>' + post.text + '</p>'
        to_ret = to_ret + '<hr>'

    to_ret = to_ret + '</body>'
    return HttpResponse(to_ret)