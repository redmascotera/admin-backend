"""Tests for Pet ViewSets"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app import models


class PetTests(TestCase):
    """Test Pet Viewsets"""

    def setUp(self):
        self.client = APIClient()
        self.owner = models.Owner.objects.create(name="John")
        self.pet_data = {"name": "Buddy", "owner_id": self.owner.id}
        self.pet = models.Pet.objects.create(**self.pet_data)
        self.url = reverse("pets-list")

    def test_create_pet(self):
        response = self.client.post(self.url, self.pet_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pets(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pet_detail(self):
        url_detail = reverse("pets-detail", args=[self.pet.id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pet(self):
        url_detail = reverse("pets-detail", args=[self.pet.id])
        updated_data = {"name": "Updated Buddy", "owner_id": self.owner.id}
        response = self.client.put(url_detail, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pet.refresh_from_db()
        self.assertEqual(self.pet.name, "Updated Buddy")

    def test_delete_pet(self):
        url_detail = reverse("pets-detail", args=[self.pet.id])
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Pet.objects.filter(id=self.pet.id).exists())


class PetTagTests(TestCase):
    """Test Pet Tag Viewsets"""

    def setUp(self):
        self.client = APIClient()
        self.pet = models.Pet.objects.create(name="Fluffy")
        self.pet_tag_data = {"pet_id": self.pet.id, "tag": "Fluffy's Tag", "code": "12345"}
        self.pet_tag = models.PetTag.objects.create(**self.pet_tag_data)
        self.url = reverse("pet_tags-list")

    def test_create_pet_tag(self):
        response = self.client.post(self.url, self.pet_tag_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pet_tags(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pet_tag_detail(self):
        url_detail = reverse("pet_tags-detail", args=[self.pet_tag.id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pet_tag(self):
        url_detail = reverse("pet_tags-detail", args=[self.pet_tag.id])
        updated_data = {"pet_id": self.pet.id, "tag": "Updated Tag", "code": "54321"}
        response = self.client.put(url_detail, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pet_tag.refresh_from_db()
        self.assertEqual(self.pet_tag.tag, "Updated Tag")

    def test_delete_pet_tag(self):
        url_detail = reverse("pet_tags-detail", args=[self.pet_tag.id])
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.PetTag.objects.filter(id=self.pet_tag.id).exists())
