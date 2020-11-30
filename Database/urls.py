"""laboratory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from.import views

urlpatterns = [
      path('index', views.index, name='index'),
      path('register', views.register, name='register'),
      path('thanks', views.thanks, name='thanks'),
      path('blood', views.blood, name='blood'),
      path('br', views.bloodr, name='br'),
      path('vitamin', views.vitamin, name='vitamin'),
      path('vr', views.vr, name='vr'),
      path('hormone', views.hormone, name='hormone'),
      path('hr', views.hr, name='hr'),
      path('serology', views.serology, name='serology'),
      path('sr', views.sr, name='sr'),
      path('Copd', views.copd, name='copd'),
      path('report', views.report, name='report'),
      path('Login', views.login, name='login'),
      path('Fail', views.fail, name='fail'),
]
