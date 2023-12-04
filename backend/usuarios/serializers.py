from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =[
            'id',
            'email',
            'name',
            'lastname',
            'username',
            'password',
            #'profile_picture',
            'type',
        ]
        extra_kwargs = {'password': {'write_only':True}, 'id':{'read_only':True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        usuario = super().update(instance, validated_data)
        if password:
            usuario.set_password(password)
            usuario.save()
        return usuario

class AuthTokenSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password = serializers.CharField(style={'input_type':'password'})
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        usuario = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not usuario:
            raise serializers.ValidationError('No se pudo validar', code='authorization')

        # Devolver un diccionario con la información necesaria
        return {'user': usuario}
