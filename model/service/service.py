import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, Text
from tensorflow.keras.applications.inception_v3 import preprocess_input
import cv2
import pickle

#Essa tag foi gerada no momento em que o modelo foi salvo no Bento.
#Ela pode ser vista rodando o comando 'bentoml models list' no prompt de comando.
INCEPTION_BENTO_MODEL_TAG =  'inception_sgd_0.05_ckpnt_model:xgugbmq3n6tns7fs'
INCEPTION_MODEL_PICKLE_PATH = 'E:\\mestrado-unifesp-vscode\\model\\inception\\budioes_inception_v2_SGD_0.05.pickle'

RESNET_BENTO_MODEL_TAG =  'resnet_adam_0.001_ckpnt_model:oiavi5y3toov27fs'
RESNET_MODEL_PICKLE_PATH = 'E:\\mestrado-unifesp-vscode\\model\\resnet\\budioes_resnet_Adam_0.001.pickle'

VGG_BENTO_MODEL_TAG = 'vgg_sgd_0.001_ckpnt_model:lu2n52i3x2coq7fs'
VGG_MODEL_PICKLE_PATH = 'E:\\mestrado-unifesp-vscode\\model\\vgg\\budioes_vgg_SGD_0.001.pickle'

#Aloca em memória o modelo salvo anteriormente
classifier_runner_inception = bentoml.keras.get(INCEPTION_BENTO_MODEL_TAG).to_runner()
classifier_runner_resnet = bentoml.keras.get(RESNET_BENTO_MODEL_TAG).to_runner()
classifier_runner_vgg = bentoml.keras.get(VGG_BENTO_MODEL_TAG).to_runner()

#Criar um serviço com o endpoint do modelo. Faremos 1 serviço para todos os modelos (Inception, VGG e Resnet)
classifier = bentoml.Service("classifier", runners=[classifier_runner_inception,classifier_runner_resnet,classifier_runner_vgg])

@classifier.api(input=Text(),output=Text())
def classify_inception(input_data: str) -> str:
    
    #1) Redimensionamento:
    #Durante o treino a rede Inception esperava como input um conjunto com dimensão 299x299x3 (RGB).
    #Por esse motivo é necessário redimencionar a image recebida para essa configuração. Não precisa passar o último canal do RGB (3) como parâmetro.
    print("========= call ml ANTES ==========")
    print(input_data)
    print("========= call ml DEPOIS ==========")
    image = cv2.imread(input_data.replace("\"",""))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("Redimensionamento...")
    image = cv2.resize(image, (299,299))
    #2) preprocess_input:
    #Durante o treino a foi aplicada a função "preprocess_input", que modifica os valores da imagem para facilitar o processamento da rede inception.
    #Por esse motivo é necessário aplicar o preprocess_input
    print("preprocess_input...")
    image = preprocess_input(image)
    
    #3) A rede espera uma lista de imagens para processar. No caso, iremos passar como parâmetro o array de 1 imagem.
    #Esse array deve ter index 0. Essa etapa do código adiciona esse índice ao array usado de input (dimensão do batch).
    print("expand dimensions...")
    image = np.expand_dims(image, axis=0)

    #Rodar o modelo, como o resultado é um array de 1 imagem temos que selecionar o índice 0.
    print("runner_result...")
    runner_result = classifier_runner_inception.predict.run(image)[0]
    print(f"runner_result... {runner_result}")
    #Dentro do índice 0 há outro array contendo as classificações prováveis. No caso temos 3 classes de budiões, vamos ter o índice 0, 1 e 2 disponívels.
    #Seleciona o índice da classe mais provável e busca no arquivo .pickle o nome da classe de budiões correspondente. 
    #O arquivo .pickle foi gerado durante o treino do modelo, ele contém uma lista com as 3 classes de budiões utilizadas no modelo.
    print("runner_result index...")
    runner_result_idx = np.argmax(runner_result)
    print(f"runner_result_idx... {runner_result_idx}")
    
    print("load pickle...")
    labels = pickle.loads(open(INCEPTION_MODEL_PICKLE_PATH,"rb").read()) #rd = read byte
    print(f"labels classes... {labels.classes_[runner_result_idx]}")
    
    print("return labels...")
    return labels.classes_[runner_result_idx]

@classifier.api(input=NumpyNdarray(),output=Text())
def classify_resnet(input_data: np.ndarray) -> str:
    print(input_data)
    #1) Redimensionamento:
    image = cv2.resize(input_data.astype('float32'), (224,224))
    #1) A rede espera uma lista de imagens para processar. No caso, iremos passar como parâmetro o array de 1 imagem.
    #Esse array deve ter index 0. Essa etapa do código adiciona esse índice ao array usado de input (dimensão do batch)
    image = np.expand_dims(image, axis=0)
    #Rodar o modelo, como o resultado é um array de 1 imagem temos que selecionar o índice 0
    runner_result = classifier_runner_resnet.predict.run(image)[0]
    #Seleciona o índice da classe mais provável e busca no arquivo .pickle o nome da classe de budiões correspondente. 
    runner_result_idx = np.argmax(runner_result)
    labels = pickle.loads(open(RESNET_MODEL_PICKLE_PATH,"rb").read()) #rd = read byte
    return labels.classes_[runner_result_idx]


@classifier.api(input=NumpyNdarray(),output=Text())
def classify_vgg(input_data: np.ndarray) -> str:
    print(input_data)
    #1) Redimensionamento:
    image = cv2.resize(input_data.astype('float32'), (224,224))
    #1) A rede espera uma lista de imagens para processar. No caso, iremos passar como parâmetro o array de 1 imagem.
    #Esse array deve ter index 0. Essa etapa do código adiciona esse índice ao array usado de input (dimensão do batch)
    image = np.expand_dims(image, axis=0)
    #Rodar o modelo, como o resultado é um array de 1 imagem temos que selecionar o índice 0
    runner_result = classifier_runner_vgg.predict.run(image)[0]
    #Seleciona o índice da classe mais provável e busca no arquivo .pickle o nome da classe de budiões correspondente. 
    runner_result_idx = np.argmax(runner_result)
    labels = pickle.loads(open(VGG_MODEL_PICKLE_PATH,"rb").read()) #rd = read byte
    return labels.classes_[runner_result_idx]