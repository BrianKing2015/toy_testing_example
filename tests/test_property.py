import json
from urllib.parse import urljoin

import pytest
import requests
from hypothesis import given, settings, example
from hypothesis.strategies import text, characters

from test_faker import create_faker_artist


URL = "http://127.0.0.1:5000"


@pytest.mark.property_based
@given(test_first=text(
    alphabet=characters(min_codepoint=32, max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size=0, max_size=30))
@example("Stan")
@settings(max_examples=10, deadline=500)
def test_first_name(test_first):
    insert_artist(first_name=test_first)


@pytest.mark.property_based
@given(test_last=text(
    alphabet=characters(min_codepoint=32, max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size=0, max_size=30))
@example("Lee")
@settings(max_examples=10, deadline=500)
def test_last_name(test_last):
    insert_artist(last_name=test_last)


def insert_artist(first_name=None, last_name=None):
    url = urljoin(URL, "artists")
    headers, payload = create_faker_artist()
    break_open_payload = json.loads(payload)

    if first_name is not None:
        break_open_payload["first_name"] = first_name
    if last_name is not None:
        break_open_payload["last_name"] = last_name

    payload = json.dumps(break_open_payload)
    requests.request("POST", url, headers=headers, data=payload)
