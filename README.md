# Portfolio Website (Django)

This is a Django-based portfolio website converted from a static HTML site.

## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).

## Installation

1.  Clone the repository (if you haven't already).
2.  Install Django:

    ```bash
    pip install django
    ```

## Setup

1.  **Apply Migrations:**
    Initialize the database by applying the migrations.

    ```bash
    python manage.py migrate
    ```

2.  **Collect Static Files:**
    Gather all static files (CSS, JS, images) into the `staticfiles` directory.

    ```bash
    python manage.py collectstatic
    ```

## Running the Website

To start the development server:

```bash
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000/` to view the website.

## Running Tests

To run the automated tests for the portfolio app:

```bash
python manage.py test portfolio
```

## Project Structure

-   `myportfolio/`: The Django project configuration.
-   `portfolio/`: The main application containing views, URLs, templates, and static files.
    -   `templates/portfolio/`: HTML templates.
    -   `static/portfolio/`: Static assets (CSS, JS, Images).
-   `manage.py`: Django's command-line utility.
