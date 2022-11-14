FROM python:3.7.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
RUN chmod +x entrypoint.sh
CMD ["/app/entrypoint.sh"] 