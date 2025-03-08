FROM python:3.13.0

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code

CMD ["python","main.py"]