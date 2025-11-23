# Blog API

A RESTful API for managing blog posts built with Flask and Python.

## Features

- ✅ Complete CRUD operations for blog posts
- ✅ Search functionality by title or content
- ✅ Sorting by title or content (ascending/descending)
- ✅ CORS support for cross-origin requests
- ✅ Comprehensive error handling and validation

## API Endpoints

### List Posts
**GET** `/api/posts`

Returns all blog posts. Supports optional sorting parameters.

**Query Parameters:**
- `sort` (optional): Sort by field (`title` or `content`)
- `direction` (optional): Sort direction (`asc` or `desc`)

**Examples:**
- `GET /api/posts` - Returns all posts in original order
- `GET /api/posts?sort=title&direction=asc` - Sort by title ascending
- `GET /api/posts?sort=content&direction=desc` - Sort by content descending

**Response:** Array of post objects

### Create Post
**POST** `/api/posts`

Creates a new blog post.

**Request Body:**
```json
{
  "title": "Post Title",
  "content": "Post content here..."
}
```

**Response:** Created post object with generated ID (201 Created)

### Get Single Post
**GET** `/api/posts/<id>`

Returns a single post by ID.

**Response:** Post object or 404 if not found

### Update Post
**PUT** `/api/posts/<id>`

Updates an existing post. Only provided fields will be updated.

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content..."
}
```

**Response:** Updated post object (200 OK) or 404 if not found

### Delete Post
**DELETE** `/api/posts/<id>`

Deletes a post by ID.

**Response:** Success message (200 OK) or 404 if not found

### Search Posts
**GET** `/api/posts/search`

Searches posts by title or content.

**Query Parameters:**
- `title` (optional): Search term for title
- `content` (optional): Search term for content

**Examples:**
- `GET /api/posts/search?title=flask` - Find posts with "flask" in title
- `GET /api/posts/search?content=python` - Find posts with "python" in content
- `GET /api/posts/search?title=web&content=app` - Find posts with both terms

**Response:** Array of matching post objects

## Data Model

### Post
```json
{
  "id": 1,
  "title": "Post Title",
  "content": "Post content..."
}
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- **400 Bad Request**: Invalid request data or parameters
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

Error response format:
```json
{
  "error": "Error message description"
}
```

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `pip install flask flask-cors`
5. Run the application: `python backend/backend_app.py`

The API will be available at `http://localhost:5002`

## Testing

You can test the API using tools like:
- curl
- Postman
- Thunder Client (VS Code extension)
- Your frontend application

## Future Features

### 🔄 Pagination
Implement pagination to handle large numbers of posts efficiently.

**Planned Features:**
- `limit` parameter to specify number of posts per page
- `offset` or `page` parameter for navigation
- Response metadata with total count and pagination info

**Example:** `GET /api/posts?page=2&limit=10`

### 📊 Expanded Data Model
Enhance the data model with additional features:

**Comments System:**
- Add comments to posts
- Nested comment threads
- Comment moderation

**Categories and Tags:**
- Organize posts by categories
- Tag posts with keywords
- Filter posts by category/tag

**Enhanced Post Model:**
```json
{
  "id": 1,
  "title": "Post Title",
  "content": "Post content...",
  "category": "Technology",
  "tags": ["python", "flask", "api"],
  "created_at": "2025-11-23T10:00:00Z",
  "updated_at": "2025-11-23T10:00:00Z",
  "author": "user_id",
  "comments": [...]
}
```

### 🔐 User Authorization
Implement user authentication and authorization system.

**Planned Features:**
- User registration and login endpoints
- JWT token-based authentication
- Role-based access control (admin, author, reader)
- Protected routes for create/update/delete operations

**New Endpoints:**
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update user profile

### 🛡️ Rate Limiting and API Versioning
Protect the API and prepare for future changes.

**Rate Limiting:**
- Limit requests per user/IP
- Different limits for different endpoints
- Graceful handling of rate limit exceeded

**API Versioning:**
- Versioned endpoints (e.g., `/api/v1/posts`)
- Backward compatibility
- Deprecation notices for old versions

**Example Versioned Endpoints:**
- `/api/v1/posts` (current version)
- `/api/v2/posts` (future enhanced version)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.