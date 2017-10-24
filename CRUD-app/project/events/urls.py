"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name="index"),
    url(r'^create/$', views.CreateView.as_view(), name="create"),
    url(r'^(?P<event_id>\d+)/edit/$', views.EditView.as_view(), name="edit"),
    url(r'^(?P<event_id>\d+)/details/$', views.DetailView.as_view(), name="edit"),
    url(r'^(?P<event_id>\d+)/delete/$', views.DeleteView.as_view(), name="delete"),
    url(r'^(?P<event_id>\d+)/attend/$', views.AttendView.as_view(), name="attend"),
    url(r'^(?P<username>\w+)/$', views.UserPosts.as_view(), name="user_posts")
]

