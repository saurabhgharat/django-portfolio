from django.urls import path
from . import views
urlpatterns = [
              path('',views.bloglist,name='bloglist'),
              path('<int:blog_id>',views.detail,name='detail'),
              ]
