from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('about/',views.about,name='about'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('log/',views.log,name="log"),
    path('logout/',views.logout,name="logout"),
    path('superuser/',views.superuser,name="superuser")
    
]
