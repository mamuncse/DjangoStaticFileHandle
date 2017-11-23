from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin #For Urlpatterns Not For Media Url

urlpatterns = [
    url(r'^admin/', admin.site.urls),

]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)