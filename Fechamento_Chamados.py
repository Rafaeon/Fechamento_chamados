import time
import pyautogui as py
import pandas as pd
import numpy

tabela = pd.read_csv("teste2.csv", sep=';', encoding="latin")
print(tabela.head())

time.sleep(5)

def fechamento_chamado(chamado, tecnico, dataInicio, horaInicio, dataFechamento, horaFechamento):
    
    py.click(x=5471, y=470, clicks=2)
    time.sleep(3)
    py.write(str(chamado))#pesquisar chamado


    time.sleep(5)
    py.middleClick(x=5613, y=554)#abrir outra guia
    time.sleep(5)

    if py.pixelMatchesColor(3321, 432, (255, 255, 255), tolerance=10):
        print("Nova guia aberta com sucesso!")
    else:
        print("Erro ao abrir a nova guia.")
        return  # Encerrar a função se a nova guia não foi aberta com sucesso

    py.click(x=3629, y=15)

    
    time.sleep(3)
    
    py.moveTo(x=3321, y=432)

    py.scroll(-50000)
    time.sleep(5)

    py.click(x=5435, y=1133, clicks=4)
    time.sleep(5)
    py.write(str(tecnico))#nome do tecnico
    time.sleep(5)

    py.click(x=5459, y=1251)

    time.sleep(5)

    py.click(x=4571, y=419)


    time.sleep(3)
    

    py.scroll(50000)
    time.sleep(3)


    time.sleep(3)
    py.click(x=3321, y=432)#fechamento
    time.sleep(3)

    py.click(x=3545, y=453)
    py.write(str(dataInicio))#preencher data de inicio
    py.press("tab")
    time.sleep(2)

    py.write(str(horaInicio))
    py.press("tab")
    time.sleep(2)

    py.write(str(dataFechamento))#preencher data de fechamento
    py.press("tab")
    time.sleep(2)

    py.write(str(horaFechamento))
    py.press("tab",3)
    time.sleep(2)
    py.press("enter")


    time.sleep(3)
    py.click(x=4587, y=353)

    time.sleep(5)


    py.hotkey("ctrl", "w") #fechar guia do navegador


for index, row in tabela.iterrows():
    chamado = row['chamado']
    tecnico = row['tecnico']
    dataInicio = row['dataInicio']
    horaInicio = row['horaInicio']
    dataFechamento = row['dataFechamento']
    horaFechamento = row['horaFechamento']

    fechamento_chamado(chamado, tecnico, dataInicio, horaInicio, dataFechamento, horaFechamento)


    if index == len(tabela) - 1:
        break