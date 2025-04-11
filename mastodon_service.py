"""This File is developed by BHASKARA VENKATA RAMANA GARBHAM(018198674) """
from mastodon import Mastodon, MastodonError, MastodonAPIError, MastodonNotFoundError

class MastodonService:
    def __init__(self, base_url, access_token):
        self.mastodon = Mastodon(api_base_url=base_url, access_token=access_token)

        def create_post(self, content):
        """Creates a post on Mastodon."""
        try:
            if not content.strip():
                raise ValueError("Post content cannot be empty.")
            post = self.mastodon.status_post(content)
            return post['id']
        except MastodonRatelimitError as e:
            reset_time = self.mastodon.ratelimit_reset
            wait_time = reset_time - time.time() if reset_time else 60
            print(f"Rate limit hit. Try again in {int(wait_time)} seconds.")
            return None
        except (MastodonAPIError, MastodonError, ValueError) as e:
            print(f"Error creating post: {e}")
            return None

    def retrieve_post(self, post_id):
        """Retrieves a post using its ID."""
        try:
            post = self.mastodon.status(post_id)
            return post['content']
        except MastodonRatelimitError as e:
            print("Rate limit exceeded while retrieving post.")
            return "Rate limit exceeded. Try again later."
        except MastodonNotFoundError:
            return "Post not found."
        except MastodonError as e:
            return "Error retrieving post."

    def delete_post(self, post_id):
        """Deletes a post."""
        try:
            self.mastodon.status_delete(post_id)
        except MastodonRatelimitError:
            print("Rate limit exceeded while deleting post.")
        except MastodonNotFoundError:
            print(f"Post with ID {post_id} not found for deletion.")
        except MastodonError as e:
            print(f"Error deleting post: {e}")


