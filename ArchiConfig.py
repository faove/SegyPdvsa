#!/usr/bin/env python 
#-*- coding:latin-1 -*-
import os

class ArchConfig:
    ver=''
    def __init__(self):
        self.rutaGuardado           =''
        self.nombredearchivobitacora=''
        self.modo                   =''
        self.usuario                =''
        self.Host                   =''
        self.usuarioAdmin           =''
        self.NumeroMaximoDeMensajes =''
        self.NombreDeArchivoTot     =''
        self.guardaResumen          =False
        
    def Abrir(self):
        try:
                
            f  = open(""+os.environ['HOME']+"/"+"PixSegy.cfg", "r")           
              
            while 1:
                
                linea1 = f.readline()

                if linea1 == '':
                    break
                elif linea1[:14] == '[rutaGuardado]':
                    rutaGuardado = linea1[15:]
                    s = rutaGuardado.split('\t')
                    self.rutaGuardado = s[0]  
                                    
                elif linea1[:25] == '[nombredearchivobitacora]':
                    nombredearchivobitacora = linea1[26:]
                    sn = nombredearchivobitacora.split('\t')
                    self.nombredearchivobitacora = sn[0]   
                                     
                elif linea1[:6] == '[modo]':
                    modo = linea1[7:]
                    smo = modo.split('\t')
                    self.modo = smo[0]  
                                      
                elif linea1[:9] == '[usuario]':
                    usuario = linea1[10:]
                    smu = usuario.split('\t')
                    self.usuario = smu[0]
                    
                elif linea1[:24] == '[NumeroMaximoDeMensajes]':
                    NumeroMaximoDeMensajes = linea1[25:]
                    smn = NumeroMaximoDeMensajes.split('\t')
                    self.NumeroMaximoDeMensajes = smn[0]
                    
                elif linea1[:20] == '[NombreDeArchivoTot]':
                    NombreDeArchivoTot = linea1[21:]
                    snt = NombreDeArchivoTot.split('\t')
                    self.NombreDeArchivoTot = snt[0]
                    
                elif linea1[:15] == '[guardaResumen]':
                    guardaResumen = linea1[16:]
                    sng = guardaResumen.split('\t')
                    self.guardaResumen = sng[0]    
                                        
            f.close()
            
            return self.rutaGuardado,self.nombredearchivobitacora,self.modo,self.usuario,self.NumeroMaximoDeMensajes,self.NombreDeArchivoTot,self.guardaResumen
        
        except IOError:
            print "El fichero no existe."    


    def Modificar(self,rutaGuardado,nombredearchivobitacora,modo,usuario,NumeroMaximoDeMensajes,NombreDeArchivoTot,guardaResumen):            
        try: 

            f  = open(""+os.environ['HOME']+"/"+"PixSegy.cfg", "r")
            
            fc = open(""+os.environ['HOME']+"/"+"PixSegy.cfg.copia", "w")

            while 1:
                
                linea1 = f.readline()

                if linea1 == '':
                    
                    break
                
                elif linea1[:14] == '[rutaGuardado]':
                    
                    cr = linea1.split('#')                    

                    fc.write('[rutaGuardado]='+rutaGuardado+'\t#'+cr[1])
                    
                elif linea1[:26] == '[nombredearchivobitacora]=':
                    
                    cn = linea1.split('#')

                    fc.write('[nombredearchivobitacora]='+nombredearchivobitacora+'\t#'+cn[1])    
                    
                elif linea1[:7] == '[modo]=':
                    
                    cm = linea1.split('#')

                    fc.write('[modo]='+modo+'\t#'+cm[1])
                    
                elif linea1[:10] == '[usuario]=':
                    
                    cu = linea1.split('#')

                    fc.write('[usuario]='+usuario+'\t#'+cu[1])
                    
                elif linea1[:25] == '[NumeroMaximoDeMensajes]=':
                    
                    ca = linea1.split('#')

                    fc.write('[NumeroMaximoDeMensajes]='+NumeroMaximoDeMensajes+'\t#'+ca[1])
                
                elif linea1[:21] == '[NombreDeArchivoTot]=':
                    
                    ct = linea1.split('#')
                    
                    fc.write('[NombreDeArchivoTot]='+NombreDeArchivoTot+'\t#'+ct[1])  
                    
                elif linea1[:16] == '[guardaResumen]=':
                    
                    cg = linea1.split('#')
                    
                    fc.write('[guardaResumen]='+guardaResumen+'\t#'+cg[1])
                    
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