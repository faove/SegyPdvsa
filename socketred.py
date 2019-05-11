import socket 

class socketf:
    print "Creating socket...",
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "done."

    print "Looking up port number...",
    port = socket.getservbyname('http', 'tcp')
    print "done."

    print "Connecting to remote host on port %d..." % port,
    s.connect(("10.0.2.2", port))
    ##s.connect(("192.168.1.1", port))
    print "done."

    print "Connected from", s.getsockname()
    print "Connected to", s.getpeername()
    ##socket.socket()
    ####socket_s.bind(("localhost", 80)) 
    ##socket_s.listen(10)  
    ##  
    ####socket_c, (host_c, puerto_c) = socket_s.accept()
    
    