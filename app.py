import io
import numpy as np
import tensorflow as tf
import json
from PIL import Image
from flask import Flask, request 

model = tf.keras.models.load_model('model_2.h5')

def prepare_image(img):
    img = Image.open(io.BytesIO(img))
    img = img.resize((224, 224))
    img = np.array(img)
    img = np.expand_dims(img, axis = 0)
    return img

def predict_result(img):
    if model.predict(img)[0][0] == 0:
        data = {
            'prediction' : 0,
            'name'       : "COVID-19",
            'desc'       : "Virus Corona atau severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) adalah virus yang menyerang sistem pernapasan. Penyakit karena infeksi virus ini disebut COVID-19. Virus Corona bisa menyebabkan gangguan ringan pada sistem pernapasan, infeksi paru-paru yang berat, hingga kematian",
            'treatment'  : "5M (Memakai masker, Mencuci tangan pakai sabun dan air mengalir, Menjaga jarak, serta Membatasi mobilisasi dan interaksi)"
        }
        newData = json.dumps(data)
        return newData
    elif model.predict(img)[0][0] == 1: 
        data = {
            'prediction' : 1,
            'name'       : "Normal",
            'prevention' : "Makan Sehat dengan Gizi Seimbang, Banyak Minum Air Putih, Istirahat Yang Cukup, Olahraga Teratur, Mengelola Stres dengan Baik"
        }
        newData = json.dumps(data)
        return newData
    else:
        data = {
            'prediction' : 2,
            'name'       : "Pneumonia",
            'desc'       : "Infeksi yang menimbulkan peradangan pada kantung udara di salah satu atau kedua paru-paru, yang dapat berisi cairan. Infeksi dapat mengancam nyawa siapa pun, terutama pada bayi, anak-anak, dan lansia di atas 65 tahun.",
            'treatment'  : "Minum obat pereda rasa sakit, seperti parasetamol atau ibuprofen yang bisa membantu menurunkan demam. Jangan mengonsumsi obat batuk. Batuk justru merupakan cara tubuh untuk mengeluarkan dahak dari paru-paru, kamu bisa minum air hangat yang dicampur madu dan lemon untuk mengurangi batukmu."
        }
        newData = json.dumps(data)
        return newData

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files.get('file')

    if not file:
        return 

    img_bytes = file.read()
    img = prepare_image(img_bytes)

    return predict_result(img)


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')