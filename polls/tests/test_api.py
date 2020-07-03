import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase



@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()



class TestDjangoTesting(APITestCase):


    @pytest.mark.xfail
    def test_format_multipart(self):
        data = {"question_text": "Hello world?"}

        url = reverse("question-list")
        resp = self.client.post(url, data=data, format="multipart")

    def test_format_json(self):
        data = {"question_text": "Hello world?"}

        url = reverse("question-list")
        resp = self.client.post(url, data=data, format="json")
        assert resp.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_pytest_json(api_client,):
    data = {"question_text": "Hello world?"}

    url = reverse("question-list")
    resp = api_client.post(url, data, format="json")

    assert resp.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
@pytest.mark.xfail
def test_pytest_multipart(api_client,):
    data = {"question_text": "Hello world?"}

    url = reverse("question-list")
    resp = api_client.post(url, data, format="multipart")

    assert resp.status_code == status.HTTP_201_CREATED
