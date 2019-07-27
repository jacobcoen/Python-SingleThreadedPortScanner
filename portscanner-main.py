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


print("--Welcome to Jacob's port scanner!--")
print('Please enter the first port in the range you would like to scan')
firstPort = input()
print('Please enter the last port in the range you would like to scan')
lastPort = input()

for x in range(int(firstPort),int(lastPort)):
    if pscan(x):
        print('Port',x, 'is Open')
    else:
        print('Port',x, 'is Closed')