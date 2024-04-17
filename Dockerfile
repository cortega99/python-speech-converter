# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install git, required for pip to clone the Whisper repository
RUN apt-get update && \
    apt-get install -y git ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools to the latest version
RUN pip install --upgrade pip setuptools

# Clear pip cache to ensure we get fresh packages
RUN pip cache purge

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Whisper without using pip's cache, directly from GitHub
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

# Make port 5000 available to the outside world
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run your Flask application
CMD ["python", "main.py"]
