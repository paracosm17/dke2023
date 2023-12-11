from django.urls import path

from shop import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main-page'),
]