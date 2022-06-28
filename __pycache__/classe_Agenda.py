from classe_Contato import *

class Agenda:
    def __init__(self):
        self.ListaContatos = []

    def salva_contatos(self):
        self.ListaContatos.append(Contato()) 

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('Cod:', self.listaContatos[i].cod,
            '- Nome:', self.listaContatos[i].nome,
            '- Telefone:', self.listaContatos[i].telefone)
            
            