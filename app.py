from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Cargar el modelo de TensorFlow
model = tf.keras.models.load_model('model/fashion_mnist_model.h5')

@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file provided"}), 400

    # Leer la imagen
    img = Image.open(file).convert('L')
    img = img.resize((28, 28))
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32') / 255

    # Realizar la predicción
    prediction = model.predict(img)
    
    output = np.argmax(prediction, axis=1)[0]

    if output==0:
        etiqueta = "Camiseta/Top"
    elif output == 1:
        etiqueta = "Pantalón"
    elif output == 2:
        etiqueta = "Jersey"
    elif output==3:
        etiqueta = "Vestido"
    elif output==4:
        etiqueta = "Abrigo"
    elif output==5:
        etiqueta = "Sandalia"
    elif output==6:
        etiqueta = "Camisa"
    elif output==7:
        etiqueta = "Zapatilla"
    elif output==8:
        etiqueta = "Bolso"
    elif output==9:
        etiqueta = "Botín"
    
    return jsonify({"prediction": etiqueta})

if __name__ == '__main__':
    app.run(debug=True)
