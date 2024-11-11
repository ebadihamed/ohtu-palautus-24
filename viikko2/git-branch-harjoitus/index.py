# Tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("Aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"Lukuejen {x} + {y} summa on {summa(x, y)}")
print(f"Lukujen {x} - {y} erotus on {erotus(x, y)}")
print(f"Lukujen {x} * {y} tulo on {tulo(x, y)}")
logger("Lopetetaan")
print("goodbye!") # Lisäys bugikorjaus-branchissa
