import socket
# echo-client.py
import argparse
import pygame


def args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--host",default="localhost",help="điền địa chỉ IP")
    parser.add_argument("--port",default=9999,help="Chọn cổng port")
    args=parser.parse_args()
    return args



if __name__=="__main__":
    arg=args()
    HOST = arg.host  # The server's hostname or IP address
    PORT = arg.port  # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                s.sendall(b"LEFT")
            if keys[pygame.K_RIGHT]:
                s.sendall(b"LEFT")
            if keys[pygame.K_DOWN]:
                s.sendall(b"DOWN")
            if keys[pygame.K_UP]:
                s.sendall(b"UP")
