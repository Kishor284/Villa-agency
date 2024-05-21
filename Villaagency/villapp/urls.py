from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('sin/',views.signup, name='signup'),
    path('con/',views.contact, name='contact'),
    path('login/',views.login, name='login'),
    path('pro/',views.pro, name='pro'),
    path('det/',views.prodetails, name='det'),
    path('profile/',views.profile, name='profile'),
    path('error/',views.error, name='error'),
    path('admin1/',views.admin, name='admin'),
    path('users/',views.users, name='users'),
    path('del/',views.details_delete, name='user_details'),
    path('del1/<pk>',views.delete1, name='delete1'),
    path('home/',views.home, name='home'),
    path('if/',views.sdataform, name='admin_data_add'),
    path('upload/',views.images, name='upload_images'),
    


    
]