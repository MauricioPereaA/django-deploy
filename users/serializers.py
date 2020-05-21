"""Users Serializers"""

#Django
from django.contrib.auth.models import User, Group
from rest_framework import serializers


#Models
from .models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Profile Serializer"""

    username = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ['username' , 'website', 'phone_number', 'biography']