from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('dd_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]