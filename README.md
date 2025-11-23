# Blog API

A RESTful API for managing blog posts built with Flask and Python, featuring persistent JSON storage and interactive documentation.

## Features

- ✅ Complete CRUD operations for blog posts
- ✅ Search functionality by title or content
- ✅ Sorting by title or content (ascending/descending)
- ✅ CORS support for cross-origin requests
- ✅ Comprehensive error handling and validation
- ✅ Persistent JSON file storage
- ✅ Interactive Swagger UI documentation
- ✅ Client-side rendered web interface

## Project Structure

```
masterBlogAPI/
├── backend/
│   ├── backend_app.py          # Flask API server
│   └── posts.json              # Persistent data storage
├── frontend/
│   ├── frontend_app.py         # Flask frontend server
│   ├── templates/
│   │   └── index.html          # Main web interface
│   └── static/
│       ├── main.js             # Frontend JavaScript
│       └── styles.css          # Styling
├── static/
│   └── masterblog.json         # OpenAPI specification
├── README.md                   # This file
└── .venv/                      # Virtual environment
```

## Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd masterBlogAPI
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-cors flask-swagger-ui
   ```

4. **Start the backend API server**
   ```bash
   python backend/backend_app.py
   ```
   The API will be available at `http://localhost:5002`

5. **Start the frontend server** (in a new terminal)
   ```bash
   source .venv/bin/activate  # Activate venv in new terminal
   python frontend/frontend_app.py
   ```
   The web interface will be available at `http://localhost:5001`

### Access Points
- **Web Interface**: `http://localhost:5001`
- **API Documentation**: `http://localhost:5002/api/docs` (Swagger UI)
- **API Base URL**: `http://localhost:5002/api`

## Data Storage

### Persistent JSON Storage
The API uses a JSON file (`backend/posts.json`) for data persistence:

- **Automatic file creation**: Creates default posts if file doesn't exist
- **Error handling**: Gracefully handles file read/write errors
- **Data integrity**: All CRUD operations update the JSON file
- **Backup friendly**: Easy to backup, restore, or migrate data

### Default Data Structure
```json
[
  {
    "id": 1,
    "author": "Alice Johnson", 
    "title": "The Future of Artificial Intelligence",
    "content": "AI is revolutionizing industries..."
  }
]
```

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

### Prerequisites
- Python 3.9+
- pip (Python package installer)

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd masterBlogAPI
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-cors flask-swagger-ui
   ```

4. **Start the backend API server**
   ```bash
   python backend/backend_app.py
   ```
   The API will be available at `http://localhost:5002`

5. **Start the frontend server** (in a new terminal)
   ```bash
   source .venv/bin/activate  # Activate venv in new terminal
   python frontend/frontend_app.py
   ```
   The web interface will be available at `http://localhost:5001`

### Development Workflow

1. **Backend Development**: Edit `backend/backend_app.py` for API changes
2. **Frontend Development**: Edit files in `frontend/` directory
3. **Data Management**: View/edit `backend/posts.json` for data changes
4. **API Documentation**: Update `static/masterblog.json` for OpenAPI spec

## Usage

### Web Interface
1. Open `http://localhost:5001` in your browser
2. Use the interface to:
   - View all blog posts
   - Add new posts using the form
   - Delete posts with the delete button
   - Posts are automatically loaded from the backend

### API Testing
1. **Swagger UI**: Visit `http://localhost:5002/api/docs` for interactive testing
2. **Command Line**: Use curl for testing endpoints
   ```bash
   # Get all posts
   curl http://localhost:5002/api/posts
   
   # Create a new post
   curl -X POST http://localhost:5002/api/posts \
     -H "Content-Type: application/json" \
     -d '{"title": "My Post", "content": "Post content"}'
   
   # Search posts
   curl "http://localhost:5002/api/posts/search?title=AI"
   ```

## Architecture

### Backend (Port 5002)
- **Flask API**: RESTful endpoints for blog operations
- **JSON Storage**: File-based persistent storage
- **CORS Enabled**: Cross-origin support for frontend
- **Swagger Integration**: Auto-generated API documentation

### Frontend (Port 5001)
- **Flask Server**: Serves static files and templates
- **Client-Side Rendering**: JavaScript handles API communication
- **Responsive Design**: Modern CSS with Poppins font
- **Real-time Updates**: Immediate UI updates after API calls

### Data Flow
```
Frontend (5001) ←→ Backend API (5002) ←→ posts.json
     ↓
User Interface ←→ main.js ←→ REST API ←→ File System
```

## Testing

### Available Testing Methods

1. **Web Interface Testing**
   - Open `http://localhost:5001`
   - Test all CRUD operations through the UI
   - Verify data persistence after server restart

2. **Swagger UI Testing**
   - Visit `http://localhost:5002/api/docs`
   - Interactive API documentation with "Try it out" buttons
   - Test all endpoints with real data

3. **Command Line Testing**
   ```bash
   # Test GET all posts
   curl http://localhost:5002/api/posts
   
   # Test POST (create new post)
   curl -X POST http://localhost:5002/api/posts \
     -H "Content-Type: application/json" \
     -d '{"title": "Test Post", "content": "This is a test"}'
   
   # Test PUT (update post)
   curl -X PUT http://localhost:5002/api/posts/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title"}'
   
   # Test DELETE (remove post)
   curl -X DELETE http://localhost:5002/api/posts/1
   
   # Test search functionality
   curl "http://localhost:5002/api/posts/search?title=AI"
   
   # Test sorting
   curl "http://localhost:5002/api/posts?sort=title&direction=desc"
   ```

4. **Professional Testing Tools**
   - **Postman**: Import OpenAPI spec from `http://localhost:5002/static/masterblog.json`
   - **Thunder Client**: VS Code extension for API testing
   - **Insomnia**: Alternative REST client

### Data Persistence Testing
1. Add posts through the web interface
2. Restart both servers
3. Verify posts are still available (stored in `backend/posts.json`)

## Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill processes on specific ports
lsof -ti:5001 | xargs kill -9  # Frontend port
lsof -ti:5002 | xargs kill -9  # Backend port
```

**Import Errors**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate
pip install flask flask-cors flask-swagger-ui
```

**CORS Errors**
- Ensure both servers are running
- Check that API base URL in frontend is correct: `http://127.0.0.1:5002/api`

**JSON File Issues**
- Check `backend/posts.json` for syntax errors
- Delete the file to regenerate with default data

**Swagger UI Not Loading**
- Verify `static/masterblog.json` exists
- Check backend server logs for file serving errors

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

### Development Guidelines

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow existing code style
   - Update documentation if needed
   - Test your changes thoroughly

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Submit a pull request**
   - Provide clear description of changes
   - Include any breaking changes
   - Reference related issues

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Update OpenAPI spec for API changes

### Testing Requirements
- Test all CRUD operations
- Verify data persistence
- Check error handling
- Test frontend integration

## Technologies Used

### Backend
- **Flask**: Lightweight WSGI web application framework
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **Flask-Swagger-UI**: Interactive API documentation
- **JSON**: File-based data persistence
- **Python 3.9+**: Programming language

### Frontend
- **HTML5**: Modern markup
- **CSS3**: Styling with Flexbox and modern features
- **JavaScript (ES6+)**: Client-side logic
- **Fetch API**: HTTP requests to backend
- **Local Storage**: API URL persistence

### Documentation
- **OpenAPI 3.0**: API specification standard
- **Swagger UI**: Interactive documentation interface
- **Markdown**: README and documentation

## Project Status

### Current Version: 1.0.0

**Completed Features:**
- ✅ Full CRUD API operations
- ✅ JSON file persistence
- ✅ Web interface
- ✅ API documentation
- ✅ Search functionality
- ✅ Sorting capabilities
- ✅ Error handling
- ✅ CORS support

**In Development:**
- 🔄 Pagination system
- 🔄 User authentication
- 🔄 Enhanced data model
- 🔄 Rate limiting

### Roadmap
- **v1.1**: Pagination and advanced filtering
- **v1.2**: User authentication and authorization
- **v1.3**: Comments system and categories
- **v2.0**: Database migration and performance optimization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask community for excellent documentation
- Swagger/OpenAPI for API documentation standards
- Contributors to Flask-CORS and Flask-Swagger-UI packages