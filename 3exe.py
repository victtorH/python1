from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


for cont in range(-10,0,-1):
    print(cont)
print('fim da repetição')
for nome in 'victtor':
    print(nome)
print('fim da repetição')
for opeA in range(1,11):
    print('taboada do:',opeA)
    for opeB in range(11):
        result=opeA*opeB
        print('{0}x{1}={2}'.format(opeA,opeB,result))
    print('fim da tabuada do {0}.\n\n'.format(opeA))
print('fim da repetição')