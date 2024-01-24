from django.urls import reverse
from rest_framework import status

from pharmacy.tests.factories.pharmacy_factory import PharmacyFactory

from .authenticated_test_case import AuthenticatedTestCase


class TestPharmacyCreateAPI(AuthenticatedTestCase):
    def test_unauthorized(self):
        """
        Test unauthenticated request.
        """
        url = reverse("pharmacy-list")
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_pharmacy_valid_data(self):
        """
        Test creating a new pharmacy with valid data.
        """
        pharmacy = PharmacyFactory()
        data = pharmacy.__dict__
        data.pop("_state")
        response = self.client.post(reverse("pharmacy-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], pharmacy.name)
        self.assertEqual(response.data["address"], pharmacy.address)
        self.assertEqual(response.data["phone_number"], pharmacy.phone_number)
        self.assertEqual(response.data["license_number"], pharmacy.license_number)

    def test_create_pharmacy_missing_required_field(self):
        """
        Test creating pharmacy with missing required field.
        """
        data = {"name": "New Pharmacy"}
        response = self.client.post(reverse("pharmacy-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual("required", response.data["address"][0].code)
        self.assertIn("required", response.data["address"][0])

    def test_create_pharmacy_max_length_exceeded(self):
        """
        Test creating a new pharmacy with a field exceeding the max length.
        """
        pharmacy = PharmacyFactory()
        data = pharmacy.__dict__
        data.pop("_state")
        data["phone_number"] = data["phone_number"] * 5
        response = self.client.post(reverse("pharmacy-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual("max_length", response.data["phone_number"][0].code)
        self.assertIn("has no more than", response.data["phone_number"][0])
