
import random

def ordenamiento_mezcla(lista):
    if len(lista)>1:
        medio=len(lista) //2
        izquierda=lista[:medio]
        derecha=lista[medio:]

        #llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        #iteradores para recorrer las 2 sublistas
        i=0
        j=0
        #iterador para lista principal
        k=0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k]=izquierda[i]
                i += 1
            else:
                lista[k]=derecha[j]
                j += 1
            k += 1
        
        while i<len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j<len(derecha):
            lista[k] = derecha[j]
            j += 1  
            k += 1  

    return lista        








if __name__ == '__main__':
    tamano_lista=int(input("Tamaño de la lista? "))
    

    lista=[random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print("-" * 20)
    lista_ordenada=ordenamiento_mezcla(lista)
    print(lista_ordenada)