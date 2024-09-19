"""
URL configuration for core project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project import views
from project.views import HomeView, HomeUsersView, EditEmployee
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
router = DefaultRouter()
router.register(r'employee_api', views.EmployeeViewset, basename='employee_api')
router.register(r'education_api', views.EducationViewset, basename='education_api')
router.register(r'skip_api', views.SkipViewset, basename='skip_api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('users/<int:id>/', HomeUsersView.as_view(), name='user_by_id'),
    path('edit/<int:id>/', EditEmployee, name='edit'),
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('panel/', views.Panel.as_view(), name='panel'),
    path('logout/', LogoutView.as_view(), name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
