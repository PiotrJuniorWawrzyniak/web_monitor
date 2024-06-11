# Web Monitor

## Description
The Web Monitor application tracks a list of web pages provided in a CSV file, along with their refresh frequency and a search phrase. If a page has changed since the last check, the application displays a notification and sends an email alert. If the specified phrase is found on the page (and was not previously present), an additional notification is sent. The application also sends a daily report of registered changes.

This project is built using Django and Celery Beat.

## Requirements
- Python 3.x
- Django
- Celery
- Redis or RabbitMQ (for Celery broker)
- SMTP server (for sending emails)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/web-monitor.git
    cd web-monitor
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Configure Celery:
    - Ensure Redis or RabbitMQ is running.
    - Start the Celery worker:
        ```sh
        celery -A web_monitor worker --loglevel=info
        ```
    - Start the Celery Beat scheduler:
        ```sh
        celery -A web_monitor beat --loglevel=info
        ```

## Usage
1. Upload the CSV file containing the list of URLs, refresh frequency, and search phrases.
2. The application will periodically check the specified web pages.
3. Notifications will be sent via email if changes are detected or if the search phrase is found.
4. A daily report of all changes will be emailed once a day.

## Author
- Piotr Wawrzyniak - [piotrjuniorwawrzyniak@gmail.com](mailto:piotrjuniorwawrzyniak@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.