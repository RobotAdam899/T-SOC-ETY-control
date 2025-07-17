import socket

ip = input("📲 Hedef IP: ")
port = int(input("🔌 Port: "))

s = socket.socket()
s.connect((ip, port))

while True:
    cmd = input("💣 Komut gönder >> ").strip()
    if cmd == "":
        continue
    s.send(cmd.encode())
    if cmd == "kapat":
        break

s.close()
