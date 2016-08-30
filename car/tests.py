import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import carName, Manufacturer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_carname(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["Manufacturer"] = "Manufacturer"
    defaults["Price"] = "Price"
    defaults["mileage"] = "mileage"
    defaults["engine"] = "engine"
    defaults["power"] = "power"
    defaults["description"] = "description"
    defaults["cardheko"] = "cardheko"
    defaults["cartrade"] = "cartrade"
    defaults["youtubeurl"] = "youtubeurl"
    defaults["imageUrl"] = "imageUrl"
    defaults.update(**kwargs)
    return carName.objects.create(**defaults)


def create_manufacturer(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Manufacturer.objects.create(**defaults)


class carNameViewTest(unittest.TestCase):
    '''
    Tests for carName
    '''
    def setUp(self):
        self.client = Client()

    def test_list_carname(self):
        url = reverse('car_carname_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_carname(self):
        url = reverse('car_carname_create')
        data = {
            "name": "name",
            "Manufacturer": "Manufacturer",
            "Price": "Price",
            "mileage": "mileage",
            "engine": "engine",
            "power": "power",
            "description": "description",
            "cardheko": "cardheko",
            "cartrade": "cartrade",
            "youtubeurl": "youtubeurl",
            "imageUrl": "imageUrl",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_carname(self):
        carname = create_carname()
        url = reverse('car_carname_detail', args=[carname.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_carname(self):
        carname = create_carname()
        data = {
            "name": "name",
            "Manufacturer": "Manufacturer",
            "Price": "Price",
            "mileage": "mileage",
            "engine": "engine",
            "power": "power",
            "description": "description",
            "cardheko": "cardheko",
            "cartrade": "cartrade",
            "youtubeurl": "youtubeurl",
            "imageUrl": "imageUrl",
        }
        url = reverse('car_carname_update', args=[carname.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ManufacturerViewTest(unittest.TestCase):
    '''
    Tests for Manufacturer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_manufacturer(self):
        url = reverse('car_manufacturer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_manufacturer(self):
        url = reverse('car_manufacturer_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_manufacturer(self):
        manufacturer = create_manufacturer()
        url = reverse('car_manufacturer_detail', args=[manufacturer.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_manufacturer(self):
        manufacturer = create_manufacturer()
        data = {
            "name": "name",
        }
        url = reverse('car_manufacturer_update', args=[manufacturer.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


