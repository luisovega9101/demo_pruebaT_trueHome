from django.shortcuts import render
from rest_framework import generics

from app.test_api.models import *
from app.test_api.serializers import *

from app.test_api import msg_log

# Create your views here.

class tabla_List(generics.ListCreateAPIView):
    queryset = tabla.objects.all()
    serializer_class = tabla_Serializer
    
    def get(self, request, *args, **kwargs):
        try:
            object = self.list(request, *args, **kwargs)
            msg_log.Log("INFO ").info()
        except:
            msg_log.Log("ERR ").error()
        return object

    def post(self, request, *args, **kwargs):
        try:
            object = self.create(request, *args, **kwargs)
            msg_log.Log("INFO ").info()
        except:
            msg_log.Log("ERR ").error()
        return object

class tabla_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tabla.objects.all()
    serializer_class = tabla_Serializer
    
    def get(self, request, *args, **kwargs):
        try:
            object = self.retrieve(request, *args, **kwargs)
            msg_log.Log("INFO ").info()
        except:
            msg_log.Log("ERR ").error()
        return object

    def put(self, request, *args, **kwargs):
        try:
            object = self.update(request, *args, **kwargs)
            msg_log.Log("INFO ").info()
        except:
            msg_log.Log("ERR ").error()
        return object

    def patch(self, request, *args, **kwargs):
        try:
            object = self.partial_update(request, *args, **kwargs)
            msg_log.Log("INFO ").info()
        except:
            msg_log.Log("ERR ").error()
        return object

    def delete(self, request, *args, **kwargs):
        try:
            object = self.destroy(request, *args, **kwargs)
            msg_log.Log("INFO ").info()
        except:
            msg_log.Log("ERR ").error()
        return object