from django.urls import path
from . import views

"""
プライマリーキーが文字列の場合slug:pkと指定する
"""
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('usstocklist/add/', views.AddView.as_view(), name='add'),
  path('usstocklist/edit/<slug:pk>', views.EditView.as_view(), name='edit'),
]
