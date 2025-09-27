# ESports Community Website

A Flask web application for content creators to connect, share, and discuss their streaming experiences across various platforms like YouTube, Twitch, Facebook Gaming, and more.

## Features

- **User Authentication & Registration**: Secure login and registration system with Flask-Login
- **Multi-Platform Support**: Support for YouTube, Twitch, Facebook Gaming, Kick, Rumble, and other streaming platforms
- **Community Posts**: Create and browse posts with different categories:
  - General Discussion
  - Stream Announcements
  - Stream Reviews
  - Tips & Tricks
  - Game Discussion
  - Collaboration Requests
  - Feedback Requests
- **Comments System**: Interactive commenting on posts
- **Search & Filter**: Search posts by content and filter by type
- **Responsive Design**: Mobile-friendly Bootstrap interface
- **User Profiles**: Display creator information and streaming platform details

## Technology Stack

- **Backend**: Flask 2.3.3
- **Database**: SQLAlchemy with SQLite (development), easily configurable for PostgreSQL/MySQL
- **Authentication**: Flask-Login with Werkzeug password hashing
- **Forms**: Flask-WTF with WTForms validation
- **Frontend**: Jinja2 templates + Bootstrap 5
- **Package Manager**: pip

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

#### Windows:
1. Double-click `start.bat`

#### Linux/Mac:
1. Make the script executable: `chmod +x start.sh`
2. Run: `./start.sh`

#### Manual Installation:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python run.py
   ```
3. Open your browser and visit `http://localhost:5000`

### Database Configuration

- The application uses SQLite by default (file: `esports_community.db`)
- Database tables are created automatically on first run
- To use PostgreSQL or MySQL, update the `DATABASE_URL` in the app configuration

## Usage

1. **Register**: Create a new account with your streaming platform details
2. **Browse Posts**: View community discussions and stream announcements
3. **Create Posts**: Share your streaming experiences, ask questions, or make announcements
4. **Engage**: Comment on posts and participate in discussions
5. **Search**: Find specific content using the search functionality

## Project Structure

```
app/
├── routes/
│   ├── auth.py          # Authentication routes
│   ├── main.py          # Home and general routes
│   └── posts.py         # Post and comment routes
├── templates/
│   ├── auth/            # Login and registration templates
│   ├── posts/           # Post-related templates
│   └── index.html       # Home page
├── __init__.py          # Flask app factory
├── models.py            # Database models
└── forms.py             # WTForms form definitions
run.py                   # Application entry point
requirements.txt         # Python dependencies
start.bat               # Windows startup script
start.sh                # Linux/Mac startup script
```

## Features in Detail

### User System
- Secure registration and login
- Password hashing with Werkzeug
- User profiles with streaming platform integration
- Optional bio and stream URL

### Posts & Comments
- Rich post categories for different types of content
- Stream URL integration for easy sharing
- Threaded comment system
- Search and filtering capabilities

### Security
- CSRF protection with Flask-WTF
- Secure session management
- Input validation and sanitization

## Development

### Environment Variables
Set these environment variables for production:
- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: Database connection string

### Database Models
- `User`: User accounts and profiles
- `Post`: Community posts with categories
- `Comment`: Post comments and discussions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please open an issue on the GitHub repository.