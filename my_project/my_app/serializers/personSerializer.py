from rest_framework import serializers
from ..models import Person
from .userSerializer import UserSerializer
from rest_framework.authtoken.models import Token

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Person
        fields = ['user', 'person_id', 'city', 'street', 'house_number']
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        token = Token.objects.create(user=user)
        person = Person.objects.create(user=user, **validated_data)
        person.token = token.key
        return person