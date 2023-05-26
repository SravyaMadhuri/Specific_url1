from django.urls import path
from app2.views import *

app_name='anywhere'

urlpatterns=[
    path('csk/',csk,name='csk'),
]