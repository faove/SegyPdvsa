import logging

import datetime
##logging.warning

##print datetime.datetime.today()
class bita2:
    '''
    bitacora: necesita nivel de error: ERROR,DEBUG,WARNING
    
    '''
    def construirmensaje(self,mensaje,nivel):
        ARCHIVO_LOG="ejemplo_01.log"
        if nivel == 'error':
##            ARCHIVO_LOG="ejemplo_01.log"
            ##FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'   datefmt=datetime.datetime.today(),
            logging.basicConfig(filename=ARCHIVO_LOG)

            ##logging.basicConfig(format=FORMAT)

            ##logging.warning('Warning.. del sistema')
    ##        logging.getLevelName(nivel)
            logging.error(mensaje)
            ##logging.debug('Debug.. del sistema')
        elif nivel=='debug':
            logging.basicConfig(filename=ARCHIVO_LOG)
            logging.debug(mensaje)

##logging.basicConfig(
obj = bita2()
obj.construirmensaje('hola','debug')
