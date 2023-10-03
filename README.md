# Airport API

## Project Overview

Welcome to the Airport API project! This Django project is designed to manage airport-related information through a comprehensive API. The project is organized into several components, each with its own models, views, serializers, and endpoints. Here's an overview of the key components:

1. **Airplane**
   - Models, views, serializers, and endpoints for AirplaneType and Airplane models.

2. **Airport**
   - Models, views, serializers, and endpoints for Crew, CrewOccupation, and Airport models.
   - Contains a `tasks.py` file with a Celery task for automatically updating experience for crew members.

3. **Flight**
   - Models, views, serializers, and endpoints for Route and Flight models.

4. **Order**
   - Models, views, serializers, and endpoints for Ticket and Order models.

5. **User**
   - User-related functionality.

The project leverages several technologies and features, including:

- **Django REST framework**: A robust toolkit for building Web APIs.
- **Simple JWT authorization**: Token-based authentication for secure API access.
- **Swagger documentation**: Interactive API documentation for easy testing and exploration.
- **Celery**: A distributed task queue system for background processing.
- **Celery Beat**: A scheduler for running periodic tasks.
- **Flower**: Real-time web-based monitoring tool for Celery tasks.

## Installation

To begin using the Airport API project, follow these steps:

1. Create a copy of the `.env.sample` file as `.env` and configure the environment variables as needed for your specific setup.

2. Clone the project repository:

   ```bash
   git clone [repository_url]
   
   # Create and activate a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install project dependencies:
   pip install -r requirements.txt
   
   # Set up the database and apply migrations:
   python manage.py migrate
   
   # Create a superuser for admin access:
   python manage.py createsuperuser
   
   # Start the Celery worker and beat scheduler:
   celery -A config worker --loglevel=info
   celery -A config beat --loglevel=info
   
   # Optionally, launch the Flower monitoring tool for real-time task insights:
   celery -A config flower
   
   # Run the development server:
   python manage.py runserver
   
   #Access the Swagger API documentation at http://localhost:8000/api/doc/swagger/ to explore and test API endpoints.
   
## Instalation with Docker

To run the project using Docker Compose, follow these steps:

1. Ensure you have Docker installed on your system.

2. Create a copy of the `.env.sample` file as `.env` and configure the environment variables as needed for your specific setup.

3. Build the Docker containers:

   ```bash
   docker-compose build
   docker-compose up -d
4. Access the development server and API at http://localhost:8000.
   
## Features

### Celery Tasks
The Airport component includes a Celery task defined in tasks.py. This task automatically updates crew members' experience field on a monthly basis. The task is scheduled using Celery Beat.

### Flower
For monitoring Celery tasks, you can use the Flower monitoring tool at http://localhost:5555 (default URL). Flower provides real-time insights into task execution and status.

### Authentication and Authorization Token
Secure API access is ensured through Simple JWT token-based authentication. To interact with protected API endpoints, acquire an access token by registering or logging in as a user. Include the token in the Authorization header of your API requests.

For any questions or further assistance, feel free to reach out to:

E-mail: nikulicastas2004@gmail.com,
[GitHub Profile](https://github.com/StreetNik)
   