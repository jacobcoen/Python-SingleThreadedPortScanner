import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '192.168.1.160'

def pscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server,port))
        s.close()
        return True
    except:
        return False

for x in range(440,451):
    if pscan(x):
        print('Port',x, 'is Open')
    else:
        print('Port',x, 'is Closed')