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
        if len(user_input>3) and user_input.isalpha():
             return user_input
        else:
             print("Entrada inválida. Certifique-se de digitar apenas letras e que tenha pelo menos três letras: ")
      

def validar_idade():

    while True:

       try:
            idade= input("Digite o a sua idade:")

            if 0<= idade<= 150:
                  
                return idade

            else:
                print("Erro, a idade deve ser de 1 a 150:")

       except ValueError:
             print("Digite um número válido:")
                       
       
def validar_genero():
      
      while True:

        try:
             sexo= input("Digite o seu genero:(f)(m)")  

             if len(0>sexo>=1) and sexo.isalpha("f","m"):
                  return sexo
             else:
                  
                    print ("Entrada inválida. Digite f ou m")

        except:
             print("Digite f ou m")
                         


                 
                  


        




