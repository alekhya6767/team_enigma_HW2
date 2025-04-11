""" This File is developed by VIJAYA SHARAVAN REDDY BADDAM(018321342)"""
from flask import Flask, render_template, request, redirect, url_for, flash
from mastodon_service import MastodonService

app = Flask(__name__)
app.secret_key = 'some_random_secret_key'  # Needed for flashing messages

BASE_URL = "https://mastodon.social"
ACCESS_TOKEN = "10Uo8BHyflZ9Aa8bV50-xYaLJZiH7mW9mDaLkuvUfzc"

mastodon_service = MastodonService(BASE_URL, ACCESS_TOKEN)
latest_post_id = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global latest_post_id
    post_content = None

    if request.method == 'POST':
        if 'create' in request.form:
            content = request.form['content']
            post_id = mastodon_service.create_post(content)
            if post_id:
                latest_post_id = post_id
                flash("Post created successfully!", "success")
            else:
                flash("Failed to create post. Check input or try again later.", "danger")

        elif 'retrieve' in request.form and latest_post_id:
            post_content = mastodon_service.retrieve_post(latest_post_id)
            flash("Post retrieved.", "info")

        elif 'delete' in request.form and latest_post_id:
            mastodon_service.delete_post(latest_post_id)
            latest_post_id = None
            post_content = None
            flash("Post deleted.", "warning")

    return render_template('index1.html', post_id=latest_post_id, post_content=post_content)

if __name__ == '__main__':
    app.run(debug=True)

