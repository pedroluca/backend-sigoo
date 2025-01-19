from django.urls import path
from . import views

urlpatterns = [
  path('', views.AreaInteresseList.as_view(), name='area_list'),
  path('add/', views.AreaInteresseCreate.as_view(), name='area_add'),
  path('<int:pk>/', views.AreaInteresseDetail.as_view(), name='area_detail'),
  path('update/<int:pk>/', views.AreaInteresseUpdate.as_view(), name='area_update'),
  path('delete/<int:pk>/', views.AreaInteresseDelete.as_view(), name='area_delete'),
  path('add-areas-interesse/', views.AdicionarAreasView.as_view(), name='adicionar_areas'),
]