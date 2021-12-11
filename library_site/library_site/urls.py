from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from books.views import *
from authors.views import *
from genres.views import *

router1 = routers.DefaultRouter()
router1.register('books', BookViewSet)
router1.register('authors', AuthorViewSet)
router1.register('genres', GenreViewSet)
router1.register('books-search',BookSearch,'books-search')

urlpatterns = [
    path('api/', include(router1.urls)),
    path('admin/', admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)