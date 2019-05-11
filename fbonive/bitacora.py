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
        
##        objarch = ArchiConfig.ArchConfig()
##        
##        ar = objarch.Abrir()
##        
##        self.rutaGuardado = ar[0]
##        self.nombredearchivobitacora = ar[1]
##        self.modo = ar[2]
##        self.usuario = ar[3]
##        self.usuarioAdmin = ''
##        self.host = ''
##        self.modo = ''

        self.usuario = ''
        self.modo = ''
##        self.usuarioAdmin = os.environ['USERNAME']
        self.usuarioAdmin = os.environ['USERNAME']
        self.nombredearchivobitacora = ''
        self.rutaGuardado = ''
        self.host = os.uname()[1]
                
##        nombreDeArchivo='bitacor.log'
    
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
##        var=self._extract_info(nombredearchivobitacora)
##        if nombredearchivobitacora is None: 
##            print "es vacio"           
##            now = datetime.datetime.now()
##            ts = now.strftime('%Y-%m-%d_%H%M%S')
##            nombredearchivobitacora = '%s.log' % (sys.argv[0], ts)            
##        else:  
##            print nombreDeArchivoBitacora          
##            nombredearchivobitacora='bita.log'

##        if self.modo is None:
##            self.modo = 'a'
##        elif self.modo is '':
##            self.modo = 'a'
        
##        if rutaGuardado is None:
##            rutaGuardado = rutaGuardadoXdefecto
##        else:
##            rutaGuardado = rutaGuardado
            
##           format='%(asctime)s %(levelname)-8s',
##        logging.getLogger(os.environ['USERNAME'])
        if rutinaerror <> None:
            rutinaerror = str(rutinaerror)
        if nombreobjeto <> None:
            nom = nombreobjeto.split('/')
            tam = len(nom)
            num = tam-1
##            print nom[num]
##            print lengh(nom)
##        print 'modo:' + self.modo + ''
##        print 'Usuario:' + self.usuario + ''
##        print 'UsuarioAdmin:' + self.usuarioAdmin + ''
##        print 'Nombre:' + self.nombredearchivobitacora + ''
##        print 'Ruta:' + self.rutaGuardado + ''
##        print 'Host:' + self.host + ''
##        print 'Nivel:' + nivel + ''
##        print 'Mensaje:' + mensaje + ''
        
##        name=self.usuario

##        %(module)s  NOMBRE DEL MODULO ACTUAL
        
        if nivel is 'DEBUG':
            logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s '+self.usuario+' '+self.usuarioAdmin+' '+nom[num]+' '+rutinaerror+' '+self.host+'%(module)s  %(levelname)-4s %(message)s',                        
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

    def guardaResumen():
        pass
    def presentaVolcado():
        pass
    def BorrarBitacora():
        pass
    
    #nombredearchivobitacora=None,modo=None,rutaGuardado=None,nivel=None,mensaje=None    
    def ConfigurarBitacora(self,rutaGuardado,nombredearchivobitacora,modo,usuario):
        '''
        Recibe de las rutinas de inicialización de la aplicación
        los parámetros de configuración de funcionamiento de la
        bitácora leídos del archivos de configuración.
        '''    
        #Asignacion de los valores generales de bitacora
        self.rutaGuardado = rutaGuardado
        
        self.nombredearchivobitacora = nombredearchivobitacora
        
        self.modo = modo
        
        self.usuario = usuario
        
        return rutaGuardado,nombredearchivobitacora,modo,usuario    

##obj=bitacora()
##nombredearchivobitacora="bitacora.log"
##usuario=os.environ['USERNAME']
##usuarioAdmin=''
##modo="a"
##rutaGuardado=os.environ['HOME']
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


