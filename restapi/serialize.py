from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'sex', 'password', 'age')

        def create(self, validated_data):
            print('create', type(validated_data), validated_data)
            id = validated_data['id']
            username = validated_data['username']
            password = validated_data['password']
            age = validated_data['age']
            sex = validated_data['sex']
            email = validated_data['email']

            person = User(id=id,username=username, password=password,age=age,sex=sex,email=email)
            person.save()
            return person