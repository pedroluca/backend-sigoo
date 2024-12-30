from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
  path('login/', obtain_auth_token, name='token_obtain_pair'),
  path('', views.UsuarioList.as_view(), name='usuario_list'),
  path('add/', views.UsuarioCreate.as_view(), name='usuario_add'),
  path('<int:pk>/', views.UsuarioDetail.as_view(), name='usuario_detail'),
  path('update/<int:pk>/', views.UsuarioUpdate.as_view(), name='usuario_update'),
  path('delete/<int:pk>/', views.UsuarioDelete.as_view(), name='usuario_delete'),
]