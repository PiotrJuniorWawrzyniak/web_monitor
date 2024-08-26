# Web Monitor (Web Monitoring Application)

An application for monitoring changes on selected websites.

## Description
- **Add websites to monitor:** Add new websites to be monitored for changes directly from the main page of the application.
- **Edit websites:** Edit the name of the monitored website, the phrase to track, and the frequency of checks.
- **Delete websites:** Remove selected monitored websites.
- **Track changes:** The application checks selected websites at specified intervals and records changes.

This project is built using Django, Celery, and Docker.

## Requirements
- Docker
- Docker Compose

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
    ```

3. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

    This command will:
    - Build the Docker images for the Django app and Celery.
    - Start the Django development server, Redis, Celery worker, and Celery Beat scheduler.

4. Access the application:
    - Open your browser and navigate to `http://localhost:8000` to access the main page.
    - To access the Django admin, navigate to `http://localhost:8000/admin`.

5. Create a superuser to access the Django admin:
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