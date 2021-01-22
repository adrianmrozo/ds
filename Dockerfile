FROM python:3.8.5

WORKDIR /usr/src/app

COPY /src/main.py .
COPY /src/load_and_test.py .
COPY /src/output.py .
COPY /src/prep_cifar10.py .
COPY /src/set_initials.py .
COPY /src/shape_model.py .
COPY /src/test.py .
COPY /src/training.py .
COPY requirements.txt .
COPY /src/postgres_db.py .
COPY /src/app.py .

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt


CMD ["python3", "postgres_db.py"]
CMD ["python3", "app.py"]

