"""This File is developed by BHASKARA VENKATA RAMANA GARBHAM """
from mastodon import Mastodon

class MastodonService:
    def __init__(self, base_url, access_token):
        self.mastodon = Mastodon(api_base_url=base_url, access_token=access_token)

    def create_post(self, content):
        """Creates a post on Mastodon."""
        post = self.mastodon.status_post(content)
        return post['id']

    def retrieve_post(self, post_id):
        """Retrieves a post using its ID."""
        post = self.mastodon.status(post_id)
        return post['content']

    def delete_post(self, post_id):
        """Deletes a post."""
        self.mastodon.status_delete(post_id)
