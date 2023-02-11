num1=input('digite o seu primeiro numero:')
num2=input('digite seu segundo numero:')
if(num1.isdecimal()):
    num1=float(num1)
else: 
    print('A situação digitada não é um numero')

if(num2.isdecimal()):
    num2=float(num2)
else:
    print('A situação digitada não é um numero')
nf=num1+num2
print('Foi formada um soma, o resultado dela é {}'.format(nf))