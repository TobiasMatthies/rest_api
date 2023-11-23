from django.contrib import admin
from django.urls import path
from rest_framework import routers
from todo import views
from django.urls import include

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
