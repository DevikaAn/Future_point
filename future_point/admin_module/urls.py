from django.urls import path
from . import views

urlpatterns =[
   path("",views.loginpage),
   path("home",views.home),
   path("crs_del",views.crs_del),

   path("notification",views.notification),
   path("viewnots",views.viewnots),
   path("tutnots",views.tutnots),
   path("mastnots",views.mastnots),
   path('mail',views.mail),
   path('login',views.login),
   path('regnewcourse',views.regnewcourse),
   path("mp_confirm",views.mp_confirm),
   path("logout",views.logout),
   path("delt",views.delt),




]