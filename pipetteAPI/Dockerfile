FROM python:3.7.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8081
WORKDIR /app
RUN chmod 400 /app/keys/ot2_ssh_key
CMD ["python", "flask_app.py"] 
