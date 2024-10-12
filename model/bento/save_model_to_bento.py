from tensorflow import keras
import bentoml

#Carregando modelo selectionado para o bentoml e salvando na biblioteca de modelos do bento
#Essa etapa é feita apenas uma vez:
# 1) Execute o script 'save_model_to_bento.py' e o modelo será salvo no bento
# 2) Após executado o script, execute o comando 'bentoml models list' no prompt. Ele irá mostrar a tag gerada para o modelo.

#comandos: 
#python save_model_to_bento.py
#bentoml models list

#Model INCEPTION
path_to_model = 'C:\\Users\\LDT\\Desktop\\mestrado-unifesp-vscode\\model\\inception\\modelo_budioes_inception_v2_SGD_0.05-ckpnt.model'
model_name = 'inception_SGD_0.05_ckpnt_model'

#Model RESNETpip 
#path_to_model = 'C:\\Users\\LDT\\Desktop\\mestrado-unifesp-vscode\\model\\resnet\\modelo_budioes_resnet_Adam_0.001-ckpnt.model'
#model_name = 'resnet_Adam_0.001_ckpnt_model'

#Model VGG
#path_to_model = 'C:\\Users\\LDT\\Desktop\\mestrado-unifesp-vscode\\model\\vgg\\modelo_budioes_vgg_SGD_0.001-ckpnt.model'
#model_name = 'vgg_SGD_0.001_ckpnt_model'

model = keras.models.load_model(path_to_model)
bento_model = bentoml.keras.save_model(model_name, model)
print(f"Bento model tag = {bento_model.tag}")

