# tvssale Project

This is a Django project named **tvssale**. It consists of two main applications: **webpage** and **sales**. The project is structured to facilitate the development of a web application focused on television sales.

## Project Structure

- **env/**: Python virtual environment for the project.
- **manage.py**: Command-line utility for interacting with the Django project.
- **tvssale/**: Main project directory containing configuration files.
  - **__init__.py**: Indicates that this directory is a Python package.
  - **settings.py**: Configuration settings for the Django project.
  - **urls.py**: URL patterns for the project.
  - **wsgi.py**: For deploying the project on WSGI-compatible web servers.
  - **asgi.py**: For deploying the project on ASGI-compatible web servers.
- **webpage/**: Application for handling webpage-related functionalities.
  - **__init__.py**: Indicates that this directory is a Python package.
  - **admin.py**: Register models with the Django admin site.
  - **apps.py**: Configuration for the webpage application.
  - **models.py**: Data models for the webpage application.
  - **tests.py**: Tests for the webpage application.
  - **views.py**: View functions for the webpage application.
  - **urls.py**: URL patterns specific to the webpage application.
  - **migrations/**: Directory for database migrations.
- **sales/**: Application for handling sales-related functionalities.
  - **__init__.py**: Indicates that this directory is a Python package.
  - **admin.py**: Register models with the Django admin site for the sales application.
  - **apps.py**: Configuration for the sales application.
  - **models.py**: Data models for the sales application.
  - **tests.py**: Tests for the sales application.
  - **views.py**: View functions for the sales application.
  - **urls.py**: URL patterns specific to the sales application.
  - **migrations/**: Directory for database migrations.
- **templates/**: Directory for HTML templates.
  - **base.html**: Base template for other templates to extend.
  - **index.html**: Homepage template that extends base.html.
- **static/**: Directory for static files (CSS, JavaScript, images).
- **requirements.txt**: Lists project dependencies, including Django and Django REST framework.
- **README.md**: Documentation for the project. 

## Installation

1. Create a virtual environment:
   ```
   python -m venv env
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Project

To run the development server, use the following command:
```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to view the homepage.