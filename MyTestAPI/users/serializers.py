from rest_framework import serializers
#from .models import User


#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ['pk', 'first_name', 'last_name', 'username', 'email', 'password', 'consent']


#class UserSerializer(serializers.Serializer):
#    first_name = serializers.CharField(max_length=70)
#    last_name = serializers.CharField(max_length=70)
#    username = serializers.CharField(max_length=70)
#    email = serializers.EmailField(max_length=70)
#    password = serializers.CharField(max_length=70)
#    consent = serializers.BooleanField(default=False)

#    def create(self, validated_data):
#        return User.objects.create(validated_data)

#    def update(self, instance, validated_data):
#        instance.first_name = validated_data.get('first_name', instance.first_name)
#        instance.last_name = validated_data.get('last_name', instance.last_name)
#        instance.username = validated_data.get('username', instance.username)
#        instance.email = validated_data.get('email', instance.email)
#        instance.password = validated_data.get('password', instance.password)
#        instance.consent = validated_data.get('consent', instance.consent)
#        instance.save()
#        return instance

