from rest_framework import serializers # serializer import
from .models import User# 선언한 모델 import

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'uname', 'password', 'ubirth', 'usex', 'uemail', 'uphone', 'admin', 'acc_allow']