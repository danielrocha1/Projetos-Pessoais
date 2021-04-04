# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:04:35 2020

@author: Warlord
"""

from tkinter import *
from tkinter import messagebox
import fdb

#conecta com o banco
con = fdb.connect(dsn= #aqui colocar informarções do dba)
cur = con.cursor()
cur.execute("SELECT CLI_COD FROM CLICLIENTES ORDER BY CLI_COD DESC")
cli_cod = cur.fetchall()
cod_cli = list((cli_cod[0]))
strings = [str(integer) for integer in cod_cli]
a_string = "".join(strings)
an_integer = int(a_string)
cod_cliente = an_integer
Cli_cod = cod_cliente + 1
            

#inicia a interface         
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer.pack()
        
        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = 20
        self.setimoContainer.pack()
        
        self.oitavoContainer = Frame(master)
        self.oitavoContainer["padx"] = 20
        self.oitavoContainer.pack()
        
        self.nonoContainer = Frame(master)
        self.nonoContainer["padx"] = 20
        self.nonoContainer.pack()
        
        self.decimoContainer = Frame(master)
        self.decimoContainer["padx"] = 20
        self.decimoContainer.pack()
        
        self.onzimoContainer = Frame(master)
        self.onzimoContainer["padx"] = 20
        self.onzimoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack(side=LEFT)
        
        self.cancelContainer = Frame(master)
        self.cancelContainer["padx"] = 20
        self.cancelContainer.pack(side=RIGHT)
        
        self.titulo = Label(self.primeiroContainer, text="Dados do Cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack()

        self.cpfLabel = Label(self.terceiroContainer, text="CPF:", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.terceiroContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack()
        
        self.endLabel = Label(self.quintoContainer, text="End.:", font=self.fontePadrao)
        self.endLabel.pack(side=LEFT)

        self.end = Entry(self.quintoContainer)
        self.end["width"] = 30
        self.end["font"] = self.fontePadrao
        self.end.pack()
        
        self.compLabel = Label(self.sextoContainer, text="Compl.:", font=self.fontePadrao)
        self.compLabel.pack(side=LEFT)

        self.comp = Entry(self.sextoContainer)
        self.comp["width"] = 30
        self.comp["font"] = self.fontePadrao
        self.comp.pack()
        
        self.obsLabel = Label(self.setimoContainer, text="Refer.:", font=self.fontePadrao)
        self.obsLabel.pack(side=LEFT)

        self.obs = Entry(self.setimoContainer)
        self.obs["width"] = 30
        self.obs["font"] = self.fontePadrao
        self.obs.pack()
        
        self.cepLabel = Label(self.oitavoContainer, text="Cep:", font=self.fontePadrao)
        self.cepLabel.pack(side=LEFT)

        self.cep = Entry(self.oitavoContainer)
        self.cep["width"] = 30
        self.cep["font"] = self.fontePadrao
        self.cep.pack()
        
        self.bairroLabel = Label(self.nonoContainer, text="Bairro:", font=self.fontePadrao)
        self.bairroLabel.pack(side=LEFT)

        self.bairro = Entry(self.nonoContainer)
        self.bairro["width"] = 30
        self.bairro["font"] = self.fontePadrao
        self.bairro.pack()
        
        self.cidadeLabel = Label(self.decimoContainer, text="Cidade:", font=self.fontePadrao)
        self.cidadeLabel.pack(side=LEFT)

        self.cidade = Entry(self.decimoContainer)
        self.cidade["width"] = 30
        self.cidade["font"] = self.fontePadrao
        self.cidade.pack()
        
        self.telefoneLabel = Label(self.onzimoContainer, text="Telefone:", font=self.fontePadrao)
        self.telefoneLabel.pack(side=LEFT)

        self.telefone = Entry(self.onzimoContainer)
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack()
                
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = ("Cadastrar")
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.autenticar_ok
        self.autenticar.pack()
        
       
        self.cancel = Button(self.cancelContainer)
        self.cancel["text"] = ("Cancelar")
        self.cancel["font"] = ("Calibri", "8")
        self.cancel["command"] = root.destroy
        self.cancel["width"] = 12
        self.cancel.pack()


        self.autenticar = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.autenticar.pack()
        self.cancelmsg = Label(self.cancelContainer, text="", font=self.fontePadrao)
        self.cancelmsg.pack(side=RIGHT)
        
        con = fdb.connect(dsn= #aqui colocar informarções do DBA
        )
        cur = con.cursor()
        
        
    
    def autenticar_ok(self):
            # cata os dados, formata no jeito correto e valida
            global t
            global cpf_
            t = bool
            Cli_cod = 'NULL'
            nome = self.nome.get()
            cpf2 = self.cpf.get()
            cpf_ = self.cpf.get()
            endereco = self.end.get()
            obs = self.obs.get()
            comp = self.comp.get()
            cep = self.cep.get()
            bairro = self.bairro.get()
            cidade = self.cidade.get()
            tel = self.telefone.get()
                      
            #formata o cpf e autentica
            if len(str(cpf_)) == 11:
              teste = str(cpf_)
              teste = teste.zfill(11)
              cpf1 = '{}.{}.{}-{}'.format(teste[:3], teste[3:6], teste[6:9], teste[9:])  
              t = self.validate_cpf(cpf1, cpf2, self.nome, self.end, self.obs, self.comp, self.cep, self.bairro, self.cidade, self.telefone)
            elif len(str(cpf_)) > 11:
               messagebox.showerror("ERRO!", "CPF com numeros demais!")   
            elif len(str(cpf_)) >= 0:
                messagebox.showerror("ERRO!", "Está faltando numero no CPF!")     
            cur = con.cursor()
            
            # pega o proximo codigo de cliente valido do banco 
            cur.execute("SELECT CLI_COD FROM CLICLIENTES ORDER BY CLI_COD DESC")
            cli_cod = cur.fetchall()
            cod_cli = list((cli_cod[0]))
            strings = [str(integer) for integer in cod_cli]
            a_string = "".join(strings)
            an_integer = int(a_string)
            cod_cliente = an_integer
            Cli_cod = cod_cliente + 1
            
            #pegas as informações que foram inseridas
            nome = self.nome.get()
            cpf2 = self.cpf.get()
            cpf_ = self.cpf.get()
            endereco = self.end.get()
            obs = self.obs.get()
            comp = self.comp.get()
            cep = self.cep.get()
            bairro = self.bairro.get()
            cidade = self.cidade.get()
            tel = self.telefone.get()
            self.empty_space(self.nome, self.end, self.obs, self.comp, self.cep, self.bairro, self.cidade, self.telefone)
            
            #caso as informações vitais estejam corretas, commit. 
            if t == True:
                 title = "Cadastrado!  Cliente:"
                 #insere os dados para a table e suas respectivas columns
                 cur.execute("INSERT INTO CLICLIENTES (EMP_COD, CLI_COD, CLI_DIGITO, CLI_RAZ, CLI_FAN,CLI_FUNDACAO, CLI_CGCCPF, CLI_INSCUF, CLI_INDENTIDADE, CLI_INDENT_EXP,CLI_CTPS, CLI_OUTROS, CLI_INSCMUN, CLI_SUFRA, CLI_EMAIL, CLI_HTTP, CLI_EAN,CLI_COD_FOR, CLI_PESSOA, CLI_PAR1, CLI_PAR2, CLI_PAR3, CLI_PAR4, CLI_STATUS,CLI_CONCEITO, CLI_CIVIL, CLI_SEXO, CLI_ESP, CLI_PAI, CLI_MAE, CLI_PROF, CLI_NACIO,CLI_BANCO, CLI_AGENCIA, CLI_CONTA, CLI_CONTATO, CLI_A_C, CAPITALREG, LIMITECRED, LIMITEDATA,LIMITEAUTO, SALDODEV, SALDOREN, SALDOJUR, SALDOCRE, DATAJUR, PRI_COM_DAT, PRI_COM_VAL,ULT_VIS_DAT, ULT_COM_DAT, ULT_COM_VAL, MAI_FAT_DAT, MAI_FAT_VAL, ATRAZO_DAT, ATRAZO_QTD, ATRAZO_TOT,ATRAZO_MAI, ATRAZO_MAIDT, ATRAZO_MED, FATURAS_QTD, FATURAS_TOT, FATURAS_MAI, FATURAS_MAIDT, FATURAS_MED,PROTESTO_QTD, PROTESTO_DAT, PROTESTO_VAL, CHEQUES_QTD ,CHEQUES_DAT ,CHEQUES_VAL, TOT_VENDAS_1, TOT_VENDAS_2,TOT_VENDAS_3, TOT_VENDAS_4, TOT_VENDAS_5, TOT_VENDAS_6, TOT_VENDAS_7, TOT_VENDAS_8, TOT_VENDAS_9, TOT_VENDAS_10,TOT_VENDAS_11, TOT_VENDAS_12, TOT_BONIFICADO, TOT_FATURADO, MODO_COBR, PRAZO_PAG, PRAZO_FRE, MODO_FIXO, PRAZO_FIXO,TRANSP_COD, VEN_COD, COMISSAO, COM_VND, DEPOSITAR, PED_DIAS, ORC_FLAG, TAB_COD, TAB_FIXO, ETIQUETA_STATUS, SPC_DATA,SPC_CARTAS, REFERENCIA, OBSERVACAO, OBS_FIN, TIT_COD, GRUPO_CLI, COR_VENCTO, COR_COMPRA, COR_PAGTO, CLI_VIS_FRE,CLI_VIS_DOM, CLI_VIS_SEG, CLI_VIS_TER, CLI_VIS_QUA, CLI_VIS_QUI, CLI_VIS_SEX, CLI_VIS_SAB, CLI_VIS_ORD, CLI_DIA_REC,SET_COD, DESCTO_MAX, FICHA_CADASTRAL, CONTA_COD, TROCA_FLAG, TIPO_ENTREGA, DESCTO_TIPO, DESCTO_PERC, ACERTO_CONSIGNA,CON_COD, DAT_CAD, DAT_ALT, USUARIO, CLI_EMAILFIN, CLI_CONTR, INTEGRACAO, TAB_MIX, CLI_EMAILNFE, TES_COD, APLICAR_REGRA,NAT_COD, REGRA_COD, SALDOFDL, FDL_COD, CLI_TXCOB, ENTIDADE_COD, CLI_CST_CONTR, INTEGRA_WEB, HORA_ALT, ULT_COM_NFSNUM,ULT_COM_DAT_ANT, ULT_COM_VAL_ANT, CLI_ID_ESTRANGEIRO, FOR_COD, CLI_EMP_FAT, CLI_ISENTO_PISCOFINS)\
                            VALUES (?,?,'0',?,NULL,NULL,?, 'ISENTO',NULL, NULL, NULL,NULL,NULL,NULL,NULL, 'http://', NULL, NULL,'1','1','2','2','2','0','A','0','0',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0.00','1000.00','01.07.2040 00:00','0','0.00','0.00','0.00','0.00',NULL,NULL,'0.00',NULL,NULL,'0.00',NULL, '0.00', NULL,'0','0.00','0.00',NULL,'0.00','0','0.00','0.00',NULL,'0.00','0',NULL,'0.00','0',NULL,'0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','0.00','DIN','030',NULL,'0','0','1',?,'0.00','0.00','0','0',' ','001',NULL,NULL,NULL,NULL,NULL,?,NULL,'1','1','0','0','0',NULL,'0','0','0','0','0','0','0',NULL,'0', NULL,'0.00',NULL,NULL,'0','0','0','0.00',NULL,NULL,'10/20/2020','10/20/2020','Daniel',NULL,'0',NULL,NULL,NULL, '500','0',NULL,'0','0.00','0','0.00','0','2','1','00:00:00','0', NULL,'0.00',NULL,'0','0',NULL)", list(('1',Cli_cod,nome,cpf1,999,obs)))
                 cur.execute("INSERT INTO CLICLIENTESEND (EMP_COD, CLI_COD, TIT_COD, CLI_LOGRA, CLI_NUM, CLI_COMPL, BAI_COD, CLI_BAI, CID_COD, CLI_CID, CLI_EST, CLI_CEP, CLI_CONTATO, CLI_FONE1, CLI_FONE2, CLI_FONE3, CLI_FONE4, CLI_FONE5, CLI_FONE6, TEL_TIT1, TEL_TIT2, TEL_TIT3, TEL_TIT4, TEL_TIT5, TEL_TIT6, ROTA_COD, ROTA_SEQ, CLI_EAN, CLI_REF, ID_LOCAL, DAT_CAD, DAT_ALT, USUARIO, CLI_PAIS, CLI_LAT, CLI_LNG, CHAVE_TIPO)\
                            VALUES ('1',? , 1, ?,'SN', ?, 43992, ?, 6971, ?, 'RJ', ?, NULL, ?, NULL, NULL, NULL, NULL, NULL, '3', '2', '3', '5', '5', '0', '001', NULL, NULL, ?, NULL, '01.07.2040', '01.07.2040', 'DANIEL', '1058', NULL, NULL, '165')",list((Cli_cod,endereco,comp,bairro,cidade,cep,tel,obs)))
                
                 con.commit()
                 
                 #imprime o codigo de cliente cadastrado e limpa os campos
                 messagebox.showinfo("Cadastrado!",title + str(Cli_cod))
                 self.nome.delete(0, 'end') 
                 self.cpf.delete(0, 'end') 
                 self.end.delete(0, 'end') 
                 self.obs.delete(0, 'end') 
                 self.comp.delete(0, 'end')  
                 self.cep.delete(0, 'end') 
                 self.bairro.delete(0, 'end')            
                 self.cidade.delete(0, 'end') 
                 self.telefone.delete(0, 'end') 
                 
                 #caso seja falso, desfaz 
            if t == False:
             con.rollback()
             
             
            #função para validar cpf 
    def validate_cpf(self, cpfo, cpf, nome, end, obs, comp, cep, bairro, cidade, telefone ):
                 #atualiza informações do DBA  
                con = fdb.connect(dsn= #aqui colocar informarções do dba
                )
                #atualiza o proximo codigo do cliente caso tenha sido alterado por outra empresa/usuario
                cur = con.cursor()
                cur.execute("SELECT CLI_CGCCPF FROM CLICLIENTES ORDER BY CLI_COD DESC")
                cli_cpf = cur.fetchall()
                cpf_cli = list((cli_cpf))
                strings = [str(integer) for integer in cpf_cli]
                a_string = "".join(strings)
                cod_cliente = a_string
                
                 # verifica se o cpf é válido
                calc = [i for i in range(1, 10)]
                d1= (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
                d2= (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10
                if str(d1) == cpf[-2] and str(d2) == cpf[-1]:
                 if cpfo in cod_cliente:
                  cpfo1 = (cpfo,)
                  cur.execute("SELECT CLI_COD FROM CLICLIENTES WHERE CLI_CGCCPF = ?", (cpfo1))
                  cod = cur.fetchone()
                  cod = str(list(cod)).strip('[]')
                  title = "Erro!"
                  title1 = "  CPF já cadastrado  \n Código do Cliente: "
                  messagebox.showerror(title, title1 + str(cod))
                  return False
                 else:
                     return True
                else:
                     messagebox.showerror("ERRO!", "CPF Invalido!")
                     return False
                
                #percorre a variavel para verificar se está vazia
                lista = (nome, end, obs, comp, cep, bairro, cidade, telefone)
                for variavel in lista:
                    if variavel.get() == "":
                        messagebox.showerror("ERRO!", "Espaço do cadastro vazio!")
                        return False 
    
               
    
                #verifica se tem somente numero 
                if int(cpf) in [s * 11 for s in [str(n) for n in range(11 - 1)]]:
                 messagebox.showerror("ERRO!", "CPF Invalido!!")
                 return False
                 
		#verifica se falta algum dado
    def empty_space(self,nome, end, obs, comp, cep, bairro, cidade, telefone):
         global t
        
         lista = (nome, end, obs, comp, cep, bairro, cidade, telefone)
         for variavel in lista:
          if variavel.get() == '':
           messagebox.showerror("ERRO!", "Espaço do cadastro vazio!")
           t = False
          
   
           
#executa o codigo acima
root = Tk()
Application(root)
root.mainloop()
