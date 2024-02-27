# import PySimpleGUI as sg

# layout = [
#     [sg.Text('Olá Mundo')],
#     [sg.Text('Olá Mundo')],
#     [sg.Text('Olá Mundo')]
# ]

# janela = sg.Window('Titulo', layout, size=(500,500))

# while True:
#     evento, valores = janela.read()

#     if evento == sg.WIN_CLOSED:
#         break 

# janela.close()

# import PySimpleGUI as sg


# #Tudo dentro da janela.
# layout = [
#     [sg.Text('Texto na primeira linha')],
#     [sg.Text('Digite alguma coisa: '), sg.InputText()],
#     [sg.Text('Digite outra coisa: '), sg.InputText()],
#     [sg.Button('OK'), sg.Button('Cancelar')]
# ]

# #Criando a Janela
# Janela = sg.Window('Titulo da Janela', layout)

# #Laço do evento para processar "eventos" e receberos "valores" obs input
# while True:
#     evento, valores = Janela.read()

#     if evento == sg.WIN_CLOSED or evento == 'Cancelar': #Se o usuario fechar
#         break

#     sg.popup(f'Você digitou {valores[0]}')

# Janela.close()

import json
import PySimpleGUI as sg

with open('arquivo.json') as arquivo:
    texto = arquivo.read()

lista = list(json.loads(texto))

#Tudo dentro da janela.
layout = [
    [sg.Text('preencha com seus dados')],
    [sg.Text('Digite seu nome: '), sg.InputText(key='nome')],
    [sg.Text('Digite sua idade: '), sg.InputText(key='idade')],
    [sg.Text('Digite seu telefone: '), sg.InputText(key='telefone')],
    [sg.Text('Digite a cor que deseja o sobretudo: '), sg.InputText(key='sobretudo')],
    [sg.Button('OK'), sg.Button('Mostrar'), sg.Button('Cancelar')]
]

#Criando a Janela
Janela = sg.Window('Deseja entrar para os Peaky blinders?', layout, size=(500,200))

#Laço do evento para processar "eventos" e receber os "valores" obs input
while True:
    evento, valores = Janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Cancelar': #Se o usuario fechar
        break

    lista.append(valores)
    novo_texto = json.dumps(lista, indent=4)
    with open('arquivo.json', 'w') as arquivo:
        arquivo.write(novo_texto)

    if evento == 'Mostrar':
        sg.popup(novo_texto)

Janela.close()


