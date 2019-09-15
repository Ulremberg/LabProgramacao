# coding: utf-8
a = raw_input("Digite M se seu sexo for masculino ou F se for feminino").upper()

if(a == 'F'):
    print('F - Feminino')
elif(a == 'M'):
    print('M - Masculino')
else:
    print('Sexo inválido')