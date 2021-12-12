from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from books.views import *
from authors.views import *
from genres.views import *
from upload.views import *
from uploadS3_storage.views import *
from django.contrib.auth import views as auth_views
from .views import login_view, home_view

router1 = routers.DefaultRouter()
router1.register('books', BookViewSet)
router1.register('authors', AuthorViewSet)
router1.register('genres', GenreViewSet)
router1.register('books-search',BookSearch,'books-search')
router1.register('upload',UploadViewSet)
router1.register('upload_S3',UploadS3ViewSet,'upload_S3')

urlpatterns = [
    path('api/', include(router1.urls)),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls',namespace='social')),
    path("", home_view, name="home"),
    path('search/', include('search.urls')),
    path('redis_key/', include('redis_key.urls')), 
    path('chat/', include('chat.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)