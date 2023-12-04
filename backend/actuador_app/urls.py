from django.urls import path
from .views import controlar_actuadores, controlar_gpio, RetrieveUpdateActuadorView, DestroyActuadorView
#Tengo dudas si se tiene que poner "api/"
urlpatterns = [
    path('actuadores/controlar_actuadores/', controlar_actuadores, name='controlar_actuadores'),
    path('actuadores/controlar_actuadores/<int:pk>/', RetrieveUpdateActuadorView.as_view(), name='actuadores'),
    path('actuadores/eliminar_actuadores/<int:pk>/', DestroyActuadorView.as_view(), name='Delete'),
    path('actuadores/controlar_gpio/', controlar_gpio, name='controlar_gpio'),
]
