FROM python:3.11.5

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# Create certificate
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=US/ST=CA/L=San Francisco/O=My semantic app/CN=mysemanticapp.com" \
    -keyout /etc/ssl/private/mysemanticapp.key \
    -out /etc/ssl/certs/mysemanticapp.crt

# Install dependencies
RUN apt-get update && apt-get install -y openssl
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . /app

# Used for Flask
EXPOSE 80

# ENTRYPOINT ["python3"]
CMD [ "python3", "console_chat.py" ]