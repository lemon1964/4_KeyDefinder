# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from .serializers import KeySerializer
from .models import MessageFront
from .models import UserKey
from rest_framework import permissions
from itertools import cycle


class MessageView(APIView):
    queryset = MessageFront.objects.all()
    permission_classes = [permissions.AllowAny]
    user_key_iterator = cycle(UserKey.objects.all())

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            selected_other_instance = next(self.user_key_iterator)
            serializer.validated_data['key'] = selected_other_instance.keywisper
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class KeyView(APIView):
    queryset = UserKey.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            MessageView.user_key_iterator = cycle(UserKey.objects.all())
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


