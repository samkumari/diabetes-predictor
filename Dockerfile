FROM python:3.9

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["sh", "-c", "python train_model.py && python app.py"]
COPY train_model.py .
RUN python train_model.py
