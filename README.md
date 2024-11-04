# Django API Project

## Project Overview
This project is a Django-based API for managing [project-specific functionality, e.g., medications]. The API supports CRUD operations and is designed to be easily integrated with other services.

## Features
- User authentication and permissions
- CRUD operations for [specific models like `MedicationSKU`]
- RESTful API endpoints for integration
- Supports bulk creation for efficient data management
- 

## Getting Started

### Prerequisites
- Python 3.x
- Django 4.x
- Django Rest Framework (DRF)
- Virtual environment manager (recommended: `venv`)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RajeshChoudharytech/medication_sku-_catalogue.git
   cd medication_sku_catalogue
2. **Set Up Virtual Environment**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**
    pip install -r requirements.txt
4. **Apply Migrations**
    python manage.py migrate
5. **Run the Development Server**
    python manage.py runserver

