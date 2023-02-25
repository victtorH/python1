#1
lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lista)
print('o ultimo numero da lista é:{}'.format(lista[-1]) )
#2
print(lista)
print('O primeiro item da lista é:{}'.format(lista[-16]))
#3
print(lista)
print('entre as possiçãoes {} e {} tem as posiçãoes: {}'.format(3,10,lista[3:11]))
#4
print(lista)
print('a soma dos itens é:',sum(lista))
#5
for item in lista: 
    print(item)
#6
num1=input('digite o 1 numero:')
num2=input('digite o 2 numero:')
num3=input('digite o 3 numero:')
num4=input('digite o 4 numero:')
num5=input('digite o 5 numero:')
listanova=[num1,num2,num3,num4,num5]
for item2 in listanova:
    print(item2,listanova.index(item2))
#7



