from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from usuarios.serializers import UsuarioSerializer, AuthTokenSerializer
from usuarios.models import Usuario
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from django.http import Http404

class createUsuarioView(generics.CreateAPIView):
    serializer_class=UsuarioSerializer
    permission_classes=[]
    authentication_classes=[]
    
class ListUsuariosView(generics.ListAPIView):
    serializer_class=UsuarioSerializer
    def get_queryset(self):
        return Usuario.objects.all()
    
class RetrieveusuariosView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes=[AllowAny]

    def get_object(self):
        #return self.request.user
        return self.queryset.get(pk=self.kwargs['pk'])
    
class DestroyUsuariosView(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk']) 
        except Usuario.DoesNotExist:
            raise Http404("Usuario no encontrado")
    
class RetrieveUpdateUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes=[AllowAny]

    def get_object(self):
        #return self.request.user
        return self.queryset.get(pk=self.kwargs['pk'])   

    
class CreateTokenView(ObtainAuthToken):
    serializer_class=AuthTokenSerializer

# Prueba

@api_view(['GET', 'POST'])
@permission_classes([])
@authentication_classes([])
def usuarios_view(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_verification(request):
    username = request.GET.get('userName','')

    user_exist = Usuario.objects.filter(username=username).exists()
    response=JsonResponse({'user_exist':user_exist}, status=status.HTTP_200_OK)
    response['Access-Control-Allow-Origin']='http://localhost:3000'
    return response

