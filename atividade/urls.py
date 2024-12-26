from django.urls import path
from . import views

urlpatterns = [
  path('', views.AtividadeList.as_view(), name='atividade_list'),
  path('add/', views.AtividadeCreate.as_view(), name='atividade_add'),
  path('<int:pk>/', views.AtividadeDetail.as_view(), name='atividade_detail'),
  path('update/<int:pk>/', views.AtividadeUpdate.as_view(), name='atividade_update'),
  path('delete/<int:pk>/', views.AtividadeDelete.as_view(), name='atividade_delete'),
]