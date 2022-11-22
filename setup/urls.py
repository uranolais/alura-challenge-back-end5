from django.contrib import admin
from django.urls import path, include
from challenge.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideoViewSet,basename='Videos')
router.register('categorias', CategoriaViewSet,basename='Categorias')
router.register('lista', ListaCategoriaViewSet,basename='Lista')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
