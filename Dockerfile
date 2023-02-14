# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM django

ADD . /iptc-web-editor
WORKDIR /iptc-web-editor

RUN pip install -r requirements.txt
RUN pip install django-tinymce

RUN ls -a

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000", "--settings=iptc-web-editor.settings.prod" ]
