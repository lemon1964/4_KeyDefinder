from rest_framework import serializers
from .models import MessageFront
from .models import UserKey


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFront
        fields = ('user', 'date', 'screen', 'event', 'key')


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKey
        fields = ('user', 'keywisper')

