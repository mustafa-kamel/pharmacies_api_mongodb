from base64 import b64encode

from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticatedTestCase(APITestCase):
    username = "test_user"
    password = "test_password"

    def setUp(self):
        super().setUp()
        User.objects.create_user(username=self.username, password=self.password)
        self.auth_header = "Basic {}".format(
            b64encode(f"{self.username}:{self.password}".encode("utf-8")).decode("utf-8")
        )
        self.set_authorized_client()

    def set_authorized_client(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
