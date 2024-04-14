import PySimpleGUI as sg;
import tkinter as tk;
import string;
import random;


#user interface
sg.theme('Dark Blue 3');
layout = [
[sg.Image('img/gerar.png', pad =(0,(0,10)))],

[sg.Text('quantidade de digitos:', font='Heveltica 15'),sg.Input(size=(3,1), font='heveltica 15', key='tamanho')],
[sg.Text('senha:', font='Heveltica 15')],
[sg.InputText(size=(25,1),font=('Arial 20'), pad =(0,(0,10)),key='saida')],
[sg.Button('GERAR', size=(8,1), font=('Arial 15'))],
]
# commands
poupW = sg.Window('Gerador de Senhas',layout=layout, element_justification='center',finalize=True)

while True:
    event,values = poupW.read()
    if event == sg.WINDOW_CLOSED:
        break;
    elif event == 'GERAR' and values['tamanho'] == '':
            sg.popup('informe a quantidade de digitos !')
            continue
    elif event == 'GERAR':
        cond = string.ascii_letters + string.digits + '!@#$%&*()/><'
        rand = random.SystemRandom()
        poupW['saida'].update(''.join(rand.choice(cond)for i in range(int(values['tamanho']))))