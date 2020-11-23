"""nepaltraders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from website import views as site


from django.conf import settings
from django.conf.urls.static import static
from clerk import views as clerk
urlpatterns=[
    path('admin/', admin.site.urls),
    path('',site.starter,name="home"),
    path('login/',clerk.logmein ,name="logimein"),
    path("clerks/logout/" ,clerk.log_out,name="log_out"),
    path("clerks",clerk.youarein,name="youarein"),
    path("gallery/",site.gallery_view,name="gallery"),
    path('aboutus/',site.about,name="about"),
    path('contact/',site.contact,name="contact"),

    path("pashmina/",site.pashmina,name="pashmina"),
    path('stones/',site.stones,name="stones"),
    path('handicraft/',site.handicraft,name="handicraft"),
    path('newin/',site.newin,name="newin"),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)