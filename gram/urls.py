from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from .forms import PostForm,ProfileForm

#Create your Urls here
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^logout/$', views.logout, {"next_page":'/'}),
    url(r'^explore/$',views.explore,name='explore'),
    url(r'^notification/$',views.notification,name='notification'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/upload/$',views.upload,name='upload'),
    url(r'^follow/(\d+)$',views.follow,name='follow'),
    url(r'^unfollow/(\d+)$',views.unfollow,name='unfollow'),
    
]
# if settings.DEBUG:
    # urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)