#Faça um Programa que peça dois números e imprima o maior deles.

numero_1= int(input("Digite um número"))
numero_2= int(input("Digite outro número"))

if numero_1> numero_2:
    print(f'{numero_1} é maior que {numero_2}')

elif numero_1< numero_2:
     print(f'{numero_1} é menor que {numero_2}')

else:
     print("Os números são iguais")
              
