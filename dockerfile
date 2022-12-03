FROM python:3.10

WORKDIR /code

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

ENV DATABASE_DIALECT=

CMD ["uvicorn", "src.main.config:app", "--host", "0.0.0.0", "--port", "80", "--reload"]