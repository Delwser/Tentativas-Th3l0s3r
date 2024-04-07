import subprocess

#retorna a o usuario, se o servidor está pingando com ele.
host = input("Qual é o ip?\n")

def ping (host):
    pingando = subprocess.run(['ping', '-c', '20'], capture_output=True , text = True)


    return pingando.stdout

resultado_ping = ping(host)
print(resultado_ping)