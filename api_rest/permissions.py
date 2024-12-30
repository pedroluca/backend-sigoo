from rest_framework.permissions import BasePermission

class IsTipo1(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.Usuario_TIPO == 1