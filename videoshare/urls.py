from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home", views.home, name="home"),
    path("videoplayer", views.videoplayer, name="videoplayer")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

