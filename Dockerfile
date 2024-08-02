# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /opt/app-root/src

# Copy the current directory contents into the container at /opt/app-root/src
COPY . .

# Ensure the default user is used (non-root user)
USER 1001

# Expose the port that the app runs on
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]
