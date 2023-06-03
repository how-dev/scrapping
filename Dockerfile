FROM python:3.8

COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip install -r requirements/base.txt

WORKDIR /code
COPY . /code/
