@echo off
echo Starting Library Management System...
echo.

REM Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo Python is not installed! Please install Python 3.8 or higher.
    pause
    exit /b
)

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements
echo Installing/Updating requirements...
pip install -r requirements.txt

REM Make and apply migrations
echo Applying database migrations...
python manage.py makemigrations
python manage.py migrate

REM Check if superuser exists
echo Checking for superuser...
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); exit(0 if User.objects.filter(is_superuser=True).exists() else 1)" > nul 2>&1
if errorlevel 1 (
    echo No superuser found. Creating one...
    echo Please create a superuser account:
    python manage.py createsuperuser
)

REM Initialize sample data
echo.
echo Initializing sample library data...
python manage.py init_library_data

REM Run the server
echo.
echo Starting development server...
echo Visit http://127.0.0.1:8000/ in your web browser
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver

REM Deactivate virtual environment
call venv\Scripts\deactivate 