from classe_Agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()
        #entrada = input('1 - Novo Contato\n2 - Listar Contato\n0')
        while true: 
            entrada = input('1 - Novo Contato\n2 - Listar Contato\n0')
            if entrada == '1':
                agenda.salvar_contatos()
            elif entrada == '2':
                agenda.listar_contatos()
            elif entrada =='0':
                break
            else:
                print('opção invalida!!!')