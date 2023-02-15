# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8-slim-bullseye

# Allows docker to cache installed dependencies between build
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]