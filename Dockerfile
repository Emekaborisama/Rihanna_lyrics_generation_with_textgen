FROM python:3.8
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
EXPOSE 8080