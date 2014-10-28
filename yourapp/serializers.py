from yourapp.models import Group, Profile
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class ProfileSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Profile
