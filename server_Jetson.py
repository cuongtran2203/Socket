import socket
import serial
import argparse
import cv2
import os
import time
def args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--host",default="localhost",type=str,help="điền địa chỉ IP")
    parser.add_argument("--ip",default=9999,type=int,help="Chọn cổng port")
    parser.add_argument("--com",default="/dev/ttyUSB1",help="Chọn cổng COM kết nối arduino")
    parser.add_argument("--ip_cam",default=None,type=str,help="Nhập địa chỉ ip cam")
    parser.add_argument("--baudrate",default=9600,type=int,help="lựa chọn tần số kết nối")
    args=parser.parse_args()
    return args
ROOT=os.makedirs("datasets",exist_ok=True)

if __name__=="__main__":
    arg=args()
    HOST = arg.host  # Standard loopback interface address (localhost)
    PORT = arg.ip  # Port to listen on (non-privileged ports are > 1023)
    COM=arg.com
    ser = serial.Serial(
    port=COM,
    baudrate=arg.baudrate,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
    # Kêt nối vs camera ip
    cam=cv2.VideoCapture(arg.ip_cam)
    try: 
        ser.open()
    except Exception as e:
        print ("error open serial port: " + str(e))
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        count=0
        while cam.isOpened():
            ret,frame=cam.read()
            data = conn.recv(1024).decode("utf-8")
            ser.write(data)
            if len(data)>2:
                count+=1
                if not os.path.exists(os.path.join(ROOT,data)):
                    os.makedirs(os.path.join(ROOT,data),exist_ok=True)
                if count%5==0:
                    cv2.imwrite(os.path.join(ROOT,data,data+"_"+str(time.time())+"_.jpg"),frame)
                    print("saved image")
                
                

