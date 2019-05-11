#!/usr/bin/env python 
#-*- coding:latin-1 -*-
import os
import sys
#Directorio de Proyecto PIXG metodo
#Directorio de Trabajo E86 otro
#Copiar la imagen metodo copiar

class manpro():
    '''
    
    '''
    def __init__(self):
        self.rutaManPro             =''
        self.nombreDirManProGrilla  ='Grilla'
        self.nombreDirManProMap     ='Map'
        self.nombreDirManProSegy    ='Segy'
        self.nombreDirManPro        ='PixG'
    def guardarconfig(self):
        pass
    def enviarconfig(self):
        '''Le informa al archivo de configuracion si sus valores 
        por default han cambiado
        '''
        pass  
    def manejadorconfig(self):
        '''
        
        '''
        pass      
    def chequearconfig(self,nombreimagen):
        '''
        Verifica si existe el directorio principal de proyecto, 
        si no lo localiza lo crea.
        PIXG/
            ->
            E86/
                ->
                Grilla/
                Map/
                Segy/
        
        Donde E86 es el archivo de imagen a abrir, por ejemplo:
        E86.jpg
                    
        '''
        
        directorio = os.environ['HOME']

        directorioOriginal = os.path.join(directorio, self.nombreDirManPro)

        dirimagen = nombreimagen.split(".")[0]
        
        if not os.path.isdir(directorioOriginal):
            
            os.mkdir(directorioOriginal)
            os.chdir(directorioOriginal)
            os.mkdir(dirimagen)
            os.chdir(dirimagen)
            os.mkdir(self.nombreDirManProGrilla)
            os.mkdir(self.nombreDirManProMap)
            os.mkdir(self.nombreDirManProSegy)
            print os.getcwd()
            
        else:
            
            os.chdir(directorioOriginal)
            
            if not os.path.isdir(dirimagen):
                
                os.mkdir(dirimagen)
                os.chdir(dirimagen)
                os.mkdir(self.nombreDirManProGrilla)
                os.mkdir(self.nombreDirManProMap)
                os.mkdir(self.nombreDirManProSegy)
                print os.getcwd()
                


obj = manpro()
obj.chequearconfig('E88.jpg')












##        print sys.exc_info.__str__
##          print dir(sys.argv.index)
####        print os.getcwd()
##
##        mifichero = os.getcwd()
##        
##        print mifichero, 'es un', 
##        if os.path.isfile(mifichero):
##            print 'fichero'
##        if os.path.isdir(mifichero):
##            print 'directorio'
##        if os.path.islink(mifichero):
##            print 'enlace'
##        print os.pardir    
##        directorio = os.environ['HOME']
##        print directorio
##        directorioOriginal = os.path.join(os.pardir, self.nombreDirManPro)
##        print directorioOriginal
##        
##        if not os.path.isdir(directorioOriginal):
##            os.mkdir(directorioOriginal)
##            os.chdir(directorioOriginal)
##            os.mkdir(self.nombreDirManProGrilla)
##            os.mkdir(self.nombreDirManProMap)
##            os.mkdir(self.nombreDirManProSegy)
##            
##            os.mkdir(directorio)
##            os.mkdir(directorio)            
##        os.chdir(directorio)
##        os.chdir(directorioOriginal) # vuelve al directorio inicial
##        os.chdir(os.environ['HOME']) # cambia al directorio home    
##        print os.curdir
