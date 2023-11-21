# Vendor Management System

Vendor Management System is a Django project designed to manage vendors, purchase orders, and performance metrics.

## Getting Started

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

### API Endpoints

#### Update Acknowledgment Endpoint

- URL: `POST /api/purchase_orders/{po_id}/acknowledge`
- Description: This endpoint is used by vendors to acknowledge purchase orders. It updates the `acknowledgment_date` and triggers the recalculation of `average_response_time`.

### Admin Interface

Access the Django admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

## Project Structure

- `vendor_management/`: Django app containing models, views, and serializers.
- `config/`: Django project settings.
- `manage.py`: Django management script.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
