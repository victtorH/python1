from operator import itemgetter


#frente e verso com lista
lista= [123, True, 'python',[123]]
listainertida=[]
for item in lista:
    listainertida.insert(0,item)
print(listainertida)
print(lista)