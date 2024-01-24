from django.urls import reverse
from rest_framework import status

from pharmacy.tests.factories.pharmacy_factory import PharmacyFactory

from .authenticated_test_case import AuthenticatedTestCase


class TestPharmacyListAPI(AuthenticatedTestCase):
    def test_unauthorized(self):
        """
        Test unauthenticated request.
        """
        url = reverse("pharmacy-list")
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_pharmacies(self):
        """
        Test retrieving all pharmacies.
        """
        factories = [PharmacyFactory() for _ in range(3)]
        url = reverse("pharmacy-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), len(factories))

    def test_empty_result(self):
        """
        Test empty result when no pharmacies match the filter.
        """
        url = reverse("pharmacy-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 0)

    def test_filter_by_name(self):
        """
        Test filtering pharmacies by name.
        """
        pharmacy_name = "Test Pharmacy"
        PharmacyFactory(name=pharmacy_name)
        url = reverse("pharmacy-list") + f"?name={pharmacy_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], pharmacy_name)

    def test_get_pharmacy_by_unique_name(self):
        """
        Test retrieving pharmacy by unique name.
        """
        unique_name = "Unique Pharmacy Name"
        pharmacy = PharmacyFactory(name=unique_name)
        url = reverse("pharmacy-list") + f"?name={unique_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["id"], pharmacy.pk)
        self.assertEqual(response.data["results"][0]["name"], unique_name)
        self.assertEqual(response.data["results"][0]["address"], pharmacy.address)
        self.assertEqual(response.data["results"][0]["phone_number"], pharmacy.phone_number)
        self.assertEqual(response.data["results"][0]["license_number"], pharmacy.license_number)

    def test_get_pharmacies_by_common_name(self):
        """
        Test retrieving pharmacies with a common name (multiple matches).
        """
        common_name = "Common Pharmacy"
        factories = [PharmacyFactory(name=common_name) for _ in range(3)]
        url = reverse("pharmacy-list") + f"?name={common_name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), len(factories))
        self.assertEqual(response.data["results"][0]["name"], common_name)
        self.assertEqual(response.data["results"][1]["name"], common_name)
