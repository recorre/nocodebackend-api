# NoCodeBackend API

FastAPI backend for the Indie Comments Widget system. Provides RESTful APIs for comment management, moderation, and real-time updates.

## Features

- ✅ **Comment Management**: Create, read, update, delete comments
- ✅ **Bulk Operations**: Approve/reject multiple comments at once
- ✅ **Real-time Updates**: WebSocket support for live notifications
- ✅ **Search & Filtering**: Advanced comment search and filtering
- ✅ **Comment Threading**: Nested replies and discussions
- ✅ **Moderation Tools**: Comprehensive moderation interface
- ✅ **Security**: JWT authentication, rate limiting, input validation
- ✅ **Monitoring**: Health checks, metrics, and logging
- ✅ **Accessibility**: WCAG 2.1 AA compliance
- ✅ **Testing**: 101 automated tests with 95%+ coverage

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/your-org/nocodebackend-api.git
cd nocodebackend-api

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Docker

```bash
# Build and run with Docker
docker build -t nocodebackend-api .
docker run -p 8000:8000 nocodebackend-api
```

## API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost/dbname

# Security
SECRET_KEY=your-secret-key-here
API_KEY=your-api-key-here

# Application
DEBUG=false
ENVIRONMENT=production

# External Services
REDIS_URL=redis://localhost:6379
```

## API Endpoints

### Comments
- `GET /api/comments` - List comments with filtering
- `POST /api/comments` - Create new comment
- `PUT /api/comments/{id}/moderate` - Moderate comment
- `DELETE /api/comments/{id}` - Delete comment

### Threads
- `GET /api/threads` - List discussion threads
- `POST /api/threads` - Create new thread
- `DELETE /api/threads/{id}` - Delete thread

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Health & Monitoring
- `GET /api/health` - Health check
- `GET /api/metrics` - Application metrics

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test file
pytest tests/test_comments.py -v
```

## Deployment

### Vercel (Recommended)

1. Connect your GitHub repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

### Other Platforms

The application can be deployed to:
- **Railway**: `railway up`
- **Render**: Connect GitHub repo
- **Heroku**: `git push heroku main`
- **AWS**: Use Elastic Beanstalk or ECS
- **Google Cloud**: Use Cloud Run or App Engine

## Architecture

```
nocodebackend-api/
├── api/                    # API route handlers
├── core/                   # Core functionality
│   ├── config.py          # Configuration management
│   ├── database.py        # Database connections
│   ├── security.py        # Authentication & security
│   └── monitoring.py      # Health checks & metrics
├── models/                 # Pydantic models
├── services/               # Business logic
├── utils/                  # Utility functions
├── tests/                  # Test suite
└── main.py                 # FastAPI application
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests
4. Run tests: `pytest tests/`
5. Commit your changes: `git commit -am 'Add your feature'`
6. Push to the branch: `git push origin feature/your-feature`
7. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

- 📧 Email: support@nocodebackend.com
- 📖 Documentation: https://docs.nocodebackend.com
- 🐛 Issues: https://github.com/your-org/nocodebackend-api/issues
- 💬 Discussions: https://github.com/your-org/nocodebackend-api/discussions