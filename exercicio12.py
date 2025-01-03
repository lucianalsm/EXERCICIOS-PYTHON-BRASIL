#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


import re

def validar_nome():
      while True:   

        user_input = input("Digite um nome com pelo menos três letras: ").strip()
        if len(user_input)>=3 and user_input.isalpha():
             return user_input
        else:
             print("Entrada inválida. Certifique-se de digitar apenas letras e que tenha pelo menos três letras: ")

             
def validar_idade():

    while True:

       try:
            idade= input("Digite o a sua idade:")

            if 0<= int(idade)<= 150:
                  
                return idade

            else:
                print("Erro, a idade deve ser de 1 a 150:")

       except ValueError:
             print("Digite um número válido:")
                       
       
def validar_genero():
      
       while True:
        sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").strip().lower()
        if sexo in ['f', 'm']:
            break
        print("Erro: O sexo deve ser 'f' ou 'm'.")

def validar_estado_civil():

     while True:
         estado_civil= input("Digite seu estado civil [s]olteiro, [c]casado, [d]ivorciado, [v]iúvo: ").strip().lower()
         if estado_civil in ['s','c', 'd', 'v'] :
             break
         print("Erro: O estado deve ser s, c, d ou v")      



validar_nome()

validar_idade()

validar_genero()

validar_estado_civil()