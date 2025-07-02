FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Build the model inside the Docker image
RUN python train_model.py

CMD ["python", "app.py"]

