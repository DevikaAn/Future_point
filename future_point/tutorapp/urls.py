from django.urls import path
from . import views
urlpatterns=[
   # path('',views.home),
    path("tutorreg", views.tureg),
    path("index", views.index),
    path("tutdetails", views.tregis),
    path("edit", views.edt),
    path('update', views.update),
    path('uploadnotes', views.uploadnotes),
    path('uploadworks',views.uploadworks),
    path('Notes',views.Notes),
    path('Works',views.Works),
    path("tutemail",views.tutemail),
    path('download_file',views.download_file),
     path('',views.login),
     path('home',views.home),
    path('logout',views.logout),
    path('appre',views.appre),
    path('delt',views.delt),
    path('gmeet',views.gmeet),
    path('sendlink',views.urlsve),
    path('videoup',views.video_upload),
    path('vclass',views.video),
    path('deletevideo',views.deletevideo),
    path("workDelete",views.workDelete)
]