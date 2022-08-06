from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.HomePageView.as_view(), name='home')
]
