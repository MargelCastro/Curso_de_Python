#METODO APPEND; Es utilizado para agregar elementos del mismo tipo a una lista 
#si le pasamos el metodo .append a la lista podemos agregar un elementos del mismo tipo
lista1 = [1, 2, 3]
print(lista1)   #Imprime la lista 1,2,3

lista_append = ["a", "b", "c"] #LAs letras van encerradas en comillas para que sean detectadas como string, sino dará error
lista_append.append("d")
print(lista_append)     #Imprime la lista habiendo agregado la letra d = a, b, c, d

#METODO COPY; copia una lista creada anteriormente
casa = [1, 2, 3]
casa_copia = casa.copy()#La lista casa_copia sera igual a una copia de la lista casa
casa_copia.append(4)#agregara el numero 4 a la lista casa_copia
print(casa, casa_copia)# imprime ambas listas

#METODO CLEAR; Elimina todos los elementos de una lista
lista = [10, 20, 30] #Crea la lista
lista.clear()#Borra los elementos de la lista
print(lista)#Imprime la lista vacia