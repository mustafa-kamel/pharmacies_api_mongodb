from django.urls import reverse
from rest_framework import status

from pharmacy.tests.factories.pharmacy_factory import PharmacyFactory

from .authenticated_test_case import AuthenticatedTestCase


class TestPharmacyDeleteAPI(AuthenticatedTestCase):
    def test_unauthorized(self):
        """
        Test unauthenticated request.
        """
        pharmacy = PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_pharmacy_existing_pk(self):
        """
        Test deleting pharmacy with valid primary key from factory.
        """
        pharmacy = PharmacyFactory()
        url = reverse("pharmacy-detail", kwargs={"pk": pharmacy.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_pharmacy_invalid_pk(self):
        """
        Test deleting pharmacy with non-existent primary key.
        """
        url = reverse("pharmacy-detail", kwargs={"pk": 999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_pharmacy_negative_pk(self):
        """
        Test deleting pharmacy with invalid negative primary key.
        """
        url = reverse("pharmacy-detail", kwargs={"pk": -1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
