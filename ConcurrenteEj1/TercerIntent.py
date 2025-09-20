#Método principal
#crea 2 hilos, cada hilo ejecuta un loop

#       loop forever
# p1:       non-critical section       
# p2:       wantp <-- true
# p3:       await wantq = false
# p4:       critical section
# p5:       wantp <-- false

#       loop forever
# q1:       non-critical section       
# q2:       wantq <-- true
# q3:       await wantp = false
# q4:       critical section
# q5:       wantq <-- false

# EL GIL HACE QUE NO FALLE
import threading
import time

MAX = 100000000
THREADS = 2
wantp = False
wantq = False
contador = 0

def pthread():
    global contador
    global wantq
    global wantp
    for j in range(0, MAX // THREADS):
        # -> sección no crítica
        wantp = True
        while wantq != False: pass
        # -----SECCIÓN CRÍTICA-----
        contador = contador + 1
        # -------------------------
        wantp = False

def qthread():
    global contador
    global wantq
    global wantp
    for j in range(0, MAX // THREADS):
        # -> sección no crítica
        wantq = True
        while wantp != False: pass
        # -----SECCIÓN CRÍTICA-----
        contador = contador + 1
        # -------------------------
        wantq = False    



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
    print("El contador vale: ", contador)
    print("Porcentaje de acierto:", (contador//MAX)*100, "%.")
    print("Tiempo de ejecución:", round(tiempo, 3), "segundos.")

if __name__ == "__main__":
    main()