def maximo(lista):
    if len(lista)==1:        
        return lista[0]      
    primeiro = lista[0]      
    lista_menor = lista[1:]  
    max_resto = maximo(lista_menor)
    if primeiro > max_resto :
        return primeiro     
    else:
        return max_resto    

def maximo1(lista):
    if len(lista)==1:        
        return lista[0]      

def maximo2(lista):
    if len(lista)==1:        
        return lista[0]      
    primeiro = lista[0]      
    lista_menor = lista[1:]  
    max_resto = maximo1(lista_menor)
    if primeiro > max_resto :
        return primeiro     
    else:
        return max_resto    

def maximo3(lista):
    if len(lista)==1:        
        return lista[0]      
    primeiro = lista[0]      
    lista_menor = lista[1:]  
    max_resto = maximo2(lista_menor)
    if primeiro > max_resto :
        return primeiro     
    else:
        return max_resto    

print(maximo3([10,20,40]))
print(maximo3([10,40,20]))
print(maximo3([40,20,10]))

print(maximo([10,20,30,22,35,70,9]))
 
