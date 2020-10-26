from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profile.user
        fields = ["username",'email','bio','image']