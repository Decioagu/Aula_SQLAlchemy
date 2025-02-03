from tqdm import tqdm
import time

'''
A biblioteca "tqdm" em Python é usada para criar barras de progresso em loops, 
facilitando o acompanhamento visual do andamento de processos demorados.
'''
for i in tqdm(range(100)):
    time.sleep(0.1)  # Simula um processo demorado

my_list = [1, 2, 3, 4, 5]
for item in tqdm(my_list):
    time.sleep(1)  # Simula uma tarefa com cada item

for i in tqdm(range(5), desc="Processando", unit="iteração", colour="green"):
    time.sleep(0.3)

from tqdm.asyncio import tqdm
import asyncio

async def tarefa(n):
    await asyncio.sleep(n)

async def main():
    tasks = [tarefa(0.5) for _ in range(10)]
    for _ in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
        await _

asyncio.run(main())