# use python runtime as base image
FROM python:3.9

# set working directory
WORKDIR /app

# Copy requirements file to working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Set the entry point for running the application
CMD ["python", "./app/main.py"]
