# Tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("Aloitetaan ohjelma") # muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}")

logger("Lopetetaan")
print("goodbye!") # Lisäys bugikorjaus-branchissa
