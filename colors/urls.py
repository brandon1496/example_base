from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('colors', views.ColorView)

urlpatterns = [
    path('list', include(router.urls)),
]
