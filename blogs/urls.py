from django.urls import path
from .views import PostList, PostDetail, home


urlpatterns=[
  path('', home, name='home'),
  path('myblog/', PostList, name='blog'),
  path('<int:user>', PostDetail, name='post_detail')
]