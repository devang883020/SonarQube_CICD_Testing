FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install flask==3.0.3 gunicorn==22.0.0


COPY app/app.py /app/app.py


EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.app:app"]
