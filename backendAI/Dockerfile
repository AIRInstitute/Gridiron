FROM python:3.7.8
WORKDIR /app
COPY . /app
RUN pip install -r backendAI/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 python3-h5py -y
EXPOSE 2725
WORKDIR /app/backendAI/src
CMD ["python", "__init__.py"] 
