#!/usr/bin/env python 
#-*- coding:latin-1 -*-
import os
##import re
class ArchConfig:
    ver=''
    def __init__(self):
        self.rutaGuardado=''
        self.nombredearchivobitacora=''
        self.modo=''
        self.usuario=''
        self.Host=''
        self.usuarioAdmin=''

    def Abrir(self):
        try:
                
            f  = open(""+os.environ['HOME']+"/"+"PixSegy.cfg", "r")           
              
            while 1:
                
                linea1 = f.readline()
##                print linea1
                if linea1 == '':
                    break
                elif linea1[:14] == '[rutaGuardado]':
                    rutaGuardado = linea1[15:]
                    s = rutaGuardado.split('\t')
##                    print s[0]
                    self.rutaGuardado = s[0]                  
                elif linea1[:25] == '[nombredearchivobitacora]':
                    nombredearchivobitacora = linea1[26:]
                    sn = nombredearchivobitacora.split('\t')
##                    print sn[0]
                    self.nombredearchivobitacora = sn[0]                    
                elif linea1[:6] == '[modo]':
                    modo = linea1[7:]
                    smo = modo.split('\t')
##                    print smo[0]
                    self.modo = smo[0]                    
                elif linea1[:9] == '[usuario]':
                    usuario = linea1[10:]
                    smu = usuario.split('\t')
##                    print smu[0]
                    self.usuario = smu[0]                    
            f.close()
            return self.rutaGuardado,self.nombredearchivobitacora,self.modo,self.usuario
        
        except IOError:
            print "El fichero no existe."    


    def Modificar(self,rutaGuardado,nombredearchivobitacora,modo,usuario):            
        try: 
##            print "AQUI"           
            f  = open(""+os.environ['HOME']+"/"+"PixSegy.cfg", "r")
            fc = open(""+os.environ['HOME']+"/"+"PixSegy.cfg.copia", "w")

            while 1:
                
                linea1 = f.readline()
##                print linea1
                if linea1 == '':
                    break
                elif linea1[:14] == '[rutaGuardado]':
                    cr = linea1.split('#')                    
##                    print cr[1]
                    fc.write('[rutaGuardado]='+rutaGuardado+'\t#'+cr[1])
                    
                elif linea1[:26] == '[nombredearchivobitacora]=':
                    cn = linea1.split('#')
##                    print 'aqui'
##                    print cn[1]
                    fc.write('[nombredearchivobitacora]='+nombredearchivobitacora+'\t#'+cn[1])    
                    
                elif linea1[:7] == '[modo]=':
                    cm = linea1.split('#')
##                    print 'aqui'
##                    print cm[1]
                    fc.write('[modo]='+modo+'\t#'+cm[1])
                    
                elif linea1[:10] == '[usuario]=':
                    cu = linea1.split('#')
##                    print 'aqui'
##                    print cu[1]
                    fc.write('[usuario]='+usuario+'\t#'+cu[1])
                    
                else:    
                    fc.write(linea1)
            
            fc.close()
            f.close()
            
            
            fc = open(""+os.environ['HOME']+"/"+"PixSegy.cfg.copia", "r")
            f  = open(""+os.environ['HOME']+"/"+"PixSegy.cfg", "w")           
          
            for linea in fc:
                f.write(linea)
            
            
            fc.close()
            os.remove(""+os.environ['HOME']+"/"+"PixSegy.cfg.copia")
            f.close()

        except IOError:
            print "El fichero no existe."
            
            
            
            
##obj = ArchConfig()
##a = obj.Modificar('/home/falvarez','bitacora.log','a','falvarez')
##
##print a
##print type(a)