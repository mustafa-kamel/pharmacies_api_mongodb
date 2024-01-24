from django.urls import reverse
from rest_framework import status

from pharmacy.tests.factories.pharmacy_factory import PharmacyFactory

from .authenticated_test_case import AuthenticatedTestCase


class TestPharmacyRetrieveAPI(AuthenticatedTestCase):
    def test_unauthorized(self):
        """
        Test unauthenticated request.
        """
        pharmacy = PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_pharmacy_by_pk(self):
        """
        Test retrieving pharmacy by primary key.
        """
        pharmacy = PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], pharmacy.pk)
        self.assertEqual(response.data["name"], pharmacy.name)
        self.assertEqual(response.data["address"], pharmacy.address)
        self.assertEqual(response.data["phone_number"], pharmacy.phone_number)
        self.assertEqual(response.data["license_number"], pharmacy.license_number)

    def test_get_pharmacy_invalid_pk(self):
        """
        Test retrieving pharmacy by invalid negative primary key.
        """
        PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": -1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_pharmacy_str_pk(self):
        """
        Test retrieving pharmacy by invalid string primary key.
        """
        PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": "abcdef"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
