from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('usstocklist/add/', views.AddView.as_view(), name='add'),
]
