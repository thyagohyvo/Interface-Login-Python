from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('DarkBlue9')
layout = [

    [sg.Text ('Usuário'), sg.Input(key= 'usuario', size=(25,1))],
    [sg.Text('Senha  '),  sg.Input(key='senha', password_char='*', size=(25,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'thyago' and valores ['senha'] == '123456':
            print('Ben-vindo')