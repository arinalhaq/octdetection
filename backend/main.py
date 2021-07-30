import base64
from io import BytesIO
from typing import Optional

import numpy as np
from PIL import Image
from fastapi import FastAPI
from fastapi import File, UploadFile
from matplotlib.pyplot import imsave
from starlette.responses import StreamingResponse

import cnn_model

app = FastAPI()


@app.get('/')
async def load_index():
    return {"message": "OCTDetection - REST API"}


@app.post('/predict')
async def predict(model: Optional[str] = None, img: UploadFile = File(...)):
    image = await open_file(img)
    transformed_image = cnn_model.transform_image(image, model)

    predict_model = cnn_model.load_model(model)
    desc, prediction, probabilities = cnn_model.predict_image(predict_model, transformed_image)

    return {
        "class": prediction,
        "probabilities": probabilities,
        "detail": desc,
        "model": model
    }


@app.post('/comparison')
async def comparison(model: str, image: UploadFile = File(...)):
    pmodel = model.split(",")
    image = await open_file(image)

    presult = {}

    for value in pmodel:
        transformed_image = cnn_model.transform_image(image, value)

        predict_model = cnn_model.load_model(value)
        desc, prediction, probabilities = cnn_model.predict_image(predict_model, transformed_image)
        presult[value] = {
            "class": prediction,
            "probabilities": probabilities,
            "detail": desc
        }

    return presult


async def open_file(img):
    image = BytesIO(img.file.read())
    image = Image.open(image).convert('RGB')

    return image


async def convert_byte(image):
    image = np.array(image)

    image_byte = BytesIO()
    imsave(image_byte, image)
    image_byte.seek(0)

    return image_byte
