#Método principal
#crea 2 hilos, cada hilo ejecuta un loop

#       loop forever
# p1:       non-critical section
# p2:       await turn = 1
# p3:       critical section
# p4:       turn <-- 2

#       loop forever
# q1:       non-critical section
# q2:       await turn = 2
# q3:       critical section
# q4:       turn <-- 1

# VA MUY LENTO

import threading
import time

MAX = 1000
THREADS = 2

turn = 1
contador = 0

def pthread():
    global turn
    global contador
    for j in range(0, MAX // THREADS):
        # -> sección no crítica, si se interrumpiese se quedaría bloqueado e incumpliría la norma 3 de Dijkstra
        while turn != 1: pass
        # -----SECCIÓN CRÍTICA-----
        contador = contador + 1
        # -------------------------
        turn = 2

def qthread():
    global turn
    global contador
    for j in range(0, MAX // THREADS):
        # -> sección no crítica, si se interrumpiese se quedaría bloqueado e incumpliría la norma 3 de Dijkstra
        while turn != 2: pass
        # -----SECCIÓN CRÍTICA-----
        contador = contador + 1
        # -------------------------
        turn = 1         



def main():
    inicio = time.time()
    hilop = threading.Thread(target = pthread)
    hiloq = threading.Thread(target = qthread)

    hilop.start()
    hiloq.start()

    hilop.join()
    hiloq.join()
    
    fin = time.time()
    tiempo = fin - inicio
    print("El contador vale:", contador)
    print("Porcentaje de acierto:", (contador//MAX)*100, "%.")
    print("Tiempo de ejecución:", round(tiempo, 3), "segundos.")
    

if __name__ == "__main__":
    main()
