from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'avatar_url'
        )

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True)
    avatar = serializers.ImageField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['name'] = self.validated_data.get('name', '')
        data['avatar'] = self.validated_data.get('avatar', None)
        return data

    def save(self, request):
        user = super().save(request)
        user.name = self.validated_data.get('name', '')
        user.avatar = self.validated_data.get('avatar', None)
        user.save()
        return user