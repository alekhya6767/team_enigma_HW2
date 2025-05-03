"""This file is developed by JAYANTH SAI YARLAGADDA(018291819)"""

# Import pytest for testing and requests_mock for mocking HTTP requests
import pytest
import requests_mock
from mastodon_service import MastodonService  # Import the MastodonService class to test

# Define constants for the base URL and access token used in the tests
BASE_URL = "https://mastodon.social"
ACCESS_TOKEN = "10Uo8BHyflZ9Aa8bV50-xYaLJZiH7mW9mDaLkuvUfzc"

# Define a pytest fixture to create an instance of MastodonService
@pytest.fixture
def mastodon_service():
    """
    Fixture to provide a MastodonService instance for testing.
    This ensures a consistent setup for all tests.
    """
    return MastodonService(BASE_URL, ACCESS_TOKEN)

# Test the create_post method of MastodonService
def test_create_post(mastodon_service):
    """
    Test the create_post method to ensure it successfully creates a post.

    Steps:
    - Mock the POST request to the Mastodon API.
    - Call the create_post method with sample content.
    - Assert that the returned post ID matches the expected value.
    """
    with requests_mock.Mocker() as mock:
        # Mock the API endpoint for creating a post
        mock.post(f"{BASE_URL}/api/v1/statuses", json={"id": "12345"})
        
        # Call the create_post method with sample content
        post_id = mastodon_service.create_post("Hello, Mastodon!")
        
        # Assert that the returned post ID is as expected
        assert post_id == "12345"

# Test the retrieve_post method of MastodonService
def test_retrieve_post(mastodon_service):
    """
    Test the retrieve_post method to ensure it retrieves the correct post content.

    Steps:
    - Mock the GET request to the Mastodon API.
    - Call the retrieve_post method with a sample post ID.
    - Assert that the returned content matches the expected value.
    """
    with requests_mock.Mocker() as mock:
        # Mock the API endpoint for retrieving a post
        mock.get(f"{BASE_URL}/api/v1/statuses/12345", json={"content": "Hello, Mastodon!"})
        
        # Call the retrieve_post method with a sample post ID
        content = mastodon_service.retrieve_post("12345")
        
        # Assert that the returned content is as expected
        assert content == "Hello, Mastodon!"

# Test the delete_post method of MastodonService
def test_delete_post(mastodon_service):
    """
    Test the delete_post method to ensure it successfully deletes a post.

    Steps:
    - Create a post using the create_post method.
    - Mock the DELETE request to the Mastodon API.
    - Call the delete_post method with the created post ID.
    - Assert that the response is None (indicating successful deletion).
    """
    # Create a post to get a post ID for deletion
    post_id = mastodon_service.create_post("Test post for deletion")

    # Debugging: Print the post ID to verify it was created
    print(f"Post ID to delete: {post_id}")

    # Mock the DELETE request to the Mastodon API
    with requests_mock.Mocker() as mock:
        mock.delete(f"{BASE_URL}/api/v1/statuses/{post_id}", status_code=200)
        
        # Call the delete_post method with the created post ID
        response = mastodon_service.delete_post(post_id)

        # Debugging: Print the response to verify the deletion
        print(f"Delete response: {response}")

        # Assert that the response is None (indicating successful deletion)
        assert response is None