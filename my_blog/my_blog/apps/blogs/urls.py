
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(),name='login'),
    url(r'^detail/$', views.LoginsuccessView.as_view(),name='detail'),
    url(r'^register/$', views.RegisterView.as_view(),name='register'),

]
