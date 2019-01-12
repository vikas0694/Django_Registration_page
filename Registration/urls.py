from django.conf.urls import url
from django.contrib import admin
from signup.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$',signup),
    url(r'^login/$',login),
    url(r'^logout/$',logout)
]
