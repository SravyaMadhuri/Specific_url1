from django.urls import path
from app1.views import *

app_name='whatever'

urlpatterns=[
    path('csk/',csk,name='csk'),
]