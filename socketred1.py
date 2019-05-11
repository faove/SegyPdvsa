import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un objeto
##s = socket.socket()
print "done."


print "Looking up port number...",
port = socket.getservbyname('http', 'tcp')
print port

##s.connect(("10.0.2.2", port))    

s.bind(("10.0.2.2", port))  # añadimos el host y el puerto

s.listen(1) # Para aceptar las conexiones entrantes

sc, addr = s.accept() # Accept para escuchar
    while True: 
        recibido = sc.recv(1024)
        if recibido == 'quit':
            break
        print 'Recibido:', recibido
        sc.send(recibido)
        print 'adios'
    sc.close()
    s.close()