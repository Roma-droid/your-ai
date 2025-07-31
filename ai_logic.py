from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def get_calss(image, model="keras_model.h5", class_names="labels.txt"):
    np.set_printoptions(suppress=True)
    model = load_model(model, compile=False)
    class_names = open(class_names, "r", encoding="utf-8").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normal_image_array = (image_array.astype(np.float32) / 127.5) -1
    data[0] = normal_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    finish_score = prediction[0][index]
    #print("Class:", class_name[2:], end="")
    #print("Score:", finish_score)
    return class_name[2:-1], finish_score