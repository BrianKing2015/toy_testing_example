import faker
import requests
import json
from urllib.parse import urljoin
import random
import pytest


URL = "http://127.0.0.1:5000"


@pytest.mark.quick
def test_insert():
    url = urljoin(URL, "artists")
    payload = json.dumps({"first_name": "Stan", "last_name": "Lee", "birth_year": "1922"})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert len(response.text) > 0


@pytest.mark.quick
def test_list_all():
    # Arrange
    url = urljoin(URL, "artists")

    # Act
    response = requests.request("GET", url)

    # Assert
    assert response.status_code == 200
    assert len(response.text) > 0


@pytest.mark.quick
def test_insert_faker():
    # Arrange
    url = urljoin(URL, "artists")
    headers, payload = create_faker_artist()

    # Act
    response = requests.request("POST", url, headers=headers, data=payload)

    # Assert
    assert response.status_code == 200
    assert len(response.text) > 0


@pytest.mark.quick
def test_search_by_id():
    # Arrange
    url = urljoin(URL, "artists")
    headers, payload = create_faker_artist()
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200

    # Act
    search_url = urljoin(URL, f"artists/{response.text.strip()}")
    search_call = requests.request("GET", search_url)
    assert search_call.status_code == 200

    # Assert
    break_open_payload = json.loads(payload)
    first = break_open_payload["first_name"]
    last = break_open_payload["last_name"]
    birth = break_open_payload["birth_year"]
    assert response.status_code == 200
    assert first in search_call.text
    assert last in search_call.text
    assert str(birth) in search_call.text


@pytest.mark.quick
def test_update_artist():
    # Arrange
    create_url = urljoin(URL, "artists")
    headers, payload = create_faker_artist()
    create_call = requests.request("POST", create_url, headers=headers, data=payload)
    assert create_call.status_code == 200

    # Act
    update_url = urljoin(URL, "artists")
    headers, update_payload = create_faker_artist()
    update_payload = json.loads(update_payload)
    update_payload["user_id"] = create_call.text.strip()
    update_payload = json.dumps(update_payload)
    update_call = requests.request("PUT", update_url, headers=headers, data=update_payload)
    assert update_call.status_code == 200

    # Assert
    search_url = urljoin(URL, f"artists/{create_call.text.strip()}")
    search_call = requests.request("GET", search_url)
    assert search_call.status_code == 200

    break_open_payload = json.loads(update_payload)
    first = break_open_payload["first_name"]
    last = break_open_payload["last_name"]
    birth = break_open_payload["birth_year"]
    assert update_call.status_code == 200
    assert first in search_call.text
    assert last in search_call.text
    assert str(birth) in search_call.text


@pytest.mark.quick
def test_delete_artist():
    # Arrange
    create_url = urljoin(URL, "artists")
    headers, payload = create_faker_artist()
    create_call = requests.request("POST", create_url, headers=headers, data=payload)
    assert create_call.status_code == 200

    # Act
    delete_url = urljoin(URL, f"artists/{create_call.text.strip()}")
    delete_response = requests.request("DELETE", delete_url, headers=headers)
    assert delete_response.status_code == 200

    # Assert
    search_url = urljoin(URL, f"artists/{create_call.text.strip()}")
    search_call = requests.request("GET", search_url)
    assert search_call.status_code == 200
    assert "null" in search_call.text


def create_faker_artist():
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_year = random.randint(1850, 2022)
    payload = json.dumps({"first_name": first_name, "last_name": last_name, "birth_year": birth_year})
    headers = {'Content-Type': 'application/json'}
    return headers, payload
