from django.urls import path
from . import views

urlpatterns = [
  path('', views.OrientacaoList.as_view(), name='orientacao_list'),
  path('add/', views.OrientacaoCreate.as_view(), name='orientacao_add'),
  path('<int:pk>/', views.OrientacaoDetail.as_view(), name='orientacao_detail'),
  path('update/<int:pk>/', views.OrientacaoUpdate.as_view(), name='orientacao_update'),
  path('delete/<int:pk>/', views.OrientacaoDelete.as_view(), name='orientacao_delete'),
]