from django.conf.urls import url
from . import views 

app_name = 'attractions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^home/$', views.home, name='home'),
    url(r'^place1/$', views.place1, name='place1'),
    url(r'^place2/$', views.place2, name='place2'),
    url(r'^place3/$', views.place3, name='place3'),
    url(r'^place4/$', views.place4, name='place4'),
    url(r'^place5/$', views.place5, name='place5'),
    url(r'^place6/$', views.place6, name='place6'),
    url(r'^place7/$', views.place7, name='place7'),
    url(r'^place8/$', views.place8, name='place8'),
    url(r'^place9/$', views.place9, name='place9'),
    url(r'^place10/$', views.place10, name='place10'),
    url(r'^place11/$', views.place11, name='place11'),
    url(r'^place12/$', views.place12, name='place12'),
    url(r'^place13/$', views.place13, name='place13'),
    url(r'^place14/$', views.place14, name='place14'),
    url(r'^place15/$', views.place15, name='place15'),
    url(r'^place16/$', views.place16, name='place16'),
    url(r'^place17/$', views.place17, name='place17'),
    url(r'^place18/$', views.place18, name='place18'),
    url(r'^place19/$', views.place19, name='place19'),
    url(r'^place20/$', views.place20, name='place20'),    
    url(r'^weather/$', views.weather, name='weather'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^home_eng/$', views.home_eng, name='home_eng'),
    url(r'^home_jp/$', views.home_jp, name='home_jp'),
    url(r'^Tagfamily/$', views.Tagfamily, name='Tagfamily'),
    url(r'^Tagfamous/$', views.Tagfamous, name='Tagfamous'),
    url(r'^Taggirls/$', views.Taggirls, name='Taggirls'),
    url(r'^Tagloner/$', views.Tagloner, name='Tagloner'),
    url(r'^Taglove/$', views.Taglove, name='Taglove'),
    url(r'^Tagtourist/$', views.Tagtourist, name='Tagtourist'),
    url(r'^Tagwriter/$', views.Tagwriter, name='Tagwriter'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]


