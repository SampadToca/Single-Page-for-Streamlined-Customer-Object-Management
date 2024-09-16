# Customer Management SPA

## Overview
This is a Single Page Application (SPA) and microservice for managing customer objects using Django as the backend. The application provides features for secure login, customer data input, storage, and error handling, all using JWT-based authentication with `rest_framework_simplejwt`.

## Features
- Secure login and logout using JWT tokens.
- Customer data management (CRUD operations).
- Error handling with custom error pages.
- JWT-based authentication.
- API documentation using OpenAPI (Swagger).

## Technologies Used
- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **Django REST Framework Simple JWT**: For JWT-based authentication.
- **PostgreSQL**: Database for storing customer data.
- **Docker**: Containerization of the application.
- **Swagger (drf-yasg)**: For generating interactive API documentation.
- **GitHub**: Hosting the source code repository.

## Prerequisites

Make sure you have the following tools installed:
- **Docker**: For containerizing and running the application.
- **Docker Compose**: For defining and running multi-container Docker applications.

## Installation Instructions

### Step 1: Clone the Repository

```bash
git clone <your-github-repo-url>
cd customer_management

-Admin Panel: http://localhost:8000/admin/
-API Endpoints: Start with http://localhost:8000/api/
-Swagger API Documentation: http://localhost:8000/swagger/