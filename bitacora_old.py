#!/usr/bin/env python 
#-*- coding:latin-1 -*-
import logging

import datetime

import os


# --------------------==== Atributos de la clase bitacora ====----------------------- #

# rutaGuardado : indica la ruta definida por el usuario dels sistema
# rutaGuardadoXdefecto = '/home/falvarez/Escritorio/python_soft/version\ 0.0.0.1/'
##rutaGuardadoXdefecto = os.environ['HOME']
#print os.environ
# Nivel : indica el level de error puede ser DEBUG,INFO,ERROR,WARNING,CRITICAL,NOTSET
##nivel=None

# FechaHoraInicio la fecha y hora viene dado por la varible asctime que esta en format

# Usuario : esta variable es tomada del sistema operativo, el usuario va hacer la sesion
# actual
##usuario=None

# mode : indica si el archivo de log esta en modo solo lectura/escritura
mode=None

# condiciondeborrado : cuanto tiempo tiene para borrar una lista de bitacora
condiciondeborrado=None

# mensaje : informacion de evento ocurrido dato suministrado po el usuario
mensaje=''

# ----------------------------==== Fin de Atributos ====---------------------------- #

class bitacora:
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
        bitacora.construirmensaje(log_fn=None,  mode=None,rutaGuardado = rutaGuardadoXdefecto, 
                            nivel=None,mensaje=None, format='%(asctime)s|%(name)s|%(levelname)s| %(message)s'):
        bitacora.guardaResumen(...
        bitacora.presentaVolcado(...
        bitacora.BorrarBitacora(...
    """    
    def construirmensaje(log_fn=None,  mode=None,rutaGuardado = None, \
                            nivel=None,mensaje=None, format='%(asctime)s|%(name)s|%(levelname)s|'):
                            
        '''   ---Metodo Construir Mensaje---
        Atributos    :
        rutaGuardado : indica la ruta (path) en donde guardara el archivo log
        usuario      : esta variable es tomada del sistema operativo, el usuario va hacer la sesion actual
        nivel        : indica el level de error puede ser DEBUG,INFO,ERROR,WARNING,CRITICAL,NOTSET        
        mensaje      : informacion de evento ocurrido dato suministrado po el usuario
        format       : %(asctime)-15s %(clientip)s %(user)-8s %(message)s
        FechaHoraInicio la fecha y hora viene dado por la varible asctime que esta en format 
        
        '''    
        if log_fn is None:
            now = datetime.datetime.now()
            ts = now.strftime('%Y-%m-%d_%H%M%S')
            log_fn = '%s.log' % (sys.argv[0], ts)
        else:
            log_fn='myapp.log'
##
        if mode is None:
            mode = 'a'
        
        if rutaGuardado is None:
            rutaGuardado = rutaGuardadoXdefecto
        else:
            rutaGuardado = rutaGuardado
            
##           format='%(asctime)s %(levelname)-8s',
        
##        logging.getLogger(os.environ['USERNAME'])
         
        if nivel is 'DEBUG':                        
            logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(name)s %(levelname)-8s %(message)s',                        
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename= '' + rutaGuardado + '/' + log_fn,
                        filemode='a')
            logging.debug(mensaje)
            logging.getLogger(os.environ['USERNAME'])
            
        elif nivel is 'INFO':
            logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s %(levelname)-8s %(message)s',                        
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename= '' + rutaGuardado + '/' + log_fn,
                        filemode='a')                        
            logging.info(mensaje)
            
        elif nivel is 'WARNING':
            logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)-15s %(levelname)-8s %(message)s',                        
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename= '' + rutaGuardado + '/' + log_fn,
                        filemode='a')                        
            logging.warning(mensaje)
        elif nivel is 'WARNING':
            logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)-15s %(levelname)-8s %(message)s',                        
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename= '' + rutaGuardado + '/' + log_fn,
                        filemode='a')                        
            logging.warning(mensaje)
        
##        print 'aqui' 
    def guardaResumen():
        pass
    def presentaVolcado():
        pass
    def BorrarBitacora():
        pass
        
##    def __doc__(self):        
##if __name__=='__main__':     
##ARCHIVO_LOG="ejemplo_01.log"
##FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'   datefmt=datetime.datetime.today(),
##logging.basicConfig(filename=ARCHIVO_LOG, level=logging.WARNING, datefmt=fecha)
##logging.basicConfig(format=FORMAT)
##logging.warning('Error.. del sistema')
##logging.debug('Debug.. del sistema')
##log = bitaexample2.inicia_bitacora()
##log.debug('Error del sistema')

obj=bitacora()

##obj.construirmensaje(nivel='WARNING',mensaje='Error en el modulo de bitacora')
##obj.construirmensaje(nivel='WARNING',rutaGuardado ='/home/falvarez/Escritorio/python_soft/version\ 0.0.0.1/',mensaje='Error en el modulo de bitacora')
##print obj.__doc__

obj.construirmensaje(nivel='DEBUG',mensaje='Error en el modulo de bitacora, debug')

##obj.advertencia(mensaje='Advertencia')


##Nivel	Cuando se usa
##DEBUG	La informacion detallada, por lo general de interés sólo cuando el diagnóstico de problemas.
##INFO	La confirmacion de que las cosas están funcionando como se esperaba.
##ADVERTENCIA	Una indicación de que algo inesperado sucedió, o indicativo de algún problema en el futuro cercano (por ejemplo, "espacio en disco"). El software sigue funcionando como se esperaba.
##ERROR	Debido a un problema más serio, el software no ha sido capaz de realizar alguna función.
##CRÍTICO	Un grave error, que indica que el programa en sí mismo puede ser capaz de seguir corriendo.

