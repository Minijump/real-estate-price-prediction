# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages 
RUN pip install -r requirements.txt

# Set the environment variable
ENV FLASK_APP=app.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]

# create requirements: pipreqs 'foldername' (--force)-> force if ou want to crush an existing requirement file
# cd Documents/Becode/real-estate-price-prediction/API_deployment
# create image: docker build -t image_prediction .
# create docker: docker run -p 5000:5000 image_prediction
# in the browser: http://localhost:5000/predict      =>...=>open with browser (in docker desktop)
#postamn: {"data": {"Living_Area": 90, "Type_of_property": "HOUSE", "Number_of_rooms": 4, "Locality": 6637, "Swimming_pool": 0}}
# Use an official Python runtime as the base image