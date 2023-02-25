#Criar tupla
tupla= ('Victtor','hugo','estevam','12345','nome')
#transformar tupla em string
tuplastr= ' '.join(tupla)
print(tuplastr)
#fatiar tupla
print(tupla[:-2])
#acessar a tupla
print(tupla[0])
#loop em tupla
for item in tupla:
    print('item{}'.format(item))