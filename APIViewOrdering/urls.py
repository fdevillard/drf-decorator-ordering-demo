"""
URL configuration for APIViewOrdering project.

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

from APIViewOrdering.views import view_with_permission_first, view_with_api_view_first

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-view-first/', view_with_api_view_first, name='api_view_first'),
    path('permission-first/', view_with_permission_first, name='permission_first'),
]
