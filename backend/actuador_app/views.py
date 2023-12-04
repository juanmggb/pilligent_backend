from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from .models import Actuador
from .serializers import ActuadorSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
#import RPi.GPIO as GPIO
import time

class RetrieveUpdateActuadorView(generics.RetrieveUpdateAPIView):
    queryset = Actuador.objects.all()
    serializer_class = ActuadorSerializer
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes=[AllowAny]

    def get_object(self):
        #return self.request.user
        return self.queryset.get(pk=self.kwargs['pk'])
    
class DestroyActuadorView(generics.DestroyAPIView):
    queryset = Actuador.objects.all()
    serializer_class = ActuadorSerializer
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes=[AllowAny]

    def get_object(self):
        #return self.request.user
        return self.queryset.get(pk=self.kwargs['pk'])

#GPIO.setmode(GPIO.BCM)
@permission_classes([AllowAny])
@authentication_classes([AllowAny])
@api_view(['GET', 'POST'])
def controlar_actuadores(request, actuador_id=None):
    if request.method == 'GET':
        # Si se proporciona un ID, obtener solo ese actuador
        if actuador_id is not None:
            actuador = Actuador.objects.get(id=actuador_id)
            serializer = ActuadorSerializer(actuador)
            return Response(serializer.data)
        else:
            # Si no se proporciona un ID, obtener todos los actuadores
            actuadores = Actuador.objects.all()
            serializer = ActuadorSerializer(actuadores, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        # Si se proporciona un ID, actualizar ese actuador
        if actuador_id is not None:
            actuador = Actuador.objects.get(id=actuador_id)
            serializer = ActuadorSerializer(instance=actuador, data=request.data)
        else:
            # Si no se proporciona un ID, crear un nuevo actuador
            serializer = ActuadorSerializer(data=request.data)

        if serializer.is_valid():
            actuador = serializer.save()

            # Aquí puedes realizar operaciones adicionales con el actuador recién creado/actualizado
            # Por ejemplo, puedes acceder a actuador.id para obtener su identificador único

            # Controlar el actuador mediante GPIO
            controlar_gpio(actuador.pin_gpio, actuador.repeticiones)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def controlar_gpio(pin_gpio, repeticiones):

    #GPIO.setup(pin_gpio, GPIO.OUT)

    #for _ in range(repeticiones):
        # Avanzar
        #GPIO.output(pin_gpio, GPIO.HIGH)
        #time.sleep(1)  # Ajusta el tiempo según tus necesidades

        # Retroceder
        #GPIO.output(pin_gpio, GPIO.LOW)
        #time.sleep(1)  # Ajusta el tiempo según tus necesidades

    # Limpiar configuración GPIO al finalizar
    #GPIO.cleanup()
    return "Control GPIO completado"  #Esto no se ocupa, solo es para evitar errores para poder guardarlo antes de subirlo a la Pi
