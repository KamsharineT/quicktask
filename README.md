# QuickTask

A lightweight and scalable Django REST API for managing personal tasks.  
Designed for simplicity and clean architecture, QuickTask features user authentication, task creation, updating, filtering by status or due date, and due date tracking.

---

## Features

- User registration and token-based authentication
- Create, read, update, and delete (CRUD) tasks
- Filter tasks by status (pending/completed) and due date
- Pagination and search support
- API documentation with Swagger UI
- Easily extendable and ready for deployment

---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default, can switch to PostgreSQL)
- Token Authentication
- Swagger (drf-yasg)

🔧 Tech Stack

Backend: Django + Django REST Framework
Database: SQLite (for demo), easily switchable to PostgreSQL
Auth: Token-based (DRF's TokenAuth or JWT)
Docs: Swagger/OpenAPI (drf-yasg or drf-spectacular)
Tests: Pytest or Django’s built-in test suite
Deployment Ready: Docker + GitHub Actions (CI) + Render/Heroku

---

## Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/quicktask.git
   cd quicktask
   ```
