import random
import multiprocessing as mp
import time


def mergeSort(num,Sol,posicion_array): 
    #Se divide el array hasta llegar a tener 1 elemento   
    
    if len(num) >1: 
        m = len(num)//2 #Se divide el array en dos mitades
        L = num[:m]   
        R = num[m:] 
        
        #Se llama dos veces al metodo mediante hilos, cada uno con uno de los arrays creados
        cores = [] # Array para guardar los cores y su trabajo
        cores.append(mp.Process(target=mergeSort, args=(L,Sol,posicion_array)))# Añado al Array los cores y su trabajo
        cores.append(mp.Process(target=mergeSort, args=(R,Sol,posicion_array+len(L))))# Añado al Array los cores y su trabajo
        #mergeSort(L,Sol,posicion_array)
        #mergeSort(R,Sol,posicion_array+len(L))
        for core in cores:
            core.start()# Arranco y ejecuto el trabajo para c/ uno de los cores que tenga mi equipo, ver excel
        

        #i, j, k son variables auxiliares y tendran diversas funciones a lo largo del programa
        j = k = 0
        
        #Esperamos a que los hilos terminen
        for core in cores:
            core.join()# Bloqueo cualquier llamada hasta que terminen su trabajo todos los cores
        
        #Copiamos las soluciones en los arrays auxiliares L Y R
        i = posicion_array
        for dato in L:
            L[k] = Sol[i]
            i +=1
            k +=1
        i = posicion_array+len(L)
        k = 0
        for dato in R:
            R[k] = Sol[i]
            i+=1
            k+=1
        
        i = k = 0
        #Reescribimos el primer array ordenandolo
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                num[k] = L[i] 
                i+=1
            else: 
                num[k] = R[j] 
                j+=1
            k+=1
          
        #Devido a que en ciertos casos uno de los arrays es mas largo que el otro
        # se incluye a continuacion de lo ya sustituido
        while i < len(L): 
            num[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            num[k] = R[j] 
            j+=1
            k+=1
    i = posicion_array
    for dato in num:
        Sol[i] = dato
        i+=1
   
#Crea un array de numeros aleatorios
def rand(lenth):
    num = [random.randint(0,9)]
    for i in range(0,lenth-1):
        num.append(random.randint(0,9))
        
    return num

#Imprime lista
def imprimir(num): 
    for i in range(len(num)):         
        print(num[i],end ='  ') 
    print() 
  

    
if __name__ == '__main__': 
    n_cores = mp.cpu_count() # Obtengo los cores de mi pc
    print ("\n\nn_cores = ", n_cores)
    
    #exp = 21839250
    exp = 210
    num = rand(exp) 
    imprimir(num)
    print ("\nUsamos el exp ", exp)
    start = time.time()
    Sol = mp.RawArray('i', len(num)) # Array Sol de memoria compartida donde se almacenaran los resultados
    mergeSort(num,Sol, 0) 
    end = time.time()
    tiempo = end-start
    
    print("\nResultado =") 
    imprimir(num) 
    print("\n\nTiempo de ejecucion = ",tiempo)

