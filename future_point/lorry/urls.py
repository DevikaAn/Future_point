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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path('admin/', admin.site.urls),
    path("",include('homeapp.urls')),
    path("Master_Tutor_Registration/",include('Master_Tutor_Registration.urls')),
     path("Minor_Programmer/",include('Minor_Programmer.urls')),
    path("admin_module/",include('admin_module.urls')),
    path("tutorapp/",include('tutorapp.urls'))


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
