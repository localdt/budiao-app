import bentoml 
from bentoml.io import NumpyNdarray
import numpy as np
import cv2

TAG = 'modelo_budioes_vgg-ckpnt:dphcykn4sooek7fs'

budiao_runner = bentoml.keras.get(TAG).to_runner()

budiao_service = bentoml.Service('budiao_service', runners = [budiao_runner])

@budiao_service.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_data: np.ndarray) -> np.ndarray:
    image = input_data.astype(np.float32)
    image = cv2.resize(image, (224,224))
    #array tem que ter 4 dimensões (criamos 1 dimensão na frente)
    image = np.expand_dims(image, axis = 0)
    pred = budiao_runner.predict.run(image)
    return pred
