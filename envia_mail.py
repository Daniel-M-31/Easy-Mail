import yagmail
import keyring

#inicializaçao
yag = None
def inicializa_conteudo(user_name):
    global yag
    senha = keyring.get_password('gmail', user_name)
    yag = yagmail.SMTP(user=user_name, password=senha)

#criptografia e registro
def cadastro_email(cadastro):
    global yag
    keyring.set_password("gmail", cadastro['nome'], cadastro['senha'])
    senha = keyring.get_password('gmail', cadastro['nome'])
    yag = yagmail.SMTP(user= cadastro['nome'], password=senha)

#envio de email
def envia_email(des, ass, cont, caminho):
    global yag
    if caminho:  # Se caminho não for None
        yag.send(
            to= des,
            subject= ass,
            contents= cont,
            attachments= [caminho]
        )
    else:
        yag.send(
            to= des,
            subject= ass,
            contents= cont
        )