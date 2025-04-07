"""
URL configuration for registro_visitantes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import VisitorViewSet, AccessLogViewSet, PolicialViewSet, PresencaDiariaViewSet, PolicialPresencaViewSet, PolicialPresencaCheckInViewSet, PolicialPresencaCheckOutViewSet
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'visitantes', VisitorViewSet)
router.register(r'acessos', AccessLogViewSet)
router.register(r'policiais', PolicialViewSet)
router.register(r'presenca_diaria', PresencaDiariaViewSet)
router.register(r'policialpresenca', PolicialPresencaViewSet, basename='policialpresenca')
router.register(r'policialpresenca-checkin', PolicialPresencaCheckInViewSet, basename='policialpresenca-checkin')
router.register(r'policialpresenca-checkout', PolicialPresencaCheckOutViewSet, basename='policialpresenca-checkout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]