import streamlit as st
from PIL import Image
import json
import requests
import io
import numpy as np

SERVICE_ENDPOINT_INCEPTION = 'http://localhost:3000/classify_inception'
SERVICE_ENDPOINT_RESNET = 'http://localhost:3000/classify_resnet'
SERVICE_ENDPOINT_VGG = 'http://localhost:3000/classify_vgg'

MODEL_INCEPTION = "Inception"
MODEL_RESNET = "Resnet"
MODEL_VGG = "VGG"
MODEL_ALL = "Todos"

def classify(service_url, image):
    serialized_image = json.dumps(image.tolist())
    response = requests.post(
        service_url,
        data=serialized_image,
        headers={'content_type':'application/json'}
    )
    return response.text

st.title('Classificação de Budiões')
st.markdown('Sistema para classificar imagens de budiões')

def select_service_endpoint(selected_model):
    return {
        MODEL_INCEPTION : SERVICE_ENDPOINT_INCEPTION,
        MODEL_RESNET: SERVICE_ENDPOINT_RESNET,
        MODEL_VGG: SERVICE_ENDPOINT_VGG
    }[selected_model]

def main():

    #Combobox para selecionar modelos (Inception, VGG, Resnet)
    selected_model = st.selectbox("Selecione o modelo usado na classificação:", (MODEL_INCEPTION,MODEL_RESNET,MODEL_VGG))
    #Espaço para selecionar o path da imagem
    img_file = st.file_uploader("Selecione a imagem do budião:", type=['png','jpg'])
    #Placeholder onde será inserido o resultado da classificação
    classify_result_placeholder = st.empty()
    classify_result = None
    
    if img_file is not None:
        with st.spinner("Classificando..."):
            byte_img = img_file.getvalue()
            img = np.array(Image.open(io.BytesIO(byte_img)))            
            classify_result = classify(select_service_endpoint(selected_model), img)                          
            img_file = None
    
    if classify_result is not None:
        classify_result_placeholder.text("Resultado: " + classify_result)       
        classify_result = None
        
if __name__ == "__main__":
    main()