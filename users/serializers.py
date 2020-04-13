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
    class Meta:
        model = Profile
        fields = ['website', 'phone_number', 'biography']