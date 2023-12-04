from django.urls import path, include
from usuarios import views
from .views import usuarios_view, RetrieveUpdateUsuarioView
from django.http import JsonResponse

def get_user_info(request):

    user = request.user
    print("USER: ", user)

    return JsonResponse({"user_id": user.id}, status=200)

urlpatterns = [
    path('usuarios/', usuarios_view, name='usuarios-list-create'),
    path('create/', views.createUsuarioView.as_view(), name='usuario-create'),
    path('token/', views.CreateTokenView.as_view()),
    path('usuario/<int:pk>/', RetrieveUpdateUsuarioView.as_view(), name='usuario-detail'),
    path('lista/<int:pk>/', views.RetrieveusuariosView.as_view(), name='usuarios-ver'),
    path('delete/<int:pk>/', views.DestroyUsuariosView.as_view(), name='delete'),
    path('list/', views.ListUsuariosView.as_view()),
    path('user-verify',views.user_verification, name='user_verification'),
    path("user-info", get_user_info)
]