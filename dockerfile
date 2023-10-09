FROM python:3.11.5

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip setuptools

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

# ENTRYPOINT ["python3"]

CMD [ "python3", "semantic-kernel-fix.py" ]