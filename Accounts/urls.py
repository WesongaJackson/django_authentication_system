from django.urls import  path,include
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('logout/',views.logout_view,name='logout'),
    path('account/',include('allauth.urls'))
]