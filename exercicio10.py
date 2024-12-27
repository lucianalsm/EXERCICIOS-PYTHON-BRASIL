#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


while True:

    solicitar_login= input("Digite seu nome de usuário:")
    solicitar_senha= input("Digitar senha: ")
            
            
    if solicitar_login == solicitar_senha:

        print("ERRO. A SENHA NAO PODE SER IGUAL AO NOME DE USUÁRIO")

    else:

        print("CADASTRO REALIZADO COM SUCESSO")

                        


    