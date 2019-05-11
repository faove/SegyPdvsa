import socket

class impresion():
    
    socket_s = socket.socket()
    
    print socket_s.bind("10.0.2.125", 9100)
    
    #socket_s.listen(1)
    
    #print socket.getaddrinfo("10.0.2.125",9100)


    

obj = impresion()   