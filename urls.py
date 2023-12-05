"""
URL configuration for reg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('home/logout/',views.LogoutPage,name='logout'),
    path('home/t1/',views.tut1,name='t1'),
    path('home/t2/',views.tut2,name='t2'),
    path('home/t3/',views.tut3,name='t3'),
    path('home/t4/',views.tut4,name='t4'),
    path('home/t1/home',views.nextt1,name='nt1'),
    
    
    path('home/t1/pr',views.progress,name='pr'),
    path('home/t2/pr1',views.progress,name='pr1'),
    path('home/t3/pr2',views.progress,name='pr2'),
    path('home/t4/pr3',views.progress,name='pr3'),
    path('home/quiz',views.quiz,name='quiz'),
    

]
