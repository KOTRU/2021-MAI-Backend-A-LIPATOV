from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include
from upload.views import image_upload

urlpatterns = [
    path("", image_upload, name="upload"),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)