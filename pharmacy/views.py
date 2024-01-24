from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Pharmacy
from .serializers import PharmacySerializer


class PharmacyViewSet(ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(__class__, self).get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name=name)
        return queryset

    def get_obj_by_pk(self, pk=None):
        try:
            pharmacy_object = self.get_queryset().get(pk=pk)
        except Exception:
            raise NotFound

        return pharmacy_object

    def list(self, request):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_obj_by_pk(pk))
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = self.get_serializer(self.get_obj_by_pk(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, pk=None):
        self.get_obj_by_pk(pk).delete()
        return Response({"message": "Pharmacy object deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
