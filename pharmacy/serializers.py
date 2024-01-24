from rest_framework import serializers

from .models import Pharmacy


class PharmacySerializer(serializers.ModelSerializer):
    """Serializer for Pharmacy objects.

    **Fields:**

    - id (integer): Primary key.
    - name (string): Name of the pharmacy.
    - address (string): Address of the pharmacy.
    - phone_number (string): Phone number of the pharmacy.
    - license_number (string): License number of the pharmacy.
    """

    class Meta:
        model = Pharmacy
        fields = "__all__"
