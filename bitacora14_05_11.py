#!/usr/bin/env python 
#-*- coding:latin-1 -*-
import logging

import datetime

import os,sys,ArchiConfig


# --------------------==== Atributos de la clase bitacora ====----------------------- #

# rutaGuardado : indica la ruta definida por el usuario dels sistema
# rutaGuardadoXdefecto = '/home/falvarez/Escritorio/python_soft/version\ 0.0.0.1/'
##rutaGuardadoXdefecto = os.environ['HOME']
##nombredearchivobitacora=None
##nombreDeArchivo='bitacor.log'
#print os.environ
# Nivel : indica el level de error puede ser DEBUG,INFO,ERROR,WARNING,CRITICAL,NOTSET
##nivel=None

# FechaHoraInicio la fecha y hora viene dado por la varible asctime que esta en format

# Usuario : esta variable es tomada del sistema operativo, el usuario va hacer la sesion
# actual
##usuario=None

# modo : indica si el archivo de log esta en modo solo lectura/escritura
##modo=None

##nombredearchivobitacora=None

# condiciondeborrado : cuanto tiempo tiene para borrar una lista de bitacora
##condiciondeborrado=None

# mensaje : informacion de evento ocurrido dato suministrado po el usuario
##mensaje=''

# ----------------------------==== Fin de Atributos ====---------------------------- #

class bitacora():
    def __init__(self):
        
        global bita
        
        objarch = ArchiConfig.ArchConfig()
        ar = objarch.Abrir()

        self.rutaGuardado               = ar[0]
        self.nombredearchivobitacora    = ar[1]
        self.modo                       = ar[2]
        self.usuario                    = ar[3]
        self.usuarioAdmin               = os.environ['USERNAME']
        self.host                       = os.uname()[1]
        self.NumeroMaximoDeMensajes     = ar[4]
        self.NombreDeArchivoTot         = ar[5]
        self.guardaResumen              = ar[6]
        
    """
    ----  Objeto Bitacora ----
    Descripcion:
    
    Atributos:
        rutaGuardado: indica la ruta (path) en donde guardara el archivo log        
        usuario : esta variable es tomada del sistema operativo, el usuario va hacer la sesion actual
        nivel : indica el level de error puede ser DEBUG,INFO,ERROR,WARNING,CRITICAL,NOTSET        
        mensaje : informacion de evento ocurrido dato suministrado po el usuario
        FechaHoraInicio la fecha y hora viene dado por la varible asctime que esta en format , datefmt='%m/%d/%Y %I:%M:%S %p'
    Metodos 
        bitacora.construirmensaje(log_fn=None,  modo=None,rutaGuardado = rutaGuardadoXdefecto, 
                            nivel=None,mensaje=None, format='%(asctime)s|%(name)s|%(levelname)s| %(message)s'):
        bitacora.guardaResumen(...
        bitacora.presentaVolcado(...
        bitacora.BorrarBitacora(...
        def construirmensaje(nombredearchivobitacora=None,modo=None,rutaGuardado=None,nivel=None,mensaje=None):
    """    
    def construirmensaje(self,nombreobjeto,rutinaerror,nivel,mensaje):
                            
        '''   ---Metodo Construir Mensaje---
        def construirmensaje(self,nombredearchivobitacora,modo,rutaGuardado,usuario,usuarioAdmin,host,nivel,mensaje):
        Atributos    :
        rutaGuardado : indica la ruta (path) en donde guardara el archivo log
        usuario      : esta variable es tomada del sistema operativo, el usuario va hacer la sesion actual
        nivel        : indica el level de error puede ser DEBUG,INFO,ERROR,WARNING,CRITICAL,NOTSET        
        mensaje      : informacion de evento ocurrido dato suministrado po el usuario
        format       : %(asctime)-15s %(clientip)s %(user)-8s %(message)s
        FechaHoraInicio la fecha y hora viene dado por la varible asctime que esta en format 
        
        '''    
        if rutinaerror <> None:
            rutinaerror = str(rutinaerror)
        if nombreobjeto <> None:
            nom = nombreobjeto.split('/')
            tam = len(nom)
            num = tam-1
      
        if nivel is 'DEBUG':
            
            logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s '+self.usuario+' '+self.usuarioAdmin+' '+nom[num]+' '+rutinaerror+' '+self.host+' %(levelname)-4s %(message)s',                        
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename= '' + self.rutaGuardado + '/' + self.nombredearchivobitacora,
                        filemode=self.modo)
                        
            logging.debug(mensaje)
            
        elif nivel is 'INFO':
            
            logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s '+self.usuario+' '+self.usuarioAdmin+' '+nom[num]+' '+rutinaerror+' '+self.host+' %(levelname)-4s %(message)s',                        
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename= '' + self.rutaGuardado + '/' + self.nombredearchivobitacora,
                        filemode=self.modo)
                                                
            logging.info(mensaje)
            
        elif nivel is 'WARNING':
            
            logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)-15s '+self.usuario+' '+self.usuarioAdmin+' '+nom[num]+' '+rutinaerror+' '+self.host+' %(levelname)-4s %(message)s',                        
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename= '' + self.rutaGuardado + '/' + self.nombredearchivobitacora,
                        filemode=self.modo)
                                              
            logging.warning(mensaje)
            
        elif nivel is 'ERROR':
            
            logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)-15s '+self.usuario+' '+self.usuarioAdmin+' '+nom[num]+' '+rutinaerror+' '+self.host+' %(levelname)-4s %(message)s',                        
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename= '' + self.rutaGuardado + '/' + self.nombredearchivobitacora,
                        filemode=self.modo) 
                                               
            logging.error(mensaje)
            
        elif nivel is 'CRITICAL':
            
            logging.basicConfig(level=logging.CRITICAL,
                        format='%(asctime)-15s '+self.usuario+' '+self.usuarioAdmin+' '+nom[num]+' '+rutinaerror+' '+self.host+' %(levelname)-4s %(message)s',                        
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename= '' + self.rutaGuardado + '/' + self.nombredearchivobitacora,
                        filemode=self.modo)
                                                
            logging.critical(mensaje)

    def guardarResumen(self):
        
        try: 
            
            ruta   = self.rutaGuardado 
            
            nombre = self.nombredearchivobitacora
            
            fc = open(""+ruta+"/"+nombre, "r")
            
            condebug    = 0
            
            conerror    = 0
            
            concritical = 0
            
            conwarning  = 0
            
            coninfo     = 0
            
            while 1:
                
                linea = fc.readline()
                
                if linea.find("DEBUG") >= 0: 
                      
                    condebug    += 1                    
                    
                elif linea.find("ERROR") >= 0:
                    
                    conerror    += 1                    
                    
                elif linea.find("CRITICAL") >= 0:
                   
                    concritical += 1                    
                        
                elif linea.find("WARNING") >= 0:
                    
                    conwarning  += 1                    
                    
                elif linea.find("INFO") >= 0:
                    
                    coninfo     += 1                    
                    
                else:
                    break    
                    
           
            fc.close()
            
            arch=str(self.NombreDeArchivoTot)
            
            f  = open(""+ruta+"/"+arch+"", "r")
            
            fc  = open(""+ruta+"/guardaResumen.copia.tot", "w")
            
            while 1:
                
                linea1 = f.readline()
                
                if linea1 == '':
                    break
                
                elif linea1[:7] == '[DEBUG]':
##                    print condebug
                    fc.write('[DEBUG]='+str(condebug)+'\n')
                    
                elif linea1[:7] == '[ERROR]':
##                    print conerror
                    fc.write('[ERROR]='+str(conerror)+'\n')  
                    
                elif linea1[:10] == '[CRITICAL]':
##                    print concritical
                    fc.write('[CRITICAL]='+str(concritical)+'\n') 
                    
                elif linea1[:9] == '[WARNING]':
##                    print conwarning
                    fc.write('[WARNING]='+str(conwarning)+'\n')
                    
                elif linea1[:6] == '[INFO]':
##                    print coninfo
                    fc.write('[INFO]='+str(coninfo)+'\n')    
                    
                else:    
                    fc.write(linea1)   
            
            f.close()
            
            fc.close()
            
            fc  = open(""+ruta+"/guardaResumen.copia.tot", "r")
            
            f  = open(""+ruta+"/"+arch+"", "w")
            
            for linea in fc:

                f.write(linea)
            
            
            fc.close()
            
            os.remove(""+ruta+"/guardaResumen.copia.tot")
            
            f.close()
            
        except:
            print "Verifique guardar Resumen"
            
            
    def presentaVolcado():
        pass
        
    def BorrarBitacora(self,rutaGuardado,nombredearchivobitacora):
        '''
        Metodo privado que se ejecuta para escribir un archivo .tot si la
        bandera del mismo nombre (guardaResumen) está activada.
        '''
        try:
                
            numLineas  = 0  
            maxLineas  = 0
            meLineas   = 0
            numLineasT = 0
            
            #--------------------------------------
            #Valor tomado del archivo de conf
            #indica el numero de mensajes a guardar
            #--------------------------------------
            
            maxLineas = int(self.NumeroMaximoDeMensajes)
            
##            print "Numero lineas cfg:"
##            print maxLineas
            
            f  = open(""+rutaGuardado+"/"+nombredearchivobitacora+"", "r")
            
            #--------------------------------------
            #Cuenta el numero de lineas del .log
            #--------------------------------------
            numLineasT = len(f.readlines())
            
            f.close()
            
##            print "Numero max:"
##            print numLineasT
            
            meLineas = maxLineas-numLineasT
            
            meLineas_resta = meLineas
           
            
            
            #--------------------------------------
            #Si la resta da negativa * -1
            #--------------------------------------
            if meLineas < 1:
                
                meLineas = meLineas*(-1)
                
            if meLineas_resta < 1:
                
                meLineas_resta = meLineas_resta*(-1)
                
##            print "meLineas_resta"
##            print meLineas_resta
##            print "meLineas"
##            print meLineas    
##            print meLineas
##            print "maxLineas"
##            print maxLineas
            #--------------------------------------
            #Si las lineas del archivo son menos
            #que el numero 
            #--------------------------------------
            if meLineas < maxLineas:
                
                meLineas = maxLineas
##            print "melineas"    
##            print meLineas
            
##            if meLineas <= maxLineas:
            if meLineas > numLineasT:
                cambia = False
            else:
                cambia = True

##            print cambia
##            print "aqui"
                
            if cambia:
                
                f  = open(""+rutaGuardado+"/"+nombredearchivobitacora+"", "r")
                
                fc  = open(""+rutaGuardado+"/bitacora_copia.log", "w")
##                print numLineas
                while 1:                    
                    linea1 = f.readline()                    
##                    print "increm"
##                    print numLineas
                    
                    if meLineas_resta <= numLineas:
                        if linea1 == '':
                            break
                        else:
##                            print linea1
                            fc.write(linea1)
                            
##                        print "numLineasT:"
##                        print numLineasT
                        
                        if numLineas == numLineasT:
                            break
                                                         
                    numLineas += 1
            

                fc.close()
                
                f.close()
           
                fc = open(""+rutaGuardado+"/bitacora_copia.log", "r")
                
                f  = open(""+rutaGuardado+"/"+nombredearchivobitacora+"", "w")           
              
                for linea in fc:

                    f.write(linea)
                
                fc.close()
                
                os.remove(""+rutaGuardado+"/bitacora_copia.log")
                
                f.close()
            
        except:
            
            print "Verifique en el metodo Borrar Bitacora"
    
    #nombredearchivobitacora=None,modo=None,rutaGuardado=None,nivel=None,mensaje=None    
    def ConfigurarBitacora(self,rutaGuardado,nombredearchivobitacora,modo,usuario,NumeroMaximoDeMensajes,
        NombreDeArchivoTot,guardaResumen):
        '''
        Recibe de las rutinas de inicialización de la aplicación
        los parámetros de configuración de funcionamiento de la
        bitácora leídos del archivos de configuración.
        '''
        try:
            #Asignacion de los valores generales de bitacora
            self.rutaGuardado = rutaGuardado
        
            self.nombredearchivobitacora = nombredearchivobitacora
        
            self.modo = modo
        
            self.usuario = usuario
        
            self.NumeroMaximoDeMensajes = NumeroMaximoDeMensajes
            
            self.NombreDeArchivoTot = NombreDeArchivoTot
            
            self.guardaResumen = guardaResumen
       
            return rutaGuardado,nombredearchivobitacora,modo,usuario,NumeroMaximoDeMensajes,NombreDeArchivoTot,guardaResumen
        except:
            print "Verifique en el metodo Configurar Bitacora "
            
            
            
            
            
            
            
            
            
        
        
        








            

            
            

####obj=bitacora()
####nombredearchivobitacora="bitacora.log"
####rutaGuardado=os.environ['HOME']
##########print rutaGuardado
####obj.BorrarBitacora(rutaGuardado,nombredearchivobitacora)
####obj.guardarResumen()
##
##obj.BorrarBitacora(rutaGuardado,nombredearchivobitacora)

##usuario=os.environ['USERNAME']
##usuarioAdmin=''
##modo="a"

##nivel="DEBUG"
##mensaje="HOLA MUNDO2"
####host = os.uname()[1]
####
####print os.uname()
##obj.construirmensaje(nivel,mensaje)


##print nombre

##obj.construirmensaje('bitacora.log','a','/home','Error en el modulo de bitacora debug')
##dir(obj.construirmensaje)
##obj.construirmensaje('log.log','a',nivel='DEBUG','/home/',mensaje='Error en el modulo de bitacora, debug')


