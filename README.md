# Web Monitor (Web Monitoring Application)

An application for monitoring changes on selected websites.

## Description
- **Add websites to monitor:** Add new websites to be monitored for changes directly from the main page of the application.
- **Edit websites:** Edit the name of the monitored website, the phrase to track, and the frequency of checks.
- **Delete websites:** Remove selected monitored websites.
- **Track changes:** The application checks selected websites at specified intervals and records changes.

This project is built using Django and Celery Beat.

## Requirements
- Python 3.x
- Django
- Celery
- Redis (for Celery broker)

## Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
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

7. Start the Redis server:
    ```sh
    redis-server
    ```

8. Configure Celery:
    - Ensure Redis is running.
      - Start the Celery worker STANDARD (This command starts the standard Celery worker. It is recommended for production environments or when tasks can be executed in parallel):
          ```sh
          celery -A web_monitor worker --loglevel=info
          ``` 
      - Start the Celery worker WITH A SINGLE-THREAD (This command starts the Celery worker in solo mode, meaning all tasks are executed sequentially, one after the other. This can be useful in development environments or for debugging purposes, where you want to see complete logs from each task synchronously):
        ```sh
        celery -A web_monitor worker --loglevel=info --pool=solo

        ``` 
    - Start the Celery Beat scheduler:
        ```sh
        celery -A web_monitor beat --loglevel=info
        ```

## Usage
1. **Add a website to monitor:**
   - Fill out the form on the main page of the application to add a new website.

2. **Edit a website:**
   - Click on the name of the monitored website to go to the edit page.
   - Enter new data (name, phrase to track, check frequency) and save changes.

3. **Delete a website:**
   - Click the delete button on the edit page to remove the website.

4. **Track changes:**
   - The application automatically checks the websites at specified intervals. Changes are recorded and displayed in the application.

## Author
- Piotr Wawrzyniak - [piotrjuniorwawrzyniak@gmail.com](mailto:piotrjuniorwawrzyniak@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.