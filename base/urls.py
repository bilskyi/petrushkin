from django.urls import path, include
from base import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'pictures', views.PictureViewSet)


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
] + path('', include(router.urls))