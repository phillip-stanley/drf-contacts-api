"""
URL configuration for contacts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from contacts.address.views import ContactsViewSet
from contacts.views import ContactsTokenObtainPairView, UserRegistrationView

contacts_router = DefaultRouter()
contacts_router.register(r"api/contacts", ContactsViewSet, basename="contacts")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", UserRegistrationView.as_view(), name="user registration"),
    path("api/token/", ContactsTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
urlpatterns += contacts_router.urls
