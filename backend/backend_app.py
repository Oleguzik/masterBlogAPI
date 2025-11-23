from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import os
import json

# Get the directory of the current file (backend/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (project root)
project_root = os.path.dirname(current_dir)
# Set the static folder path relative to project root
static_folder = os.path.join(project_root, 'static')

app = Flask(__name__, static_folder=static_folder)
CORS(app)  # This will enable CORS for all routes

# Swagger UI configuration
SWAGGER_URL = "/api/docs"  # Swagger endpoint e.g. HTTP://localhost:5002/api/docs
API_URL = "/static/masterblog.json"  # Ensure you create this dir and file

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Masterblog API'  # You can change this if you like
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# JSON file path for persistent storage
POSTS_FILE = os.path.join(os.path.dirname(__file__), 'posts.json')

# Default posts data
DEFAULT_POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

def load_posts():
    """Load posts from JSON file. Create file with default data if it doesn't exist."""
    try:
        if os.path.exists(POSTS_FILE):
            with open(POSTS_FILE, 'r', encoding='utf-8') as file:
                posts = json.load(file)
                return posts
        else:
            # File doesn't exist, create it with default data
            save_posts(DEFAULT_POSTS)
            return DEFAULT_POSTS.copy()
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {POSTS_FILE}: {e}")
        print("Using default posts data.")
        return DEFAULT_POSTS.copy()
    except Exception as e:
        print(f"Error loading posts: {e}")
        return DEFAULT_POSTS.copy()

def save_posts(posts):
    """Save posts to JSON file with error handling."""
    try:
        with open(POSTS_FILE, 'w', encoding='utf-8') as file:
            json.dump(posts, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving posts to {POSTS_FILE}: {e}")
        raise

def get_next_id(posts):
    """Generate the next available ID for a new post."""
    if not posts:
        return 1
    return max(post['id'] for post in posts) + 1


@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Get query parameters for sorting
    sort_by = request.args.get('sort')
    direction = request.args.get('direction')
    
    # Validate sort parameter if provided
    if sort_by and sort_by not in ['title', 'content']:
        return jsonify({"error": "Invalid sort field. Must be 'title' or 'content'"}), 400
    
    # Validate direction parameter if provided
    if direction and direction not in ['asc', 'desc']:
        return jsonify({"error": "Invalid direction. Must be 'asc' or 'desc'"}), 400
    
    # Load posts from file
    posts = load_posts()
    
    # If no sorting parameters provided, return posts in original order
    if not sort_by:
        return jsonify(posts)
    
    # Create a copy of posts to sort
    sorted_posts = posts.copy()
    
    # Sort the posts
    reverse = direction == 'desc'
    sorted_posts.sort(key=lambda post: post[sort_by].lower(), reverse=reverse)
    
    return jsonify(sorted_posts)


@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Both 'title' and 'content' are required"}), 400
    
    title = data['title'].strip()
    content = data['content'].strip()
    
    if not title or not content:
        return jsonify({"error": "Both 'title' and 'content' must be non-empty"}), 400
    
    # Load current posts
    posts = load_posts()
    
    # Generate new unique ID
    new_id = get_next_id(posts)
    
    new_post = {
        "id": new_id,
        "title": title,
        "content": content
    }
    
    # Add new post and save to file
    posts.append(new_post)
    try:
        save_posts(posts)
    except Exception as e:
        return jsonify({"error": "Failed to save post"}), 500
    
    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    # Load current posts
    posts = load_posts()
    
    # Find the post with the given ID
    post_to_delete = None
    for post in posts:
        if post['id'] == post_id:
            post_to_delete = post
            break
    
    if post_to_delete is None:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404
    
    # Remove the post from the list
    posts.remove(post_to_delete)
    
    # Save updated posts to file
    try:
        save_posts(posts)
    except Exception as e:
        return jsonify({"error": "Failed to delete post"}), 500
    
    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Load current posts
    posts = load_posts()
    
    # Find the post with the given ID
    post_to_update = None
    for post in posts:
        if post['id'] == post_id:
            post_to_update = post
            break
    
    if post_to_update is None:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404
    
    # Get the update data
    data = request.get_json()
    
    # Update only the provided fields
    if data:
        if 'title' in data:
            title = data['title'].strip()
            if title:  # Only update if not empty
                post_to_update['title'] = title
        
        if 'content' in data:
            content = data['content'].strip()
            if content:  # Only update if not empty
                post_to_update['content'] = content
    
    # Save updated posts to file
    try:
        save_posts(posts)
    except Exception as e:
        return jsonify({"error": "Failed to update post"}), 500
    
    return jsonify(post_to_update), 200


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    # Get query parameters
    title_query = request.args.get('title', '').strip().lower()
    content_query = request.args.get('content', '').strip().lower()
    
    # If no search terms provided, return empty list
    if not title_query and not content_query:
        return jsonify([])
    
    # Load posts from file
    posts = load_posts()
    
    # Filter posts that match the search criteria
    matching_posts = []
    for post in posts:
        title_match = title_query and title_query in post['title'].lower()
        content_match = content_query and content_query in post['content'].lower()
        
        # Include post if it matches either title or content (or both)
        if title_match or content_match:
            matching_posts.append(post)
    
    return jsonify(matching_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
