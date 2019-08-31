# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 02:50:49 2019

@author: Brainiac
"""
global x
global h1
h1 = [' '] * 10
global pos
pos = str 
acabou = False
game_on = True
i = 0

# Começa Aqui

jd1 = input("Qual o nome do Jogador 1: ").upper()
x = input("Quer ser X ou O: ").upper()
jd2 = input("Qual o nome do Jogador 2: ").upper()
if x == "X" : o = "O"
else : o = "X"


     
print("")
print("Olá, {}".format(jd1))

print("Olá, {}".format(jd2)) 
print("")
print("Sejam Bem-Vindos ao jogo da velha")
print("{} Jogará com {}".format(jd1,x))
print("{} Jogará com {}".format(jd2,o))
print("------------------------------------")

print("   0    1    2")
print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))

def check_win(h1, x):        
 return (( h1[0] == x and h1[3] == x and h1[6] == x )or
 (h1[1] == x and h1[4] == x and h1[7] == x)or
 (h1[2] == x and h1[5] == x and h1[8] == x)or
 (h1[0] == x and h1[1] == x and h1[2] == x)or  
 (h1[3] == x and h1[4] == x and h1[5] == x)or  
 (h1[6] == x and h1[7] == x and h1[8] == x)or  
 (h1[0] == x and h1[4] == x and h1[8] == x)or  
 (h1[6] == x and h1[4] == x and h1[2] == x))

def game_board(h1,pos):   #função atribui X ou O pela posição que é definida
 pos = input("Informe uma posição: ").upper()
 if pos == "A0":
      h1[0] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
      
 elif pos == "A1":
      h1[1] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
      
 elif pos == "A2":
      h1[2] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
      
 elif pos == "B0":
      h1[3] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
      
 elif pos == "B1":
      h1[4] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
 elif pos == "B2":
      h1[5] = input("Entre com X ou O: ").upper()  
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
 elif pos == "C0":
      h1[6] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
 elif pos == "C1":
      h1[7] = input("Entre com X ou O: ").upper()
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
 elif pos == "C2":
      h1[8] = input("Entre com X ou O: ").upper()  
      print("   0    1    2")
      print(" A[{}]  [{}]  [{}] ".format(h1[0], h1[1], h1[2]))
      print(" B[{}]  [{}]  [{}] ".format(h1[3], h1[4], h1[5]))
      print(" C[{}]  [{}]  [{}] ".format(h1[6], h1[7], h1[8]))
 return

def empate(h1):    #função checa se está empatado e se o espaço ainda está vazio
    cont = 0
    for i in range(0,10):
     if h1[i] == "X" or h1[i] == "O":
        cont = cont+1
        if cont == 9:
            return True
     else :
         h1[i] == " "
         return False

    
while game_on:                       #main code    
  game_board(h1, x)
  acabou = empate(h1)
  if acabou == True:
      print("Tivemos um empate!!") 
      game_on = False
  else:
       if check_win(h1,x):
         print("Meus parabens,{}".format(jd1))
         print("Voce Ganhou !!!")
         game_on = False
       elif check_win(h1,o):
         print("Meus parabens,{}".format(jd2))
         print("Voce Ganhou !!!")
         game_on = False
    
 


    
    