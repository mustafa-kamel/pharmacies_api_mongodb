from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Pharmacy
from .serializers import PharmacySerializer


class PharmacyViewSet(ModelViewSet):
    """API endpoint for managing pharmacies.
    This viewset provides CRUD operations for pharmacy objects.

    **Supported Actions:**

    * `list(request)`: Get a list of all pharmacies or filter by name (GET /pharmacies/).
    * `create(request)`: Create a new pharmacy (POST /pharmacies/).
    * `retrieve(request, pk)`: Get a specific pharmacy by primary key or name (GET /pharmacies/{pk}/).
    * `update(request, pk)`: Update an existing pharmacy (PUT/PATCH /pharmacies/{pk}/).
    * `destroy(request, pk)`: Delete a pharmacy (DELETE /pharmacies/{pk}/).

    **Authentication:**

    This viewset requires basic authentication for all actions.

    **Permissions:**

    * `IsAuthenticated`: All actions require authenticated users.
    """

    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Get the queryset of Pharmacy objects.

        Returns:
        - QuerySet: The queryset of Pharmacy objects and filter by name if it exists.
        """

        queryset = super(__class__, self).get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name=name)
        return queryset

    def get_obj_by_pk(self, pk=None):
        """Retrieve a specific pharmacy by primary key.

        Parameters:
        - pk (int): The primary key of the pharmacy to retrieve.

        Returns:
        - Pharmacy: The pharmacy object with the specified primary key.

        Raises:
        - NotFound: If the pharmacy with the specified primary key does not exist."""

        try:
            pharmacy_object = self.get_queryset().get(pk=pk)
        except Exception:
            raise NotFound

        return pharmacy_object

    def list(self, request):
        """List all pharmacies or filter by name.

        **Request Parameters:**

        - `name` (optional, string): Filter pharmacies by name (exact match).

        **Response:**

        - **200 OK:**
            ```json
            {
            "count": 17,
            "next": "http://127.0.0.1:8000/pharmacies/?page=2",
            "previous": null,
            "results": [
                        {
                            "id": 1,
                            "name": "Pharmacy 1",
                            "address": "123 Main St",
                            "phone_number": "123-456-7890",
                            "license_number": "ABC123"
                        },
                        ...
                    ]
            }
            ```
        - **400 BAD_REQUEST:** Invalid request parameters.
        """

        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new pharmacy.

        **Request Body:**

        ```json
        {
            "name": "New Pharmacy",
            "address": "555 Elm St",
            "phone_number": "555-123-4567",
            "license_number": "XYZ987"
        }
        ```

        **Response:**

        - **201 CREATED:**
            ```json
            {
                "id": 4,
                "name": "New Pharmacy",
                "address": "555 Elm St",
                "phone_number": "555-123-4567",
                "license_number": "XYZ987"
            }
            ```
        - **400 BAD_REQUEST:** Invalid serializer data.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Retrieve a specific pharmacy by primary key or name.

        **Path Parameters:**

        - `pk` (integer): Primary key of the pharmacy to retrieve.

        **Response:**

        - **200 OK:**
            ```json
            {
                "id": 1,
                "name": "Pharmacy 1",
                "address": "123 Main St",
                "phone_number": "123-456-7890",
                "license_number": "ABC123"
            }
            ```
        - **404 NOT_FOUND:** Pharmacy not found.
        """

        serializer = self.get_serializer(self.get_obj_by_pk(pk))
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Update an existing pharmacy.

        **Path Parameters:**

        - `pk` (integer): Primary key of the pharmacy to update.

        **Request Body:**

        ```json
        {
            "name": "Updated Pharmacy Name",
            "phone_number": "987-654-3210"
        }
        ```

        **Response:**

        - **200 OK:**
            ```json
            {
                "id": 1,
                "name": "Updated Pharmacy Name",
                "address": "123 Main St",
                "phone_number": "987-654-3210",
                "license_number": "ABC123"
            }
            ```
        - **400 BAD_REQUEST:** Invalid serializer data.
        - **404 NOT_FOUND:** Pharmacy not found.
        """

        serializer = self.get_serializer(self.get_obj_by_pk(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Delete a pharmacy.

        **Path Parameters:**

        - `pk` (integer): Primary key of the pharmacy to delete.

        **Response:**

        - **204 NO CONTENT:** Pharmacy deleted successfully.
        - **404 NOT_FOUND:** Pharmacy not found.
        """

        self.get_obj_by_pk(pk).delete()
        return Response({"message": "Pharmacy object deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
