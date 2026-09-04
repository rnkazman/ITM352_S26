# Bainomugisha Nature Park Mobile Application

A comprehensive real-time mobile park management system enabling GPS-based wildlife tracking, crowd control, and emergency coordination across thousands of square kilometers of diverse ecosystems.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/flask-2.3+-orange.svg)
![Status](https://img.shields.io/badge/status-development-yellow.svg)

## 🌟 Features

- **User Management**: Secure registration with phone verification for visitors and staff
- **Vehicle Tracking**: Real-time GPS monitoring with license plate registration
- **Wildlife Spotting**: Animal sighting reports with photo uploads and community verification
- **Crowd Control**: Intelligent zone capacity monitoring to prevent overcrowding
- **Emergency Alerts**: Panic button system with proximity-based staff coordination
- **Zone Information**: GPS-based ecosystem information and wildlife guidance
- **Real-time Notifications**: Live alerts for sightings, emergencies, and zone updates

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Mobile Apps   │    │   API Gateway   │    │   Core Services │
│                 │    │                 │    │                 │
│ • Visitor App   │◄──►│ • Flask API     │◄──►│ • Authentication│
│ • Staff App     │    │ • Load Balancer │    │ • Location      │
└─────────────────┘    └─────────────────┘    │ • Emergency     │
                                              │ • Notifications │
┌─────────────────┐    ┌─────────────────┐    │ • Crowd Control │
│   Data Layer    │    │   Message Queue │    └─────────────────┘
│                 │    │                 │
│ • PostgreSQL    │◄──►│ • Celery        │
│ • PostGIS       │    │ • Redis Broker  │
│ • Redis Cache   │    │ • FCM Push      │
└─────────────────┘    └─────────────────┘
```

### Technology Stack

- **Backend**: Flask 2.3+ with Python 3.8+
- **Database**: PostgreSQL with PostGIS extension for spatial data
- **Caching**: Redis for real-time data and session storage
- **Authentication**: JWT tokens with refresh token support
- **Real-time**: WebSocket connections via Flask-SocketIO
- **Message Queue**: Celery for asynchronous alert distribution
- **File Storage**: AWS S3 for photo and media uploads
- **Push Notifications**: Firebase Cloud Messaging (FCM)
- **Mobile**: React Native (future implementation)

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL 12+ with PostGIS extension
- Redis 6.0+
- Node.js 16+ (for future mobile development)
- AWS S3 bucket (for photo storage)
- Firebase project (for push notifications)

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/rnkazman/ITM352_S26.git
cd ITM352_S26
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv bnp_env

# Activate environment
# macOS/Linux:
source bnp_env/bin/activate
# Windows:
bnp_env\Scripts\activate

# Install dependencies
pip install -r requirements-bnp.txt
```

### 3. Configure Environment

```bash
# Copy environment template
cp .env.template .env

# Edit .env with your configuration
# DATABASE_URL, REDIS_URL, SECRET_KEY, etc.
```

### 4. Set Up Database

```bash
# Install PostgreSQL and PostGIS
# macOS with Homebrew:
brew install postgresql postgis

# Start PostgreSQL service
brew services start postgresql

# Create database
createdb bnp_development

# Enable PostGIS extension
psql bnp_development -c "CREATE EXTENSION postgis;"
```

### 5. Initialize Database

```bash
# Set environment
export FLASK_APP=app.py
export FLASK_ENV=development

# Initialize migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Load Sample Data

```bash
# Load park zones and animal species (coming in next phase)
python scripts/load_sample_data.py
```

### 7. Start Development Server

```bash
# Start Redis (if not running)
redis-server

# Start Flask application
python app.py

# API will be available at http://localhost:5000
```

## 📡 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token
- `GET /api/v1/auth/profile` - Get user profile

### Wildlife & Locations  
- `GET /api/v1/zones` - Get park zones
- `GET /api/v1/species` - Get animal species
- `POST /api/v1/sightings` - Report animal sighting
- `GET /api/v1/sightings` - Get recent sightings

### Vehicle Tracking
- `POST /api/v1/tracking/location` - Update vehicle location
- `GET /api/v1/tracking/zones/{zone_id}` - Get zone occupancy

### Emergency
- `POST /api/v1/emergency/alert` - Create emergency alert
- `GET /api/v1/emergency/alerts` - Get active alerts (staff)

### Notifications
- `GET /api/v1/notifications` - Get user notifications
- `PATCH /api/v1/notifications/{id}/read` - Mark notification as read

## 🗺️ Project Structure

```
ITM352_S26/
├── docs/
│   └── architecture/          # PlantUML architecture diagrams
├── backend/
│   ├── models/               # SQLAlchemy database models
│   ├── api/                  # Flask API endpoints
│   └── services/             # Business logic services
├── config/                   # Configuration files
├── data/                     # Sample data (GeoJSON, species)
├── migrations/               # Database migration files
├── mobile/                   # Future React Native app
├── app.py                    # Flask application factory
├── requirements-bnp.txt      # Python dependencies
└── README.md                 # This file
```

## 🔧 Development

### Database Models

The system includes 8 core models with spatial data support:

- **User**: Visitor and staff authentication
- **Vehicle**: License plate registration and tracking
- **ParkZone**: Geographic boundaries with PostGIS
- **AnimalSpecies**: Wildlife species database
- **AnimalSighting**: GPS-tagged wildlife reports
- **VehicleTracking**: Real-time location history
- **EmergencyAlert**: Panic button incidents
- **Notification**: Multi-channel messaging system

### Running Tests

```bash
# Set test environment
export FLASK_ENV=testing

# Run test suite
python -m pytest tests/

# Run with coverage
python -m pytest --cov=backend tests/
```

### Code Quality

```bash
# Format code
black backend/

# Lint code  
flake8 backend/

# Type checking
mypy backend/
```

## 📱 Mobile Application

The mobile application will be built using React Native and will include:

- Cross-platform support (iOS/Android)
- Offline GPS tracking capability
- Real-time push notifications
- Camera integration for wildlife photography
- Maps integration with zone boundaries

## 🔐 Security Features

- JWT-based authentication with refresh tokens
- Phone number verification via SMS
- Role-based access control (visitor/guide/medical/control)
- Rate limiting on API endpoints
- Input validation and sanitization
- Secure file upload handling

## 📊 Monitoring & Analytics

### Real-time Metrics
- Active vehicles per zone
- Emergency response times
- Popular sighting locations
- User engagement statistics

### Performance Monitoring
- API response times
- Database query optimization
- WebSocket connection health
- Push notification delivery rates

## 🌍 Deployment

### Development
- SQLite database for local development
- Local Redis instance
- Flask development server

### Production
- PostgreSQL with PostGIS on AWS RDS
- Redis on AWS ElastiCache
- Docker containers on AWS ECS
- AWS S3 for file storage
- CloudWatch for monitoring

## 📖 Documentation

- **Architecture Documentation**: [docs/architecture/README.md](docs/architecture/README.md)
- **API Documentation**: Available at `/docs` endpoint (Swagger UI)
- **Database Schema**: See PlantUML diagram in [docs/architecture/database_schema.puml](docs/architecture/database_schema.puml)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support, please contact:
- **Technical Issues**: Create a GitHub issue
- **Emergency**: Use the in-app panic button
- **General Questions**: admin@bnp.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

### Phase 1: Foundation ✅
- [x] Architecture documentation
- [x] Database models and relationships
- [x] JWT authentication system
- [x] Basic API structure

### Phase 2: Core Features (In Progress)
- [ ] PostgreSQL + PostGIS setup
- [ ] Vehicle registration and tracking
- [ ] Animal spotting with photo upload
- [ ] Real-time zone monitoring

### Phase 3: Real-time Systems
- [ ] WebSocket notifications
- [ ] Emergency alert distribution
- [ ] Push notification integration
- [ ] Celery task processing

### Phase 4: Mobile Application
- [ ] React Native app structure
- [ ] GPS tracking implementation  
- [ ] Camera integration
- [ ] Offline capability

### Phase 5: Advanced Features
- [ ] AI-powered animal recognition
- [ ] Predictive crowd modeling
- [ ] Advanced analytics dashboard
- [ ] Multi-language support

---

## 🦁 About Bainomugisha Nature Park

This system is designed for one of Africa's largest and most technologically advanced wildlife reserves, supporting conservation efforts through innovative mobile technology and real-time monitoring systems.

**Built with ❤️ for wildlife conservation and visitor safety.**