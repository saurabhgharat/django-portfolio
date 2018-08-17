from jobs import views
from django.urls import path


app_name='jobs'
urlpatterns=[
            path('',views.home,name='home'),

]
