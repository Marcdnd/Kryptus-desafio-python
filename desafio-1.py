#python
lista=[] # inicia variavel lista
lista.append(2) # put 2
lista.append(7) # put 7
lista.append(3) # put 3 
first = lista[0] # first = 2 { get first element }
last = lista[-1] # last = 3 {get last element }
lista.append(8) # put 8
tres = lista[2] # tres = 3 {get 3}
dois = lista[1] # dois = 7 {get 2}
print(lista) # (2, 7, 3, 8)
lista.pop(2) # remove 3o element
print(lista) # [2, 7, 8]

#test
print(first,last,dois,tres) #  2 3 7 3

lista = [] # clear
exit()

