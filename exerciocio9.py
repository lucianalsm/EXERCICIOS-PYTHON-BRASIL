## Estrutura de repetição
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.



while True:
    try:
            solicitar_nota= (input("Digite a sua nota:"))  
            
            nota_float= float(solicitar_nota)

            if 0<=nota_float <= 10.0: 

                print(f'Sua nota é {nota_float}')

                break
            else:
                 print("Valor inválido. A nota deve ser de 0 a 10")    
    except ValueError:

        print("Erro.")
        

        
















