import pandas as pd
import pickle
from time import sleep
filename = 'modelo_titanic.pkl'

res = pickle.load(open(filename, 'rb'))

lr = res['resultados']
escala = res['escala'][0]
print("🥶"*30)
print(f"🚢 TITANIC: SIMULADOR \n\n\n")

decisao = "c"
cont = 1
while decisao.lower() == "c":
    
    print(f"SIMULAÇÃO {cont}...\n")

    sexo = input("Q1. Informe seu Sexo (M ou F): ")
    if sexo.upper not in ['M', 'F', 'Masculino', 'Feminino']:
        sexo = input("Q1. Digite apenas M ou F: ")

    if sexo.upper() in ["M", "Masculino"]:
        sexo = True
    else:
        sexo = False


    age = int(input("Q2. Informe sua idade: "))
    age = (age - escala['age'][0])/(escala['age'][1] - escala['age'][0])

    X_form = pd.DataFrame({
        'age': [age], 'sibsp': [0.361169], 'parch': [0], 'fare': [0.412503],
        'pclass_2': [False], 'pclass_3': [False], 
        'sex_male': [sexo],
        'embarked_Q': [False], 'embarked_S': [True]
    })

    sleep(1)
    print("Treinando o modelo....")

    for i in range(1,11):
        print(f'Iteração preditiva {i}...')
        sleep(0.05)

    classe = lr.predict(X_form.loc[[0]])[0]
    if classe == 1:
        rotulo = "Sobreviveria"
    else:
        rotulo = "Morreria"

    prob = lr.predict_proba(X_form.loc[[0]])[0][classe]*100


    print(f"Classificação prevista.... Em 1912, você {rotulo.upper()} com {prob:3.1f}% de chances!")
    cont = cont + 1 

    decisao = input('Quer fazer outra simulação? (Digite C para continuar): ')

print("Obrigado!!!")
