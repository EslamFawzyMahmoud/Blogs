from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('',views.allPosts, name='all_post'),
    path('<int:id>',views.post, name='post'),
]
