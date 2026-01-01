FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install pytest pytest-cov


COPY app/app.py /app/app.py


EXPOSE 5000

CMD ["python", "app.py"]
