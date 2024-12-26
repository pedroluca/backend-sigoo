from django.urls import path
from . import views

urlpatterns = [
  path('', views.ReuniaoList.as_view(), name='reuniao_list'),
  path('add/', views.ReuniaoCreate.as_view(), name='reuniao_add'),
  path('<int:pk>/', views.ReuniaoDetail.as_view(), name='reuniao_detail'),
  path('update/<int:pk>/', views.ReuniaoUpdate.as_view(), name='reuniao_update'),
  path('delete/<int:pk>/', views.ReuniaoDelete.as_view(), name='reuniao_delete'),
]