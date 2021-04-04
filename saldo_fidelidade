# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:32:28 2020

@author: warlord
"""


import fdb

con = fdb.connect(dsn= #colocar aqui info do DBA)
search = list

#puxa do DBA informação de saldo de fidelidade do banco
while True:
 search = input("Digite o codigo do cliente:")
 cur = con.cursor()

 cur.execute("SELECT cli_cod,CLI_RAZ,EMP_COD, SALDOFDL FROM CLICLIENTES WHERE CLI_COD = ?" , (search,))
 pesq = cur.fetchall()
 print("|COD CLIENTE|        NOME CLIENTE                                 | EMPRESA | SALDO")
 for i in pesq:
    print(i)
