"""This File is developed by BHASKARA VENKATA RAMANA GARBHAM(018198674) """

# Import necessary modules from the Mastodon library
from mastodon import Mastodon, MastodonError, MastodonAPIError, MastodonNotFoundError

class MastodonService:
    """
    A service class to interact with the Mastodon API.
    Provides methods to create, retrieve, and delete posts.
    """

    def __init__(self, base_url, access_token):
        """
        Initializes the MastodonService instance with the given base URL and access token.
        
        Args:
            base_url (str): The base URL of the Mastodon instance.
            access_token (str): The access token for authenticating API requests.
        """
        self.mastodon = Mastodon(api_base_url=base_url, access_token=access_token)

    def create_post(self, content):
        """
        Creates a post on Mastodon.

        Args:
            content (str): The content of the post to be created.

        Returns:
            str: The ID of the created post if successful, or None if an error occurs.
        """
        try:
            # Ensure the content is not empty or just whitespace
            if not content.strip():
                raise ValueError("Post content cannot be empty.")
            
            # Use the Mastodon API to create a new post
            post = self.mastodon.status_post(content)
            return post['id']  # Return the ID of the created post

        except MastodonRatelimitError as e:
            # Handle rate-limiting errors by calculating the wait time
            reset_time = self.mastodon.ratelimit_reset
            wait_time = reset_time - time.time() if reset_time else 60
            print(f"Rate limit hit. Try again in {int(wait_time)} seconds.")
            return None

        except (MastodonAPIError, MastodonError, ValueError) as e:
            # Handle other API or validation errors
            print(f"Error creating post: {e}")
            return None

    def retrieve_post(self, post_id):
        """
        Retrieves a post using its ID.

        Args:
            post_id (str): The ID of the post to retrieve.

        Returns:
            str: The content of the retrieved post, or an error message if retrieval fails.
        """
        try:
            # Use the Mastodon API to retrieve the post by its ID
            post = self.mastodon.status(post_id)
            return post['content']  # Return the content of the retrieved post

        except MastodonRatelimitError as e:
            # Handle rate-limiting errors
            print("Rate limit exceeded while retrieving post.")
            return "Rate limit exceeded. Try again later."

        except MastodonNotFoundError:
            # Handle cases where the post is not found
            return "Post not found."

        except MastodonError as e:
            # Handle other API errors
            return "Error retrieving post."

    def delete_post(self, post_id):
        """
        Deletes a post.

        Args:
            post_id (str): The ID of the post to delete.

        Returns:
            None
        """
        try:
            # Use the Mastodon API to delete the post by its ID
            self.mastodon.status_delete(post_id)

        except MastodonRatelimitError:
            # Handle rate-limiting errors
            print("Rate limit exceeded while deleting post.")

        except MastodonNotFoundError:
            # Handle cases where the post is not found
            print(f"Post with ID {post_id} not found for deletion.")

        except MastodonError as e:
            # Handle other API errors
            print(f"Error deleting post: {e}")