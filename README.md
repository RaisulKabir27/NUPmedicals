# NUP Medical System

A Django-based hospital management system designed to support patient management, authentication, hospital operations, payment processing, and administrative workflows through a centralized web application.

## Overview

NUP Medical System is a web-based healthcare management application developed using the **Django Model-View-Template (MVT) architecture**.

The system organizes different aspects of hospital administration into separate modules, including:

* Patient and medical information management
* User authentication and login
* Hospital management workflows
* Payment-related operations
* Database-backed record management
* Web-based administrative interfaces

The project follows Django's modular application structure, making the system easier to maintain and extend.

## Key Features

### Patient Management

The system provides functionality for managing patient-related information and medical records within the hospital management workflow.

### Authentication

A dedicated authentication module provides user login and access to the system.

### Hospital Management

The hospital module handles core hospital-related operations and provides the application structure for managing healthcare workflows.

### Payment Management

The payment module provides functionality for handling payment-related information within the system.

### Database Management

The application uses a relational database architecture for persistent storage. The repository also contains an SQL database dump for the project.

### MVT Architecture

The application follows Django's Model-View-Template architecture:

```text
User
 │
 ▼
URL / Request
 │
 ▼
View
 │
 ├── Model ──► Database
 │
 ▼
Template
 │
 ▼
Response
```

This separation keeps application logic, data models, and presentation components organized.

## Project Structure

```text
NUPmedicals/
│
├── Hospital/
├── Login/
├── MVT Structure/
├── NUPmedicals/
├── Payment/
├── static/
│
├── NUPmedicalsdb.sql
├── manage.py
├── requirments.txt
├── .gitignore
└── README.md
```

### Main Components

| Component           | Purpose                                 |
| ------------------- | --------------------------------------- |
| `Hospital/`         | Hospital-related functionality          |
| `Login/`            | Authentication and login functionality  |
| `Payment/`          | Payment-related functionality           |
| `NUPmedicals/`      | Main Django project configuration       |
| `MVT Structure/`    | MVT-related project structure/materials |
| `static/`           | Static assets                           |
| `manage.py`         | Django project administration           |
| `NUPmedicalsdb.sql` | Database SQL dump                       |
| `requirments.txt`   | Python dependency list                  |

## Technology Stack

* **Python**
* **Django 3.2**
* **PostgreSQL**
* **Django Polymorphic**
* **Pillow**
* **ReportLab**
* **HTML/CSS**
* **SQL**

The repository specifies Django 3.2, `django-polymorphic`, PostgreSQL's `psycopg2` driver, Pillow, ReportLab, and other supporting Python packages.

## Requirements

Before running the project, install:

* Python
* PostgreSQL
* pip
* A virtual environment is recommended

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/RaisulKabir27/NUPmedicals.git
cd NUPmedicals
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

The repository currently uses a file named `requirments.txt`:

```bash
pip install -r requirments.txt
```

## Database Setup

The repository contains:

```text
NUPmedicalsdb.sql
```

which can be used to recreate the project's database.

Configure the database connection in the Django settings according to your local PostgreSQL configuration.

Do not commit production database credentials or other sensitive configuration information to the repository.

## Running the Application

From the project directory:

```bash
python manage.py runserver
```

The Django development server will start locally.

Open the address shown by Django in your browser.

## Django Management Commands

Common Django commands include:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Create an administrator account with:

```bash
python manage.py createsuperuser
```

## Architecture

The system follows the Django MVT pattern.

### Models

Models define the application's data structures and database relationships.

### Views

Views contain the application logic responsible for processing requests and generating responses.

### Templates

Templates provide the presentation layer used to display application data through the web interface.

This architecture separates data management, application logic, and presentation.

## Security Considerations

When deploying the system:

* Keep Django `SECRET_KEY` private.
* Do not expose database passwords.
* Do not commit production credentials.
* Use appropriate authentication and authorization controls.
* Use HTTPS in production.
* Keep patient and medical information private.
* Do not expose real patient records through a public repository.

## Educational Purpose

This project demonstrates the development of a web-based healthcare management system using Django and the MVT architectural pattern.

It provides practical experience with:

* Django web development
* MVT architecture
* Relational databases
* Authentication
* Hospital information management
* Payment workflows
* Server-side web application development
* Static asset management

## Future Improvements

Possible extensions include:

* Role-based access control for doctors, nurses, administrators, and patients
* Improved patient search and filtering
* Appointment scheduling
* Prescription management
* Electronic medical records
* Online payment integration
* REST API support
* Improved security and audit logging
* Responsive user interface
* Automated testing
* Containerized deployment

## Author

**Raisul Kabir News**

GitHub:
https://github.com/RaisulKabir27/NUPmedicals

## License

This project is provided for educational and academic purposes.
