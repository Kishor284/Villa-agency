from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings
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
    path('views/',views.admin_views_datas, name='views'),
    path('success/', views.success, name='success'),
    path('image2/', views.uploads, name='image2'),
    path('cart/', views.cart, name='cart'),
    path('data/', views.Data, name='data'),
    path('dview/', views.dataviewss, name='dview'),
       
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)