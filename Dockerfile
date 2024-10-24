# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Download NLTK data
RUN python -m nltk.downloader stopwords

# Expose the port that the app runs on
EXPOSE 5002

# Define the command to run the application
CMD ["python", "app.py"]
