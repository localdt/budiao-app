import json
import numpy as np
import requests
import cv2
import pickle

url = 'http://localhost:3000/classify'

def makeRequest(service_url: str, input=np.ndarray) -> np.ndarray:
    serialized = json.dumps(input.tolist())
    response = requests.post(url=service_url, data=serialized, headers={'content_type':'application/json'})
    return np.array(response.json())


def main():
    lb = pickle.loads(open("C:\\Users\\LDT\\Desktop\\mestrado-unifesp\\budioes.pickle", "rb").read())
    input_image = cv2.imread('C:\\Users\\LDT\\Desktop\\mestrado-unifesp\\db\\train\\Sparisoma axillare_IP\\Sparisoma axillare_IP_251.jpeg')
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    prediction = makeRequest(url, input_image)
    idx = np.argmax(prediction[0])
    label = lb.classes_[idx]
    print('É um ' + label)

if __name__ == '__main__':
    main()