# Use Python 3.9 as base image
FROM python:3.9

# Set working directory to /app
WORKDIR /app

# Copy requirements.txt first for caching layer optimization
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into /app/app
COPY ./app /app/app

# Copy the Gunicorn config file
COPY gunicorn_config.py /app/gunicorn_config.py

# Set the entry point to start the app with Gunicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/app/gunicorn_config.py", "app.main:app"]
