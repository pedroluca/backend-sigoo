from django.urls import path, include

urlpatterns = [
  path('area-interesse/', include('area_interesse.urls')),
  path('reuniao/', include('reuniao.urls')),
  path('atividade/', include('atividade.urls')),
  path('post/', include('post.urls')),
  path('orientacao/', include('orientacao.urls')),
  path('usuario/', include('usuario.urls')),
]