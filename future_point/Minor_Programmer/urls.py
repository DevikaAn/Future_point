"""lorry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns =[

    path("minorpgrmerreg",views.mpreg),
    path('Notes',views.Notes),
    path("index",views.index),
    path("mpdetails",views.mpegis),
    path("mpdetailsT",views.mpegisT),
    path("minorwork",views.minorwork),
    path("viewminorwork",views.viewminorwork),
    path("mipremail",views.mipremail),
    path('download_file',views.download_file),
    path("edit", views.edt),
    path('update', views.update),
     path('',views.login),
     path('home',views.home),
    path('logout',views.logout),
    path('view_mp',views.view_mp),
    path('onlineeditor',views.onlineeditor),
    path('shareprofile',views.shareprofile),
    path('liveclass',views.urllink),
    path('Worksmp',views.Worksmp),
    path('deleteminwork',views.deleteminwork),
    

]
