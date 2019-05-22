from django.urls import path
from django.conf.urls import url
from . import views


# we use below namespace for url to let django understand different urls if there are two urls with same name
app_name = 'blogs'

urlpatterns = [
    url(r'^$',views.templateindex,name='list'),
    path('index/',views.index),
    url(r'^create/$',views.blog_create,name="blog_create"),
    url(r'^(?P<slug>[\w-]+)/$',views.blog_details,name='details'),
    
]