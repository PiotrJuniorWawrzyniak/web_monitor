# Web Monitor (Web Monitoring Application)

An application for monitoring changes on selected websites.

## Description
- **Add websites to monitor:** Add new websites to be monitored for changes directly from the main page of the application.
- **Edit websites:** Edit the name of the monitored website, the phrase to track, and the frequency of checks.
- **Delete websites:** Remove selected monitored websites.
- **Track changes:** The application checks selected websites at specified intervals and records changes.

This project is built using Django, Celery (worker, beat), Redis, and Docker for a complete web monitoring solution. Django handles the web application framework, Celery manages asynchronous tasks and periodic tasks, Redis is used as a message broker and result backend for Celery, and Docker provides containerization for the application. 

## Requirements
- Docker (version 20.10 or higher)
- Docker Compose (version 1.29 or higher)
- Python 3.8 or higher

## Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd web-monitor
    ```

2. Create a `.env` file in the project root directory and set the environment variables:
    ```sh
    DEBUG=1
    SECRET_KEY=your_secret_key_here
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    POSTGRES_DB=web_monitor_db
    POSTGRES_USER=web_monitor_user
    POSTGRES_PASSWORD=your_secure_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

    This command will:
    - Build the Docker images for the Django app and Celery.
    - Start the Django development server, Redis, Celery worker, and Celery Beat scheduler.


5. Restart Celery beat server:
    ```sh
    docker-compose restart celery-beat
    ```

6. Apply database migrations:
    ```sh
    docker-compose exec web python manage.py migrate
    ```

7. Access the application:
    - Open your browser and navigate to `http://localhost:8000` to access the main page.
    - To access the Django admin, navigate to `http://localhost:8000/admin`.

8. Create a superuser to access the Django admin:
    ```sh
    docker-compose exec web python manage.py createsuperuser
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

## Stopping the Application
To stop the Docker containers, use:
```sh
docker-compose down
```

## Author
- Piotr Wawrzyniak - [piotrjuniorwawrzyniak@gmail.com](mailto:piotrjuniorwawrzyniak@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.