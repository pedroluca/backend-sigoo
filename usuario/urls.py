from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('login/', obtain_auth_token, name='token_obtain_pair'),
    path('valid-token/', views.ValidUser.as_view(), name='valid_token'),
    path('', views.UsuarioList.as_view(), name='usuario_list'),
    path('add/', views.UsuarioCreate.as_view(), name='usuario_add'),
    path('<int:pk>/', views.UsuarioDetail.as_view(), name='usuario_detail'),
    path('update/<int:pk>/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('delete/<int:pk>/', views.UsuarioDelete.as_view(), name='usuario_delete'),
    path('get-aluno-orientacao/<int:id_aluno>/', views.GetAlunoOrientacao.as_view(), name='get_aluno_orientacao'),
    path('get-professor-orientacoes/', views.GetProfessorOrientacoes.as_view(), name='get_professor_orientacoes'),
    path('update-password/', views.PasswordUpdateView.as_view(), name='update_password'),
]