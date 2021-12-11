from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorView,basename='api')

urlpatterns = [
    path('', include(router.urls)),
]