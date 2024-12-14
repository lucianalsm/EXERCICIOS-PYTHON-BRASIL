#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra_digitada= (input("Digite uma letra:"))
vogais=[ 'a', 'e', 'i', 'o', 'u']
consoantes="bcdfghjklmnpqrstvwyz"



if letra_digitada in vogais:
    print("A letra digitada é uma vogal")   
elif letra_digitada  in consoantes:
    print("A letra digitada é uma consoante") 
else:
    print(f'Erro. {letra_digitada}')   

