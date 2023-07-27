from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from error_app.models import ErrorLog
from error_app.serializers import ErrorLogSerializer


class ErrorLogListView(ListAPIView):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer


class ErrorLogCreateView(CreateAPIView):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ErrorLogUpdateView(UpdateAPIView):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj


class ErrorLogDeleteView(DestroyAPIView):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
