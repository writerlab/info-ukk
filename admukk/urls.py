from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from info.views import Lab1Viewset, Lab2Viewset

router = routers.DefaultRouter()
router.register('lab1', Lab1Viewset)
router.register('lab2', Lab2Viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
