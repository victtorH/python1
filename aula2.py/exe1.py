#incluir e duplicar na lista
lista= [123, True, 'python',[123]]
print(lista[2])
lista.insert(0,'inserido')
lista.append('ultimo')
print(lista)
lista2=[2023,'carnaval']
lista2.extend(lista2)
print(lista2)
print(lista[2])