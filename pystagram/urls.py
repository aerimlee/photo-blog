from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from photos.views import detail

urlpatterns = [

    url(r'^admin/', admin.site.urls),
]

