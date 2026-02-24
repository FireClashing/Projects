import socket

host = "154.57.164.70"  # host ip address
port = 31972  # host port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Tcp connection
s.connect((host, port))

s.settimeout(5)


def recv():
    data = b""
    while True:
        chunk = s.recv(1024)
        if not chunk:
            break
        data += chunk
        print(data.decode())  # Prints untill server sends data


recv()
