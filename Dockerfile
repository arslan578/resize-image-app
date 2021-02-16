FROM python:3.7
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","app.py"]
