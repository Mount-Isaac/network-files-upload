FROM python:3.9-slim

WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Create the upload directory
RUN mkdir -p /app/uploads/data

EXPOSE 1515

CMD ["gunicorn", "--bind", "0.0.0.0:1515", "app:app"]