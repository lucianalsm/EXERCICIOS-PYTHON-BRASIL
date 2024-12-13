# faça um programa que peça as 4 notas bimestrais e faça a média

Nota_bimetre_1= float(input(f'Digite a nota do primeiro bimestre:'))
Nota_bimetre_2= float(input(f'Digite a nota do segundo bimestre:'))
Nota_bimetre_3= float(input(f'Digite a nota do terceiro bimestre:'))
Nota_bimetre_4= float(input(f'Digite a nota do quarto bimestre:'))

Media_notas= (Nota_bimetre_1 + Nota_bimetre_2 + Nota_bimetre_3 + Nota_bimetre_4)/4

if Media_notas >= 5.0:

    print(f'Sua média anual foi:{Media_notas}. Parabéns, Você passou')      

else:
    print(f'Sua média foi {Media_notas}). Você está de recuperação')                         