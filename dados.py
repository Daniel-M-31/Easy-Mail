import json
import os
import envia_mail


def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


diretorio_imagen = resource_path('icone')
caminho_icone = os.path.join(diretorio_imagen, 'icone_mail.ico')


login_efetuado = False
contatos = None

#variaveis de controle do login
if os.path.exists('login.json'):
    login_efetuado = True
    with open("login.json", "r") as arquivo:
        dados_login = json.load(arquivo)
    envia_mail.inicializa_conteudo(dados_login)

else:
    login_efetuado = False
    dados_login = {"nome": 'sem usuario',
                   "senha": 'sem senha'}

#variaveis de controle de dados de caixa
posy = 0

#armazenamento de contatos
def verifica_contatos():
    global contatos
    if os.path.exists('contatos.json'):
        with open("contatos.json", "r") as arquivo:
            contatos = json.load(arquivo)
    else:
        contatos = []

def inicializaçao_SMTP():
    global dados_login
    envia_mail.inicializa_conteudo(dados_login)

#conversao de dados
def converte_dados_login(dado):
    global dados_login
    envia_mail.cadastro_email(dado)
    dado = dado['nome']
    with open('login.json', 'w') as arquivo:
        json.dump(dado, arquivo)
    dados_login = dado

def converte_dado_contato(dado):
    with open('contatos.json', 'w') as arquivo:
        json.dump(dado, arquivo)

def converte_dados_posy(dado):
    with open('posy_contato.json', 'w') as arquivo:
        json.dump(dado, arquivo)


def converte_dados_assunto(dado):
    with open('assunto.json', 'w') as arquivo:
        json.dump(dado, arquivo)

def converte_dados_doc(dado):
    with open('documento.json', 'w') as arquivo:
        json.dump(dado, arquivo)

def converte_dados_link(dado):
    with open('link.json', 'w') as arquivo:
        json.dump(dado, arquivo)

def converte_dados_imagem(dado):
    with open('imagen.json', 'w') as arquivo:
        json.dump(dado, arquivo)

#atualizçao posicional
def atualiza_posy():
    global posy
    if os.path.exists('posy_contato.json'):
        with open("posy_contato.json", "r") as arquivo:
            dados_posy = json.load(arquivo)
        posy = dados_posy
    else:
        pass

#funcoes de envio de dado e-mail
def envia_email(des, ass, cont, cam):
    envia_mail.envia_email(des, ass, cont, cam)

#deleta dados:
def deleta_dado(dado):
    os.remove('{}'.format(dado))