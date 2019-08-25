# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 05:00:05 2019

@author: Daniel Rocha
"""
check_codigo = [1,2,3,4]
produtos = ["ARROZ","FEIJAO","MACARRAO","CARNE"]
codigo = ["1","2","3","4"]
x = 0
preco_comp = [2,2,3,4]
quantidade = [2,3,5,4]
preco_vend = [5,5,6,8]
categoria = [1,1,2,3]


def menu():  #função menu
    print("MENU: ")
    print("   1- Cadastrar Produto")
    print("   2- Listar Produto")
    print("   3- Excluir Produto")
    print("   4- Ticket Médio da Empresa")
    print("   5- Sair")
    opt = int(input("Digite a opção desejada: "))
    return opt

def cadastro_produto():  #função para cadastrar produtos.
     ret = 0
     bot = True
     produto = input("Digite o nome do produto: ").upper()
     if produto in produtos:
         print("Produto já cadastrado:")
         produto = input("Digite o nome do produto: ").upper()
         produto = produto.upper
     else:
          produtos.append(produto)
    
     while bot == True:
      num = int(input("Digite o codigo do produto: "))
      if num in check_codigo:
         print("Produto com codigo já cadastrado.")
         
      else:
         check_codigo.append(num)
         bot = False
         break   
     preco_comp.append(int(input("Digite o valor de compra do produto: ")))
     preco_vend.append(int(input("Digite o valor de venda do produto: ")))
     categoria.append(int(input("Digite o numero da categoria do produto: ")))
     quantidade.append(int(input("Digite a quantidade desse produto: ")))
     
     ret = int(input("1- Retorne ao Menu . 2- Continue a cadastrar: "))
     return ret

 
def lista_produto():  # função para listar os produtos
    x = 0
    ret = 0
    print("[     Nome    ][        Codigo       ][           Preço de venda       ][        Categoria       ][    Quantidade   ]")
    for x in range(0,len(produtos)):
     print("{:>10}""{:>18}""{:>32}""{:>27}""{:>20}".format(produtos[x], check_codigo[x], preco_vend[x], categoria[x], quantidade[x]))
     x = x + 1
    x = 0 
    ret = int(input("1- Retorne ao Menu . 3- Deseja excluir: "))
    return ret

def excluir_produto():  #funcao para excluir produtos
    x = 0
    ex_produto = input("Digite o nome do produto: ").upper()
    for x in range(0, len(produtos)):
     if ex_produto in produtos:
      print(produtos)   
      x = produtos.index(ex_produto)   
      produtos.pop(x)
      check_codigo.pop(x)
      preco_comp.pop(x)
      preco_vend.pop(x)
      categoria.pop(x)
      print("--Produto Retirado--")
      print(produtos)
            
     else:
      ret = 0
      ret = int(input("1- Retorne ao Menu . 3- Continue a excluir: "))
      return ret
          
def ticket_medio():  #funçao para ter o Ticket Média do total de vendas
    ticket = 0
    
    for x in range(0,len(produtos)):
     ticket = ticket + preco_comp[x] * quantidade[x]
    print("O ticket médio da empresa é: %s" %ticket)
    ret = 0
    ret = int(input("1- Retorne ao Menu "))
    return ret
    
    
boo = True
while boo == True:
 opcao = menu()
 if opcao == 1:
  cadastro_produto()
  opcao = 0
 elif opcao == 2:
  lista_produto()
  opcao = 0
 elif opcao == 3:
  excluir_produto()
  opcao = 0
 elif opcao == 4:
  ticket_medio()
  opcao = 0  
 elif opcao == 5 :
  boo = False

while boo == True:
 opcao = excluir_produto()
 if opcao == 1:
    menu()
    opcao = 0
 elif opcao == 0:
    excluir_produto() 
    opcao = 0

while boo == True:
  opcao = cadastro_produto()
  if opcao == 1:
     menu()
     opcao = 0
  elif opcao == 2:
    cadastro_produto()
    opcao = 0

while boo == True: 
  opcao = lista_produto()
  if opcao == 1:
    menu()
    opcao = 0
  elif opcao == 3:
    excluir_produto()       
    opcao = 0
    