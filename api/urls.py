from django.conf.urls import url
#import path
from django.urls import path
from . import views


urlpatterns = [
path('items', views.task1 , name='task1'),
path('booking', views.task2_booking, name='task2_booking'),
path('cancel', views.task2_cancel, name='task2_cancel'),
path('plot', views.task3 , name='task3'),
]