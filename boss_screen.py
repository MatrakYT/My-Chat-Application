import socket
import socket
from tkinter import *
import threading

class ekran(Tk):
    def __init__(self):
        super().__init__()
        self.disconnect_msg = "!DISCONNECT" 
        self.machine_status = "client"
        self.machine_token = "?ZZ+WUxEx/QaEHq4CAitGIAjBujCtm2AY=8V0(Mq=&9I3vCg+Fr_v4EFPwftADIX79KmYS9%Ym6tq+sp7N(Z9g5^lqwl6-g/lbkeg7kTi5X@xJ9e2dX9Ovsooh5Z1?LltEwmot&&l5bWU^ogPBKbB4X7zMx4x%96UDDuMb7-wciIlQ!sQa=Gm8)KiGx+rlsSW4?KIlB6client"
        self.machine_token_boss= "6^j8Pd1/KXFTWBvR/b!Y0vxECvcB?mHC$NoqTeZ/hm0E5AQf_At5^i=zYG=_$=tDS^CF?0bdKcOsPY6O5aA2GtrhyIACK&6OtA%GyxbzX9Nf!g-+hK=L$7fbSPWYgrUoKFwcOCz-fU=3NlzRKK-O_y6ZtQgC^da@4$KGS?AdfhpFA6ratXv4Zl?oXYGP1acU/3MKgzdD"
        self.machine_user = socket.gethostname()
        self.machine_ip= socket.gethostbyname(self.machine_user)
        self.server_port=5050
        self.boyut=1024
        self.Format="utf-8"
        self.server_ip="MAKİNE İPSİNİ YAZ"
        self.server_conntect_details = (self.server_ip, self.server_port)
        self.client_Socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_Socket.connect(self.server_conntect_details)
        self.client_Socket.send((self.machine_token_boss).encode(self.Format))
        self.title(f"Bağlandığın yer {self.server_ip}")
        self.witdh=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.witdh,self.height))
        self.yScroll = Scrollbar(self, orient=VERTICAL)
        self.lb=Listbox(self,height=25, width=168,background="blue")
        self.lb.pack()
        self.lb.place(x=0,y=0)
        self.lbu=Listbox(self,height=25, width=55,background="yellow", yscrollcommand=self.yScroll.set)
        self.lbu.pack()
        self.lbu.place(x=1015,y=0)
        self.message_entry = Entry(self,width=25, background="blue",font=('Halvetica',12,'bold'))
        self.message_entry.pack()
        self.message_entry.grid(row=1, column=0, padx=20, pady=30)
        self.message_entry.place(x=0,y=680)
        self.send_button = Button(self,text="Send",width=20,command=lambda:self.senderll())
        self.send_button.pack()
        self.send_button.place(x=250,y=676)
        self.t1= threading.Thread(target=self.recv_funck)
        self.t1.daemon = True
        self.t1.start()

    def senderll(self):
        msg = self.message_entry.get()
        if msg == self.disconnect_msg:
            self.client_Socket.send(msg.encode(self.Format))
            quit()
        else:
            self.client_Socket.send(msg.encode(self.Format))

    def recv_funck(self):
        while True:
            msg = self.client_Socket.recv(self.boyut).decode(self.Format)
            if "ux0yl" in msg:
                al=[]
                msg = msg.replace("ux0yl","")
                msg = msg.replace("{","")
                msg = msg.replace("}","")
                if "," in msg:
                    splitsss = msg.split(",")
                    for i in splitsss:
                        al.append(i)
                else:
                    al.append(msg)
                self.lbu.delete(0, END)
                for i in al:
                    self.lbu.insert(END, str(i))
                al.clear()
            else:
                self.lb.insert(END, msg)

e=ekran()
e.mainloop()