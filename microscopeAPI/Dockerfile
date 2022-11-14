FROM python:3.7.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
WORKDIR /app/src
CMD ["python", "__init__.py"] 
