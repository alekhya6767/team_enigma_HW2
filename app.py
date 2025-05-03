""" This File is developed by VIJAYA SHARAVAN REDDY BADDAM(018321342) """

# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for, flash
# Import the MastodonService class for interacting with the Mastodon API
from mastodon_service import MastodonService

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for the application, required for using Flask's session and flash features
app.secret_key = 'some_random_secret_key'  # Needed for flashing messages

# Define the base URL and access token for the Mastodon API
BASE_URL = "https://mastodon.social"
ACCESS_TOKEN = "10Uo8BHyflZ9Aa8bV50-xYaLJZiH7mW9mDaLkuvUfzc"

# Create an instance of the MastodonService class to handle API interactions
mastodon_service = MastodonService(BASE_URL, ACCESS_TOKEN)

# Global variable to store the ID of the latest post created
latest_post_id = None

# Define the main route for the application, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the main functionality of the application:
    - Create a new post
    - Retrieve the latest post
    - Delete the latest post
    """
    global latest_post_id  # Access the global variable to track the latest post ID
    post_content = None  # Variable to store the content of the retrieved post

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Handle the "Create Post" functionality
        if 'create' in request.form:
            content = request.form['content']  # Get the content of the post from the form
            post_id = mastodon_service.create_post(content)  # Call the Mastodon API to create the post
            if post_id:  # If the post was created successfully
                latest_post_id = post_id  # Update the global variable with the new post ID
                flash("Post created successfully!", "success")  # Show a success message
            else:  # If the post creation failed
                flash("Failed to create post. Check input or try again later.", "danger")  # Show an error message

        # Handle the "Retrieve Post" functionality
        elif 'retrieve' in request.form and latest_post_id:
            post_content = mastodon_service.retrieve_post(latest_post_id)  # Retrieve the latest post content
            flash("Post retrieved.", "info")  # Show an informational message

        # Handle the "Delete Post" functionality
        elif 'delete' in request.form and latest_post_id:
            mastodon_service.delete_post(latest_post_id)  # Delete the latest post using the Mastodon API
            latest_post_id = None  # Reset the global variable as the post is deleted
            post_content = None  # Clear the post content
            flash("Post deleted.", "warning")  # Show a warning message

    # Render the index1.html template and pass the latest post ID and content to it
    return render_template('index1.html', post_id=latest_post_id, post_content=post_content)

# Entry point of the application
if __name__ == '__main__':
    # Run the Flask application in debug mode for easier development and debugging
    app.run(debug=True)