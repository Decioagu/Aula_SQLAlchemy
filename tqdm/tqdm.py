from tqdm import tqdm
import time

'''
A biblioteca "tqdm" em Python é usada para criar barras de progresso em loops, 
facilitando o acompanhamento visual do andamento de processos demorados.
'''
for i in tqdm(range(100)):
    time.sleep(0.1)  # Simula um processo demorado