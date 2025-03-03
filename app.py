""" This File is developed by VIJAYA SHARAVAN REDDY BADDAM(018321342)"""
from flask import Flask, render_template, request, redirect, url_for
from mastodon_service import MastodonService

app = Flask(__name__)

# Replace with your Mastodon instance and access token
BASE_URL = "https://mastodon.social"
ACCESS_TOKEN = "10Uo8BHyflZ9Aa8bV50-xYaLJZiH7mW9mDaLkuvUfzc"

mastodon_service = MastodonService(BASE_URL, ACCESS_TOKEN)

# Store the latest post ID for retrieval
latest_post_id = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global latest_post_id
    post_content = None

    if request.method == 'POST':
        if 'create' in request.form:
            content = request.form['content']
            latest_post_id = mastodon_service.create_post(content)

        elif 'retrieve' in request.form and latest_post_id:
            post_content = mastodon_service.retrieve_post(latest_post_id)

        elif 'delete' in request.form and latest_post_id:
            mastodon_service.delete_post(latest_post_id)
            latest_post_id = None
            post_content = None

    return render_template('index1.html', post_id=latest_post_id, post_content=post_content)


if __name__ == '__main__':
    app.run(debug=True)
