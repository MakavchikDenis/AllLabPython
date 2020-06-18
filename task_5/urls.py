
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^AppPhoneCatalog/', include("AppPhoneCatalog.urls")),
    url(r'^admin/', admin.site.urls)
]
