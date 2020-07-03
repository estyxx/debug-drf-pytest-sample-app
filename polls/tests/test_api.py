import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestContactAPI(APITestCase):
    def test_post_request_can_create_new_entity(self):
        data = {"question_text": "Hello world?"}

        url = reverse("question-list")
        resp = self.client.post(url, data=data)
        assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_project_create(api_client,):
    data = {"question_text": "Hello world?"}

    url = reverse("question-list")
    resp = api_client.post(url, data, format="json")

    assert resp.status_code == status.HTTP_201_CREATED
