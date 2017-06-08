from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.urls import reverse
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def place1(request):
    return render(request, '東區.html')

def place2(request):    
    return render(request, '龍山寺.html')

def place3(request):
    return render(request, '西門町.html')

def place4(request):
    return render(request, '永康.html')

def place5(request):
    return render(request, '美麗華.html')

def place6(request):
    return render(request, '寶藏巖.html')

def place7(request):
    return render(request, '九份.html')

def place8(request):
    return render(request, '平溪.html')

def place9(request):
    return render(request, '鶯歌.html')

def place10(request):
    return render(request, 'houtong.html')

def place11(request):
    return render(request, 'buyen.html')

def place12(request):
    return render(request, 'badouzi.html')

def place13(request):
    return render(request, 'miaokow.html')

def place14(request):
    return render(request, 'wangyou.html')

def place15(request):
     return render(request, 'daping.html')

def place16(request):
    return render(request, 'chaoning.html')

def place17(request):
    return render(request, 'northeast.html')

def place18(request):
    return render(request, 'caoling.html')

def place19(request):
    return render(request, '三峽.html')

def place20(request):
    return render(request, '淡水.html')    

def weather(request):
    return render(request, 'weather.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def home_eng(request):
    return render(request, 'nav-bar-eng.html')

def home_jp(request):
    return render(request, 'nav-bar-jp.html')

def Tagfamily(request):
    return render(request, 'Tag-family.html')

def Tagfamous(request):
    return render(request, 'Tag-famous.html')  

def Taggirls(request):
    return render(request, 'Tag-girls.html')

def Tagloner(request):
    return render(request, 'Tag-loner.html')

def Taglove(request):
    return render(request, 'Tag-love.html')

def Tagtourist(request):
    return render(request, 'Tag-tourist.html')

def Tagwriter(request):
    return render(request, 'Tag-writer.html')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})                                   