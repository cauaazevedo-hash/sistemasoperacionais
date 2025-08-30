# importação de biblioteca
import threading
import time
import math
#estrutura da thread
def estruturathread(nome, inicio, fim):
    for i in range(inicio, fim +1):
        print(f"{nome} -> {i}")
        time.sleep(1000)

thread1 = threading.Thread(target=estruturathread, args=("thread1", 1, 10))
thread2 = threading.Thread(target=estruturathread, args=("thread2", 11, 20))

thread1.start()
thread2.start()