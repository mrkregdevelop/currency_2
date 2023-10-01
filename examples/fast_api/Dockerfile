FROM python:3.11.5

WORKDIR /project/code

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .


CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0
