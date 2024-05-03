from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('sin/',views.signup, name='signup'),
    path('log/',views.login, name='login'),
    
]