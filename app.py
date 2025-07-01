from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]
    prediction = model.predict([input_data])[0]
    return render_template('index.html', result=f"Diabetes Risk: {'Yes' if prediction else 'No'}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)