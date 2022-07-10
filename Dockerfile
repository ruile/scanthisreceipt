FROM python:3.8-slim-buster

WORKDIR /myapp

RUN apt update
RUN apt install build-essential -y
RUN apt install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py ocr.py .
COPY models ./models
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]