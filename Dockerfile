FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy application code
COPY . /app/
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python3", "main.py"]
