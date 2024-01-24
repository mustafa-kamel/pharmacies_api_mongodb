from django.urls import reverse
from rest_framework import status

from pharmacy.tests.factories.pharmacy_factory import PharmacyFactory

from .authenticated_test_case import AuthenticatedTestCase


class TestPharmacyUpdateAPI(AuthenticatedTestCase):
    def test_unauthorized(self):
        """
        Test unauthenticated request.
        """
        pharmacy = PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_pharmacy_valid_data(self):
        """
        Test updating existing pharmacy with valid data using factory.
        """
        pharmacy = PharmacyFactory()
        data = {"name": "Updated Pharmacy"}

        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])

    def test_update_pharmacy_max_length_exceeded(self):
        """
        Test updating a new pharmacy with a field exceeding the max length.
        """
        pharmacy = PharmacyFactory()
        data = pharmacy.__dict__
        data.pop("_state")
        data["phone_number"] = data["phone_number"] * 5
        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual("max_length", response.data["phone_number"][0].code)
        self.assertIn("has no more than", response.data["phone_number"][0])
