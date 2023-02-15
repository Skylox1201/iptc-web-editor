# Dockerfile

FROM python:3.8

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/iptc-web-editor
COPY ./requirements.txt start-server.sh /opt/app/
COPY ./manage.py /opt/app/iptc-web-editor
COPY .pip_cache /opt/app/pip_cache
COPY . /opt/app/iptc-web-editor/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]