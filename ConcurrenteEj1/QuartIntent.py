#       loop forever
# p1:       non-critical section       
# p2:       wantp <-- true
# p3:       while wantq
# p4:               wantp <-- false
# p5:               wantp <-- true
# p6:       critical section
# p7:       wantp <-- false

#       loop forever
# q1:       non-critical section       
# q2:       wantq <-- true
# q3:       while wantp
# q4:               wantq <-- false
# q5:               wantq <-- true
# q6:       critical section
# q7:       wantq <-- false

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
        while wantq != False: 
            wantp = False
            wantp = True
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
        while wantp != False:
            wantq = False
            wantq = True
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