# Python image
FROM python:3.14.2-slim

# Environment settings
# The following variable ensures that the python output is set staright to the termial
# without the buffering it first.
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents .pyc files (not needed in containers)
ENV PYTHONUNBUFFERED 1

# Set working directory
# Note: all directives that follow in the `DockerFile` will be executed in this directory.
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server with Gunicorn
CMD ["gunicorn", "*.wsgi", "--bind", "0.0.0.0:8000", "--workers", "4"]

