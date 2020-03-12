
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(),name='login'),
    url(r'^details/$', views.LoginsuccessView.as_view(),name='details'),
    url(r'^register/$', views.RegisterView.as_view(),name='register'),
    url(r'^det_index/$', views.Det_indexView.as_view(),name='det_index'),
    url(r'^whisper/$', views.WhisperView.as_view(),name='whisper'),
    url(r'^leacots/$', views.LeacotsView.as_view(),name='leacots'),
    url(r'^album/$', views.AlbumView.as_view(),name='album'),
    url(r'^about/$', views.AboutView.as_view(),name='about'),

]
#
# class ="layui-nav-item" > < a href="det_index.html" class ="active" > 文章 < / a > < / li >
# class ="layui-nav-item" > < a href="whisper.html" > 微语 < / a > < / li >
# class ="layui-nav-item" > < a href="leacots.html" > 留言 < / a > < / li >
# class ="layui-nav-item" > < a href="album.html" > 相册 < / a > < / li >
# class ="layui-nav-item" > < a href="about.html" class ="active" > 关于 < / a > < / li >