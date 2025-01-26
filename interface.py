#conversação, gerenciamento e envio de dados
import dados
#criação de uma interfce e gerenciamento de eventos
import tkinter as tk
from tkinter import filedialog
#atalhos para variaveis especificas
import chaves

#frame de login
class Frame1:
    def __init__(self, tela):
        #variavel que cria a tela para o frame de login
        self.tela = tela
        #variavel que armazena o conteudo escrito para a censura
        self.conteudo = ''
        #dicionario dos dados de registro do login
        self.dados_login = {'nome': None, 'senha': None}

    #criador de multimidia
    def cria_label(self, texto_label, Fonte_label, Tamanho_label, bg_label, fg_label, linha, coluna, dist_x, dist_y, rowspan, columnspan, borda):
        label = tk.Label(self.tela, text=texto_label, font=(Fonte_label, Tamanho_label), bg=bg_label, fg=fg_label)
        label.grid(row=linha, column=coluna, sticky=borda, padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)

    #criador de caixas de entrada de texto
    def cria_text_box_login(self, altura_box, largura_box, fonte_box, tamanho_box, bg_box, fg_box, row_box, column_box, dist_x, dist_y, usuario_senha, rowspan, columnspan, borda):
        box = tk.Text(self.tela, height=altura_box, width=largura_box, font=(fonte_box, tamanho_box), bg=bg_box, fg=fg_box)
        box.grid(row=row_box, column=column_box, sticky=borda, padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)
        #verificador de eventos de digitaçao
        box.bind(chaves.digito, lambda event, caixa=box, width=largura_box: self.config_tamanho_box(caixa, width))
        #tratamento condicional da caixa
        if usuario_senha:
            box.bind(chaves.digito, lambda event, box=box: self.manipula_dado_box(box, 'senha'))

        else:
            box.bind(chaves.digito, lambda event, box=box: self.manipula_dado_box(box, 'nome'))

    #tratamento de dados e eventos de caixa de entrada de texto
    def config_tamanho_box(self, box, largura_box):
        caracteres = box.get('1.0', 'end-1c')
        row_box = (len(caracteres)-6)//largura_box + 1
        box.config(height=row_box)

    def manipula_dado_box(self, box, verbete):
        if verbete == 'nome':
            self.dados_login['nome'] = box.get('1.0', tk.END).strip()
        else:
            dados = box.get('1.0', tk.END).strip()
            self.conteudo += dados
            box.delete('1.0', tk.END)
            box.insert('1.0', "*" * len(dados))
            self.conteudo=self.conteudo.replace("*", "")
            self.dados_login['senha'] = self.conteudo

    #criador de botoe
    def cria_button(self, texto_button, bg_button, fg_button, fonte_button, tam_button, command_button, linha_button, column_button, dist_x, dist_y, rowspan, columnspan, borda):
        button = tk.Button(self.tela, text=texto_button, bg=bg_button, fg=fg_button, font=(fonte_button, tam_button), command=command_button)
        button.grid(row=linha_button, column=column_button, sticky=borda, padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)

    #sessao de comando
    def command_troca(self):
        test.frame_login.grid_forget()
        test.frame_usuario.grid(row=0, column=0, sticky="nsew")

    def commad_login(self):
        if self.dados_login['senha']!= None and self.dados_login['nome'] != None:
            dados.converte_dados_login(self.dados_login)
            test.elementos_usuario()
            self.command_troca()
        else:
            pass

#frame_intermediario de interaçao de usuario
class Frame2:
    def __init__(self, tela):
        #variavel que cria a tela usavel
        self.tela = tela
        #atualiza a posiçao dos labels de contato
        dados.atualiza_posy()
        #entradas e registro de entradas do usuario
        self.contato = None
        self.destinatario = ''
        dados.verifica_contatos()
        self.linha = dados.posy
        self.lista_contatos = dados.contatos
        #armazenamento multi-telas
        self.conteiner = []
        #construçao das multi-telas
        self.cria_contenier(0, 3, 8, 3, 'nsew', cor=chaves.Cinza_prata, width=200, height=800, padx=0, pady=0)
        self.cria_canvas(self.conteiner[0], 'vertical', rowspan=8, columnspan=4)
        self.cria_contenier(0, 11, 2, 13, 'nsew', cor=chaves.Cinza_chumbo, width=1367, height=100, padx=0, pady=0)
        self.cria_contenier(4, 3, 4, 4,'nse', cor=chaves.Cinza_chumbo, width=530, height=380, padx=20, pady=0)
        self.cria_contenier(14, 0, 13, 2, 'nsw', cor=chaves.Cinza_chumbo, width=270+200, height=0, padx=0, pady=0 )
        #exibiçao dos contatos ja registrados
        self.cria_contatos_init()

    #contruçao de telas simples
    def cria_contenier(self, coluna, linha, rowspan, columnspan, borda, cor, width, height, padx, pady):
        contenier = tk.Frame(self.tela,  width=width, height=height)
        contenier.grid(row=linha, column=coluna, sticky=borda, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady)
        contenier.config(bg=cor)
        self.conteiner.append(contenier)
    #construçao de telas com mais funcionalidades
    def cria_canvas(self, frame, orient, rowspan, columnspan):
        canvas = tk.Canvas(frame, bg=chaves.Cinza_prata, width=500, height=500)
        scrollbar = tk.Scrollbar(frame, orient=orient, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=chaves.Cinza_prata)

        # Configurar canvas e scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
        scrollbar.grid(row=0, column=4, rowspan=rowspan, sticky="ns")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        self.conteiner.append(scrollable_frame)
        self.conteiner.append(canvas)

    #cria a exibiçao de contatos ja registrados
    def cria_contatos_init(self):
        if self.lista_contatos != []:
            posy = 0
            for i in self.lista_contatos:
                self.cria_label(i, chaves.Padrao, chaves.full_screen_pequeno, chaves.Cinza_prata, chaves.Preto, posy, 0, 0, 0, columnspan=2, rowspan=1, borda='nsew', tela=self.conteiner[1])
                posy += 1
                self.conteiner[2].update_idletasks()
                self.conteiner[2].configure(scrollregion=self.conteiner[2].bbox("all"))

    #cria um elemento multimidia
    def cria_label(self, texto_label, Fonte_label, Tamanho_label, bg_label, fg_label, linha, coluna, dist_x, dist_y, rowspan, columnspan, borda, tela):
        label = tk.Label(tela, text=texto_label, font=(Fonte_label, Tamanho_label), bg=bg_label, fg=fg_label)
        label.grid(row=linha, column=coluna, sticky=borda, padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)
        if type(dados.dados_login) == dict or texto_label != dados.dados_login + '(Você)':
            label.bind(chaves.sobrepos,lambda event, evento=chaves.sobrepos, Label=label, email=texto_label: self.events_label(Label, evento,email))
            label.bind(chaves.off_sobrepos,lambda event, evento=chaves.off_sobrepos, Label=label, email=texto_label: self.events_label(Label, evento, email))
            label.bind(chaves.click,lambda event, evento=chaves.click, Label=label, email=texto_label: self.events_label(Label,evento,email))

    #tratamento de evento do multimidia
    def events_label(self, label, evento, nome_conversa):
        # controla os atos de acordo com o evento em um label expecifico
        if evento == chaves.sobrepos:
            label.config(fg=chaves.Azul_royal)
        if evento == chaves.off_sobrepos:
            label.config(fg=chaves.Preto)
        if evento == chaves.click:
            self.destinatario = nome_conversa
            test.frame_3 = Frame3(self.conteiner[4], self.destinatario)
            test.elementos_conversa()

    #cria uma caixa de entrada de texto
    def cria_text_box(self, altura_box, largura_box, fonte_box, tamanho_box, bg_box, fg_box, row_box, column_box, dist_x, dist_y, rowspan, columnspan, borda):
        box = tk.Text(self.tela, height=altura_box, width=largura_box, font=(fonte_box, tamanho_box), bg=bg_box, fg=fg_box)
        box.grid(row=row_box, column=column_box, sticky=borda, padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)
        box.bind(chaves.digito, lambda event, caixa=box, width=largura_box: self.config_tamanho_box(caixa, width))
        box.bind(chaves.digito, lambda event, caixa=box: self.manipula_dado_box(caixa))

    #eventos da caixa de texto
    def config_tamanho_box(self, box, largura_box):
        caracteres = box.get('1.0', 'end-1c')
        row_box = (len(caracteres)-6)//largura_box + 1
        box.config(height=row_box)

    def manipula_dado_box(self, email):
        self.contato = email.get('1.0', tk.END).strip()

    #cria um botao
    def cria_button(self, texto_button, bg_button, fg_button, fonte_button, tam_button, command_button, linha_button, column_button, dist_x, dist_y, rowspan, columnspan, borda, tela):
        button = tk.Button(tela, text=texto_button, bg=bg_button, fg=fg_button, font=(fonte_button, tam_button), command=command_button)
        button.grid(row=linha_button, column=column_button, sticky=borda, padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)

    #sessao de comando
    def commad_adiciona_caixa_and_button(self):
        self.cria_button('Pronto', chaves.Cinza_prata, chaves.Preto, chaves.Padrao, chaves.full_screen_pequeno, self.commad_adiciona_contato, 2, 2, 0, 0, columnspan=1, rowspan=1, borda='nsew', tela=self.tela)
        self.cria_text_box(1, 20, chaves.Padrao, chaves.full_screen_pequeno, chaves.Cinza_claro, chaves.Preto, 2, 1, 0, 0, columnspan=1, rowspan=1, borda='nsew')

    def commad_adiciona_contato(self):
        if self.contato != None:
            if '@' in self.contato and ('.com' in self.contato or '.ce' in self.contato or '.br' in self.contato or '.emi' in self.contato or '.gov' in self.contato):
                if self.contato != dados.dados_login:
                    if self.contato not in self.lista_contatos:
                        self.lista_contatos.append(self.contato)
                        dados.converte_dado_contato(self.lista_contatos)
                        self.linha += 1
                        dados.converte_dados_posy(self.linha)
                        dados.atualiza_posy()
                        self.linha = dados.posy
                        self.cria_label(self.contato, chaves.Padrao, chaves.full_screen_pequeno, bg_label=chaves.Cinza_prata, fg_label=chaves.Preto, linha=self.linha, coluna=0, dist_x=0, dist_y=0, columnspan=2, rowspan=1, borda='nsew', tela=self.conteiner[1])
                        self.conteiner[2].update_idletasks()
                        self.conteiner[2].configure(scrollregion=self.conteiner[2].bbox("all"))
                        self.contato = None
        else: pass

    def command_reseta_contatos(self):
        dados.deleta_dado('contatos.json')
        dados.deleta_dado('posy_contato.json')
        test.frame_usuario.destroy()
        test.frame_usuario = tk.Frame(test.tela)
        test.frame_usuario.grid(row=0, column=0, sticky="nsew")
        test.frame_2 = Frame2(test.frame_usuario)
        test.elementos_usuario()
    def command_reseta_login(self):
        dados.deleta_dado('login.json')
        test.frame_usuario.grid_forget()
        test.frame_login.grid(row=0, column=0, sticky="nsew")
    def command_reseta_all(self):
        dados.deleta_dado('contatos.json')
        dados.deleta_dado('login.json')
        dados.deleta_dado('posy_contato.json')
        test.frame_usuario.grid_forget()
        test.frame_login.grid(row=0, column=0, sticky="nsew")
        test.frame_usuario.destroy()
        test.frame_usuario = tk.Frame(test.tela)
        test.frame_usuario.grid(row=0, column=0, sticky="nsew")
        test.frame_usuario.grid_forget()
        test.frame_2 = Frame2(test.frame_usuario)

#frame de conversa do usuario
class Frame3:
    def __init__(self, tela, destinnatario):
        # variavel que cria a tela usavel
        self.tela = tela
        #define o destinatario
        self.destinnatario = destinnatario
        self.cria_label(self.destinnatario, chaves.Padrao, chaves.full_screen_medio, chaves.Cinza_chumbo, chaves.Branco_neve, 0, 0, 0,
                        0, rowspan=2, columnspan=3)
        #informaçoes para o envio de email
        self.assunto = ''
        self.link = None
        self.tema = ''
        self.remetente = dados.dados_login
        self.arquivo = None
        self.texto_link = ''

    #cria um elemento multimidia
    def cria_label(self, texto_label, Fonte_label, Tamanho_label, bg_label, fg_label, linha, coluna, dist_x, dist_y, rowspan, columnspan):
        label = tk.Label(self.tela, text=texto_label, font=(Fonte_label, Tamanho_label), bg=bg_label, fg=fg_label)
        label.grid(row=linha, rowspan=rowspan, column=coluna, columnspan=columnspan, sticky="nsew", padx=dist_x, pady=dist_y)
        test.elementos_exibiçao.append(label)

    #cria uma caixa de entrada de texto
    def cria_text_box(self, altura_box, largura_box, fonte_box, tamanho_box, bg_box, fg_box, row_box, column_box,
                      dist_x, dist_y, ass, link, rowspan, columnspan):
        box = tk.Text(self.tela, height=altura_box, width=largura_box, font=(fonte_box, tamanho_box), bg=bg_box,
                      fg=fg_box)
        box.grid(row=row_box, column=column_box, sticky="nsew", padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)
        box.bind(chaves.digito, lambda event, caixa=box, width=largura_box: self.config_tamanho_box(caixa, width))
        box.bind(chaves.digito, lambda event, box=box, ass=ass, link=link: self.manipula_dado_box(box, ass, link))
        test.elementos_exibiçao.append(box)

    #eventos da caixa
    def config_tamanho_box(self, box, largura_box):
        caracteres = box.get('1.0', 'end-1c')
        row_box = (len(caracteres) - 6) // largura_box + 1
        box.config(height=row_box)

    def manipula_dado_box(self, email, ass, link):
        if ass:
            if email.get('1.0', tk.END) == None:
                pass
            else:
                self.tema = email.get('1.0', tk.END)
        elif link:
            self.link = email.get('1.0', tk.END)
        else:
            self.assunto = email.get('1.0', tk.END)

    #cria botoes
    def cria_button(self, texto_button, bg_button, fg_button, fonte_button, tam_button, command_button, linha_button,
                    column_button, dist_x, dist_y, rowspan, columnspan):
        button = tk.Button(self.tela, text=texto_button, bg=bg_button, fg=fg_button, font=(fonte_button, tam_button),
                           command=command_button)
        button.grid(row=linha_button, column=column_button, sticky="nsew", padx=dist_x, pady=dist_y, rowspan=rowspan, columnspan=columnspan)
        test.elementos_exibiçao.append(button)
        if texto_button == 'Anexar arquivo':
            self.anexar_arquivo =  button
        elif texto_button == 'enviar':
            self.enviar = button
        elif texto_button == 'Anexar link':
            self.anexar_link = button
    #sessao de comandos
    def command_evio(self):
        if self.link != None:
            self.assunto = self.assunto + '{}'.format(self.anexo_link)
        dados.envia_email(self.destinnatario, self.tema, self.assunto, self.arquivo)
        self.confirma_evento(self.enviar)

    def command_troca(self):
        for i in test.elementos_exibiçao:
            i.destroy()

    def command_abrir_explorador(self):
        #Abre uma janela para o usuário selecionar um arquivo.
        self.arquivo = filedialog.askopenfilename(title="Selecione um arquivo")
        self.confirma_evento(self.anexar_arquivo)
    def command_link(self):
        self.anexo_link = "<a href='{}'>Clique aqui</a>".format(self.link)
        self.confirma_evento(self.anexar_link)

    def command_caixa_link(self):
        self.cria_text_box(1, 10, chaves.Padrao, chaves.full_screen_medio, bg_box=chaves.Cinza_claro,
                                   fg_box=chaves.Preto, row_box=7, column_box=1, dist_y=0, dist_x=0, ass=False, link=True, rowspan=1, columnspan=1)
        self.cria_button('Anexar link', chaves.Cinza_prata, fg_button= chaves.Preto, fonte_button= chaves.Padrao, tam_button= chaves.full_screen_medio, command_button=self.command_link, linha_button=7, column_button=2 , dist_y=0, dist_x=0, rowspan=1, columnspan=1)

    def confirma_evento(self, button):
        button.config(bg=chaves.verde_claro)


#gerenciador de frames
class interface:
    def __init__(self):
        #inicia a tela principal
        self.tela = tk.Tk()
        self.tela.title(chaves.titulo)
        self.tela.config(bg=chaves.Cinza_escuro)
        self.tela.rowconfigure(0, weight=1)
        self.tela.columnconfigure(0, weight=1)
        #ativa a tela cheia
        self.tela.state('zoomed')
        #elementos exibidos no frame 3
        self.elementos_exibiçao = []
        #cria os frames
        self.cria_frames()
        #inicializa as outras classes
        self.frame_1 = Frame1(self.frame_login)
        self.frame_2 = Frame2(self.frame_usuario)
        self.frame_3 = None

    #cria os frames
    def cria_frames(self):
        self.frame_login = tk.Frame(self.tela)
        self.frame_login.grid(row=0, column=0, sticky="nsew")
        self.frame_login.config(bg=chaves.Cinza_escuro)
        self.frame_usuario = tk.Frame(self.tela)
        self.frame_usuario.grid(row=0, column=0, sticky="nsew")
        self.frame_usuario.grid_forget()
        self.frame_usuario.config(bg=chaves.Cinza_escuro)

    #Define em qual forma os elementos serao exibidos
    def element_login(self):
        if not dados.login_efetuado:
            self.frame_usuario.grid_forget()

        else:
            self.frame_usuario.grid(row=0, column=0, sticky="nsew")
            self.frame_login.grid_forget()

        #labels
        self.frame_1.cria_label('Easy Mail', chaves.Padrao, chaves.full_screen_grande, bg_label=chaves.Cinza_escuro, fg_label=chaves.Preto, linha=0, coluna=6, dist_y=0, dist_x=55, columnspan=4, rowspan=2, borda='nsew')

        self.frame_1.cria_label('Seu E-mail:', chaves.Padrao, chaves.full_screen_medio, bg_label=chaves.Cinza_escuro,
                                fg_label=chaves.Preto, linha=1+6, coluna=1, dist_y=40, dist_x=75, columnspan=1, rowspan=2, borda='nsew')

        self.frame_1.cria_label('Sua senha:', chaves.Padrao, chaves.full_screen_medio, bg_label=chaves.Cinza_escuro,
                                fg_label=chaves.Preto, linha=3+7, coluna=1, dist_y=40, dist_x=75, columnspan=1, rowspan=2, borda='nsew')

        #caixas de texto
        self.frame_1.cria_text_box_login(1, 20, chaves.Padrao, chaves.full_screen_medio, chaves.Cinza_claro, chaves.Preto, 2+7, 1, 75, 0, False, columnspan=1, rowspan=1, borda='ew')
        self.frame_1.cria_text_box_login(1, 20, chaves.Padrao, chaves.full_screen_medio, chaves.Cinza_claro, chaves.Preto, 4+8,
                                         1, 75, 0, True, columnspan=1, rowspan=1, borda='ew')

        #butoes
        self.frame_1.cria_button('Logar', chaves.Cinza, chaves.Preto, chaves.Padrao, chaves.full_screen_medio, self.frame_1.commad_login, linha_button=4+10, column_button=1, dist_x=75, dist_y=40, columnspan=1, rowspan=1, borda='ew')

    # Define em qual forma os elementos serao exibidos
    def elementos_usuario(self):
        dado = dados.dados_login + '(Você)'
        self.frame_2.cria_label(dado, chaves.Padrao, chaves.full_screen_pequeno, chaves.Cinza_escuro, chaves.Preto,
                                0, 0, 0, 0, columnspan=3, rowspan=1, borda='nsew', tela=self.frame_2.tela)
        self.frame_2.cria_button('+', chaves.Cinza_prata, chaves.Preto, fonte_button=chaves.Padrao,
                                 tam_button=chaves.full_screen_pequeno,
                                 command_button=self.frame_2.commad_adiciona_caixa_and_button, linha_button=2,
                                 column_button=0, dist_x=0, dist_y=0, columnspan=1, rowspan=1, borda='nsew', tela=self.frame_2.tela)

        self.frame_2.cria_button('reseta login', chaves.Cinza_prata, chaves.Preto, fonte_button=chaves.Padrao,
                                 tam_button=chaves.tamanho_pequeno, command_button=self.frame_2.command_reseta_login,
                                 linha_button=0, column_button=6, dist_x=0, dist_y=0, columnspan=1, rowspan=1, borda='nsew', tela=self.frame_2.conteiner[3])

        self.frame_2.cria_button('reseta contatos', chaves.Cinza_prata, chaves.Preto, fonte_button=chaves.Padrao,
                                 tam_button=chaves.tamanho_pequeno, command_button=self.frame_2.command_reseta_contatos,
                                 linha_button=1, column_button=6, dist_x=0, dist_y=7, columnspan=1, rowspan=1, borda='nsew', tela=self.frame_2.conteiner[3])

        self.frame_2.cria_button('reseta tudo', chaves.Cinza_prata, chaves.Preto, fonte_button=chaves.Padrao,
                                 tam_button=chaves.tamanho_pequeno, command_button=self.frame_2.command_reseta_all,
                                 linha_button=2, column_button=6, dist_x=0, dist_y=0, columnspan=1, rowspan=1, borda='nsew', tela=self.frame_2.conteiner[3])

    # Define em qual forma os elementos serao exibidos
    def elementos_conversa(self):

        self.frame_3.cria_label('Assunto', chaves.Padrao, chaves.full_screen_medio, bg_label=chaves.Cinza_escuro, fg_label=chaves.Preto, linha=1+1, coluna=0, dist_y=0, dist_x=0, rowspan=1, columnspan=1)
        self.frame_3.cria_text_box(1, 15, chaves.Padrao, chaves.full_screen_medio, bg_box=chaves.Cinza_claro, fg_box=chaves.Preto, row_box=2+1, column_box=0, dist_y=0, dist_x=0, ass=True, link=False, rowspan=1, columnspan=1)

        self.frame_3.cria_label('conversa', chaves.Padrao, chaves.full_screen_medio, bg_label=chaves.Cinza_escuro,
                                fg_label=chaves.Preto, linha=4+1, coluna=0, dist_y=0, dist_x=0, rowspan=1, columnspan=1)
        self.frame_3.cria_text_box(1, 15, chaves.Padrao, chaves.full_screen_medio, bg_box=chaves.Cinza_claro,
                                   fg_box=chaves.Preto, row_box=5+1, column_box=0, dist_y=0, dist_x=0, ass=False, link=False, rowspan=1, columnspan=1)
        self.frame_3.cria_button('enviar', chaves.Cinza_prata, fg_button= chaves.Preto, fonte_button= chaves.Padrao, tam_button= chaves.full_screen_medio, command_button=self.frame_3.command_evio, linha_button= 8, column_button= 1, dist_y=0, dist_x=0, rowspan=1, columnspan=2)

        self.frame_3.cria_button('<<<', chaves.Cinza_prata, fg_button= chaves.Preto, fonte_button= chaves.Padrao, tam_button=chaves.full_screen_medio, command_button=self.frame_3.command_troca, linha_button= 0+1, column_button= 7-4, dist_y=0, dist_x=0, rowspan=1, columnspan=1)

        self.frame_3.cria_button('Anexar arquivo', chaves.Cinza_prata, fg_button= chaves.Preto, fonte_button= chaves.Padrao, tam_button= chaves.full_screen_medio, command_button=self.frame_3.command_abrir_explorador, linha_button= 8, column_button= 0, dist_y=0, dist_x=0, rowspan=1, columnspan=1)

        self.frame_3.cria_button('Insira um link:', chaves.Cinza_prata, fg_button=chaves.Preto,
                                 fonte_button=chaves.Padrao, tam_button=chaves.full_screen_medio,
                                 command_button=self.frame_3.command_caixa_link, linha_button=6+1, column_button=0,
                                 dist_y=0, dist_x=0, rowspan=1, columnspan=1)


test = interface()
test.element_login()
if dados.login_efetuado:
    test.elementos_usuario()
else: pass
test.tela.mainloop()