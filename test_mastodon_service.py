"""This file is developed by JAYANTH SAI YARLAGADDA(018291819)"""
import pytest
import requests_mock
from mastodon_service import MastodonService

BASE_URL = "https://mastodon.social"
ACCESS_TOKEN = "10Uo8BHyflZ9Aa8bV50-xYaLJZiH7mW9mDaLkuvUfzc"

@pytest.fixture
def mastodon_service():
    return MastodonService(BASE_URL, ACCESS_TOKEN)

def test_create_post(mastodon_service):
    with requests_mock.Mocker() as mock:
        mock.post(f"{BASE_URL}/api/v1/statuses", json={"id": "12345"})
        post_id = mastodon_service.create_post("Hello, Mastodon!")
        assert post_id == "12345"

def test_retrieve_post(mastodon_service):
    with requests_mock.Mocker() as mock:
        mock.get(f"{BASE_URL}/api/v1/statuses/12345", json={"content": "Hello, Mastodon!"})
        content = mastodon_service.retrieve_post("12345")
        assert content == "Hello, Mastodon!"


def test_delete_post(mastodon_service):
    post_id = mastodon_service.create_post("Test post for deletion")

    # Print the response before deletion
    print(f"Post ID to delete: {post_id}")

    response = mastodon_service.delete_post(post_id)

    # Debugging: Check if response is None or unexpected
    print(f"Delete response: {response}")

    assert response is None  # Deleting a post typically returns an empty response

