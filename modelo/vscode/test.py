import keras
import pandas as pd

filepath = 'C:\\Users\\LDT\\Desktop\\mestrado-unifesp\\vscode\\Estudos\\Data\\Titanic\\train.csv'

df = pd.read_csv(filepath)

df['Sex']