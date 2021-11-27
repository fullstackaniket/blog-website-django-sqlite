"""calvin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('category',views.category, name="category"),
    path('contact',views.contact, name="contact"),
    path('basic',views.basic, name="basic"),
    path('signup',views.signup, name="signup"),
    path('singleaudio',views.singleaudio, name="singleaudio"),
    path('singlevideo',views.singlevideo, name="singlevideo"),
    path('singlestandard/<int:id>/<slug>',views.singlestandard,name="singlestandard"),
    path('styles',views.styles,name="styles"),
    path('blogpost',views.blogpost, name ="blogpost"),
    path('login',auth_views.LoginView.as_view(), name="login"),
    #path('login',auth_views.LoginView.as_view(template="login.html")),
    path('signup1',views.signup1, name="signup1"),
    path('logout',views.logout, name="logout"),
    path('display',views.display, name="display"),
    path('base',views.base, name="base"),
    path('like_post',views.like_post, name="like_post"),
    path('post_edit/<int:id>',views.post_edit, name="post_edit"),
    path('cate_edit',views.cate_edit, name="cate_edit"),
   
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)