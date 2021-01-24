import socket
import threading
import tkinter
from termcolor import *
import sys

header = 1024
port = 5050
server = socket.gethostbyname(socket.gethostname())
print(server)
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bilgiler = (server, port)
Server.bind(bilgiler)
Format = "utf-8"
disconnect_msg = "!DISCONNECT"
Warning_msg = "Warning"
Security_msg = "Security"
client_token = "?ZZ+WUxEx/QaEHq4CAitGIAjBujCtm2AY=8V0(Mq=&9I3vCg+Fr_v4EFPwftADIX79KmYS9%Ym6tq+sp7N(Z9g5^lqwl6-g/lbkeg7kTi5X@xJ9e2dX9Ovsooh5Z1?LltEwmot&&l5bWU^ogPBKbB4X7zMx4x%96UDDuMb7-wciIlQ!sQa=Gm8)KiGx+rlsSW4?KIlB6"
boss_token = "6^j8Pd1/KXFTWBvR/b!Y0vxECvcB?mHC$NoqTeZ/hm0E5AQf_At5^i=zYG=_$=tDS^CF?0bdKcOsPY6O5aA2GtrhyIACK&6OtA%GyxbzX9Nf!g-+hK=L$7fbSPWYgrUoKFwcOCz-fU=3NlzRKK-O_y6ZtQgC^da@4$KGS?AdfhpFA6ratXv4Zl?oXYGP1acU/3MKgzdD"
user_list = set()
client=set()
boss=set()
user_list_addr=set()
boos_msg="boss"
client_msg="client"

def ayristirici(msg, conn, addr):
    if msg == boss_token: 
        boss.add(addr)
        print(colored(f"[{addr}] => Machine Status ","blue"),colored("Boss","red"))
        return True
    elif msg == client_token:
        client.add(addr)
        print(f"[{addr}] => Machine Status Client")
        return True
    else:
        banned=open("banned.txt", "a")
        banned.write(str(addr)+"\n")
        for i in user_list:
            i.send((f"{addr} => izinsiz giriş").encode(Format))
        print(colored(f"{addr} mal aq bu lan", "red"))
        user_list.remove(conn)
        user_list_addr.remove("ux0yl"+str(addr[0])+"-"+str(addr[1]))
        return False

def islemler(conn, addr, msg):
    if msg:
        #işlemler
        if msg == disconnect_msg:
            print(colored(f"[{addr}] Bağlantısını kendi isteğiyle kesti!","red"))
            user_list.remove(conn)
            user_list_addr.remove("ux0yl"+str(addr[0])+"-"+str(addr[1]))
            return False
        else:
            print(colored(f"[{addr}] {msg}", "yellow"))
            for i in user_list:
                i.send((f"{addr} => {msg}").encode(Format))
            return True
    else:
        return True

def user_send():
    for i in user_list:
        i.send((f"{user_list_addr}").encode(Format))
        print(f"{user_list_addr}")

def clients(conn, addr):
    print(colored(f"[Yeni Bağlantı] {addr} bağlandı", "green"))
    baglanti = True
    a = True
    user_send()
    try:
        while baglanti:
            msg = conn.recv(header).decode(Format)
            if a == True:
                baglanti=ayristirici(msg, conn,addr)
                a = False
            else:
                baglanti=islemler(conn,addr,msg)
    except Exception as e:
        user_list.remove(conn)
        user_list_addr.remove("ux0yl"+str(addr[0])+"-"+str(addr[1]))
        print(e)
    conn.close()


def basla():
    print(colored("[Başladı] Sistem başladı!", "green"))
    Server.listen()
    a=0
    while True:
        conn, addr = Server.accept()
        coklu = threading.Thread(target=clients, args=(conn, addr))
        coklu.start()
        user_list.add(conn)
        user_list_addr.add("ux0yl"+str(addr[0])+"-"+str(addr[1]))
        print(colored(f"[Yeni Aktif Bağlantı] {threading.activeCount() - 1}",color="green"))
baslıyor = colored("[Başlıyor] ",color="green")
a=colored("Server sistemi başlıyor...", color="green")
print(baslıyor+a)
basla()