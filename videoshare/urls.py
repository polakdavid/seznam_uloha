from django.urls import path
from videoshare import views

urlpatterns = [
    path("", views.home, name="home")
]