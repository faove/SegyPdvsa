import socket

import bitacora,sys

try:
    
    bita = bitacora.bitacora()
    
##    s = socket.socket()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # ahora se conecta al servidor web en el puerto 80 (http)
##    s.connect(("www.mcmillan-inc.com", 80))
##    s.connect(("NPI06416A", 80))
    s.connect(("10.0.2.125", 80))
    s.listen(1)
    
    sc, addr = s.accept()
    
    while True:
        
        recibido = sc.recv(1024)

        if recibido == "quit":
            break

        print "Recibido:", recibido
        
        sc.send(recibido)

    print "adios"

    sc.close()

    s.close()
    
except:
    
    bita.presentaVolcado(sys.argv[0],sys.exc_info())