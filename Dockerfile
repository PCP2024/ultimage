# Start your image with a node base image
FROM python:3.9

# The /app directory should act as the main application directory
WORKDIR /app

# Copy the app package and package-lock.json file
COPY requirements.txt .

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Can add a command to run an application here
CMD ["python", "time.py"]

