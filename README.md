# Hotel

# Hotel Management System

A comprehensive Django-based web application designed to streamline hotel operations, from guest management to room reservations and staff workflows.

## Overview

This full-stack web application addresses real-world challenges in the hospitality industry by digitizing manual processes and providing an integrated platform for hotel management. The system supports multiple user roles and provides intuitive interfaces for daily hotel operations.

## Features

### Core Functionality
- **Guest Management**: Complete guest registration, search, and profile management
- **Room Management**: Configure room types, manage inventory, and track occupancy
- **Reservation System**: Multi-step booking process with conflict detection and validation
- **Check-in/Check-out**: Streamlined guest arrival and departure workflows
- **Advanced Search**: Filter guests, reservations, and rooms with multiple criteria

### User Roles
- **Receptionists**: Handle daily operations, guest check-ins, and bookings
- **Managers**: Access to all features plus room/system configuration

### Technical Features
- **REST API**: Full API access for external integrations
- **Session Management**: Maintains user context across multi-step processes
- **Data Validation**: Comprehensive input validation and business rule enforcement
- **Audit Logging**: Detailed operation tracking for monitoring and compliance

## Technology Stack

- **Backend**: Python 3.x, Django 4.x
- **Database**: SQLite (development), PostgreSQL ready
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **API**: Django REST Framework
- **Authentication**: Django's built-in authentication system
- **Validation**: Custom validators with regex patterns

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   cd hotel-management-system
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv hotel_env
   
   # On Windows
   hotel_env\Scripts\activate
   
   # On macOS/Linux
   source hotel_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework django-filter
   ```

4. **Database setup**
   ```bash
   python manage.py makemigrations hotel_app
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data (optional)**
   ```bash
   python manage.py loaddata sample_data.json
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Web interface: http://localhost:8000
   - Admin panel: http://localhost:8000/admin
   - API root: http://localhost:8000/api/

## Project Structure

```
hotel_management_system/
├── hotel_app/
│   ├── models.py          # Data models and business logic
│   ├── views.py           # Request handling and workflows
│   ├── forms.py           # Form definitions and validation
│   ├── filters.py         # Search and filtering logic
│   ├── serializers.py     # API serialization
│   ├── permissions.py     # Custom permissions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin interface configuration
│   └── templates/         # HTML templates
├── static/                # CSS, JavaScript, images
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file
```

## User Management

### Setting Up User Roles

1. **Create Manager Group** (via Django Admin):
   - Go to http://localhost:8000/admin
   - Navigate to Groups → Add Group
   - Create group named "Manager"

2. **Assign Users to Groups**:
   - Select user in admin panel
   - Add to appropriate group (Manager for full access)

### Default Permissions
- **All authenticated users**: Guest and reservation management
- **Manager group**: Full access including room and room type management

## Configuration

### Database Configuration
For production, update `settings.py` to use PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hotel_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your_secret_key_here
DEBUG=False
DATABASE_URL=postgresql://user:pass@localhost/hotel_db
```

## API Documentation

### Authentication
The API supports both session and basic authentication:
```bash
# Using session authentication (after web login)
curl http://localhost:8000/api/guest/

# Using basic authentication
curl -u username:password http://localhost:8000/api/guest/
```

### Key Endpoints
- **Guests**: `/api/guest/` (GET, POST), `/api/guest/{id}/` (GET, PUT, DELETE)
- **Reservations**: `/api/reservation/` (GET, POST), `/api/reservation/{id}/` (GET, PUT, DELETE)
- **Rooms**: `/api/room/` (GET, POST), `/api/room/{id}/` (GET, PUT, DELETE)
- **Room Types**: `/api/room-type/` (GET, POST), `/api/room-type/{code}/` (GET, PUT, DELETE)

### Sample API Usage
```bash
# Create a new guest
curl -X POST http://localhost:8000/api/guest/ \
  -u admin:password \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mr",
    "first_name": "John",
    "last_name": "Smith",
    "email": "john.smith@email.com",
    "phone_number": "07123456789",
    "address_line1": "123 Main St",
    "city": "London",
    "county": "Greater London",
    "postcode": "SW1A 1AA"
  }'
```

## Testing

### Run Tests
```bash
python manage.py test hotel_app
```

### Test Coverage Areas
- Model validation and business logic
- Form validation and processing
- View functionality and permissions
- API endpoints and authentication
- Filter and search functionality

## Security Features

- **Authentication Required**: All views require user login
- **Role-Based Access**: Manager permissions for sensitive operations
- **Input Validation**: Comprehensive validation with regex patterns
- **SQL Injection Protection**: Django ORM parameterized queries
- **XSS Protection**: Django template auto-escaping
- **CSRF Protection**: Built-in Django CSRF middleware

## Deployment

### Development
Already configured for development with SQLite and DEBUG=True.

### Production Considerations
1. **Database**: Use PostgreSQL or MySQL
2. **Static Files**: Configure static file serving (nginx/Apache)
3. **Security**: Update `ALLOWED_HOSTS`, set `DEBUG=False`
4. **Environment Variables**: Use environment variables for secrets
5. **HTTPS**: Enable SSL/TLS in production

### Docker Deployment (Optional)
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Contributing

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make changes and add tests
4. Commit changes (`git commit -am 'Add new feature'`)
5. Push to branch (`git push origin feature/new-feature`)
6. Create Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings for all functions and classes
- Include tests for new functionality
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

**Database Migration Errors**
```bash
python manage.py makemigrations --empty hotel_app
python manage.py migrate
```

**Permission Denied Errors**
- Ensure user is in correct group (Manager for room operations)
- Check user authentication status

**Static Files Not Loading**
```bash
python manage.py collectstatic
```

**Port Already in Use**
```bash
python manage.py runserver 8001
```

## Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Review existing documentation
- Check the Django documentation for framework-specific questions

## Roadmap

### Planned Features
- [ ] Mobile responsive design improvements
- [ ] Email notification system
- [ ] Payment gateway integration
- [ ] Advanced reporting and analytics
- [ ] Multi-property support
- [ ] Housekeeping management module
- [ ] Guest loyalty program
- [ ] Calendar integration
- [ ] Real-time updates with WebSockets

### Performance Improvements
- [ ] Database query optimization
- [ ] Caching implementation (Redis)
- [ ] API rate limiting
- [ ] Background task processing

---

## Screenshots

[See Appendix A - User Acceptance Tests - testing.pdf]

<img width="1283" height="599" alt="image" src="https://github.com/user-attachments/assets/5933512a-7396-40e2-8f77-6392f43f9bc3" />

<img width="1280" height="737" alt="image" src="https://github.com/user-attachments/assets/188fc310-c9e9-42e9-9063-fdc243f620bf" />

<img width="1297" height="593" alt="image" src="https://github.com/user-attachments/assets/d8f93223-8257-4cd2-995d-21e2bf088371" />

<img width="1282" height="961" alt="image" src="https://github.com/user-attachments/assets/2aa19d6c-f7b3-4212-8e27-ff0fbb136334" />


<img width="1293" height="663" alt="image" src="https://github.com/user-attachments/assets/e0890c44-63d7-4a78-b284-e4ed4973797c" />


<img width="1271" height="989" alt="image" src="https://github.com/user-attachments/assets/1af816c4-3e7f-4596-92cd-64607ac2bb9f" />
