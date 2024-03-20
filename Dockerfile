# Use an existing Python image as a base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the local project directory to the container's working directory
COPY . /app

# Install necessary Python packages defined in requirements.txt
RUN pip install -r requirements.txt

# Specify any additional configurations if needed
# For example, EXPOSE instruction to expose a port, or ENV instruction to set environment variables

# Command to run your application, if applicable
# CMD [ "python", "app.py" ]
