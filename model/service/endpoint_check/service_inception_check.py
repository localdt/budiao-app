import json
import cv2
import numpy as np
import requests

SERVICE_URL = 'http://localhost:3000/classify_inception'

def make_request(service_url, image):
    serialized_image = json.dumps(image.tolist())
    response = requests.post(
        service_url,
        data=serialized_image,
        headers={'content_type':'application/json'}
    )
    return response.text

def main():
    PATH_IMAGE_BUDIAO = 'C:\\Users\\LDT\\Desktop\\mestrado-unifesp\\db\\val_v2\\Sparisoma axillare_IP\\Sparisoma axillare_IP_95.png'
    image = cv2.imread(PATH_IMAGE_BUDIAO)
    
    #Por padrão a biblioteca cv2 utilizada a ordem de cores BGR. Temos que converter a imagem lida para RGB antes da execução do modelo.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    #Chama o endpoint e passa a imagem como parâmetro
    result = make_request(SERVICE_URL, image)
    
    #Mostra o resultado do modelo
    print(f"RESULT: {result}")
    
if __name__ == '__main__':
    main()