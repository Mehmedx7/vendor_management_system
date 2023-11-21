# Vendor Management System

Vendor Management System is a Django project designed to manage vendors, purchase orders, and performance metrics.

## Getting Started

## API Documentation
Explore the API endpoints and usage in the [Postman API Documentation](https://documenter.getpostman.com/view/29819419/2s9YeAAZyp).


Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python (3.7 or higher)
- Pipenv (for managing virtual environments)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mehmedx7/vendor_management_system.git
    cd vendor_management_system
    ```

2. Install requirements using Pipenv:

    ```bash
    pipenv install -r requirements.txt
    ```

3. Activate the virtual environment:

    ```bash
    pipenv shell
    ```

4. Apply migrations to create the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

The project should now be accessible at http://127.0.0.1:8000/.


### Admin Interface

Access the Django admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
