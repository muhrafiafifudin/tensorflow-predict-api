# Flask API
A simple Flask application that can serve predictions from a models. Reads a pickled model into memory when the Flask app is started and returns predictions through the /predict endpoint. You can also use the /train endpoint to train/retrain the model. Any sklearn model can be used for prediction.

### Dependencies
- numpy
- tensorflow
- Pillow
- Flask

```
pip install -r requirements.txt
```

### Running API
```
python main.py <port>
```

After a second or so you'll get an output showing you the app is running on the localhost

Now I will open Postman and do the following :
- Change the method to POST
- Enter localhost:5000/predict as the URL
- Inside the Body, choose form-data
- Fill Key with 'file' and choose file
- Upload images in sample-images

You can then hit Send :

![Postman](https://user-images.githubusercontent.com/62749874/127580726-546d9c15-b93f-4b78-b9f4-c32155451b79.png)

and sample output :
```
{
	'prediction' : 0,
	'name'       : "COVID-19",
	'desc'       : "Virus Corona atau severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) adalah virus yang menyerang sistem pernapasan. Penyakit karena infeksi virus ini disebut COVID-19. Virus Corona bisa menyebabkan gangguan ringan pada sistem pernapasan, infeksi paru-paru yang berat, hingga kematian",
	'treatment'  : "5M (Memakai masker, Mencuci tangan pakai sabun dan air mengalir, Menjaga jarak, serta Membatasi mobilisasi dan interaksi)"
}
```
