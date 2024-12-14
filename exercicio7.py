#Faça um Programa que peça um valor e mostre na tela se o valor é 
# positivo ou negativo.

digite_numero= int(input(f'Digite um número:'))

if digite_numero >0:
    print("Você digitou um número positivo")
elif digite_numero<0:
    print("Você digitou um numero negativo")
else:
    print("Você digitou o número 0")    
