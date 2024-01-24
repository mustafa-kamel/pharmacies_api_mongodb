from factory.django import DjangoModelFactory
from factory.faker import Faker

from pharmacy.models import Pharmacy


class PharmacyFactory(DjangoModelFactory):
    class Meta:
        model = Pharmacy

    name = Faker("company")
    address = Faker("street_address")
    phone_number = Faker("phone_number")
    license_number = Faker("uuid4")
