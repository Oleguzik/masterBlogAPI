from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


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
    
    # If no sorting parameters provided, return posts in original order
    if not sort_by:
        return jsonify(POSTS)
    
    # Create a copy of posts to sort
    sorted_posts = POSTS.copy()
    
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
    
    # Generate new unique ID
    new_id = max(post['id'] for post in POSTS) + 1 if POSTS else 1
    
    new_post = {
        "id": new_id,
        "title": title,
        "content": content
    }
    
    POSTS.append(new_post)
    
    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    # Find the post with the given ID
    post_to_delete = None
    for post in POSTS:
        if post['id'] == post_id:
            post_to_delete = post
            break
    
    if post_to_delete is None:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404
    
    # Remove the post from the list
    POSTS.remove(post_to_delete)
    
    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Find the post with the given ID
    post_to_update = None
    for post in POSTS:
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
    
    return jsonify(post_to_update), 200


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    # Get query parameters
    title_query = request.args.get('title', '').strip().lower()
    content_query = request.args.get('content', '').strip().lower()
    
    # If no search terms provided, return empty list
    if not title_query and not content_query:
        return jsonify([])
    
    # Filter posts that match the search criteria
    matching_posts = []
    for post in POSTS:
        title_match = title_query and title_query in post['title'].lower()
        content_match = content_query and content_query in post['content'].lower()
        
        # Include post if it matches either title or content (or both)
        if title_match or content_match:
            matching_posts.append(post)
    
    return jsonify(matching_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
