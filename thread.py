# importação de biblioteca
import threading #para criação e controle de threads
import time #para simular tempo de processamento com sleep()
import math
#estrutura da thread
def estruturathread(nome, inicio, fim):
    for i in range(inicio, fim +1): # loop de 50 até 60
        print(f"{nome} -> {i}") # imprime o numero atual
        time.sleep(1000) # aguarda 0.5 segundos para simular processamento
# ponto de entrada do progama
thread1 = threading.Thread(target=estruturathread, args=("thread1", 1, 10)) # criação dos objetos thread, associando cada uma a sua respectiva função
thread2 = threading.Thread(target=estruturathread, args=("thread2", 50, 60))
# o método join() faz com que o programa principal aguarde a finalização das threads
thread1.start()# após ambas finalizarem esta mensagem será exibida print("todas as threads terminaram.programa finalizado.")
thread2.start()