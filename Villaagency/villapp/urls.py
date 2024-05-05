from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('sin/',views.signup, name='signup'),
    path('log/',views.login, name='login'),
    path('pro/',views.pro, name='pro'),
    path('det/',views.prodetails, name='det'),

    
]