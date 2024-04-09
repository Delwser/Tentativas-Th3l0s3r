import socket
host = str(input("Coloque o site que deseja fazer o scan!\n"))
porta = 20, 21 , 22 , 25 , 53 , 80 , 443    
def verifica_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  

    try:
        sock.connect((host, porta))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()



if verifica_porta(host, porta):
   print(f'A porta {porta} em {host} está aberta.')

else:
    print(f"A porta {porta} em {host} está aberta.")