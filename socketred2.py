import socket  
  
##s = socket.socket() 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = socket.getservbyname('http', 'tcp')

print "Connecting to remote host on port %d..." % port,

s.bind(("10.0.2.2", port)) 

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