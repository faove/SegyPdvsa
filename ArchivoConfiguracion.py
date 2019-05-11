#!/usr/bin/env python 
#-*- coding:latin-1 -*-
import os

class ArchivoConfiguracion:
    def __init__(self):
        pass
        
    def Abrir(self):
        pass
        
    def Modificar(self):            
        try:            
            f  = open(""+os.environ['HOME']+"/"+"PixSegy.cfg", "r")
            fc = open(""+os.environ['HOME']+"/"+"PixSegy.cfg.copia", "w")

            while 1:
                
                linea1 = f.readline()
                print linea1
                if linea1 == '':
                    break
                elif linea1[:-1] == 'rutaGuardado..........................:':
                    
                    fc.write('rutaGuardado..........................:'+txt_bitapatch.Value+'\n')
                    
                elif linea1[:-1] == 'nombredearchivobitacora...............:':
                    
                    fc.write('nombredearchivobitacora...............:'+txt_bita.Value+'\n')
                    
                elif linea1[:-1] == 'modo..................................:':
                    
                    fc.write('modo..................................:'+Lta_mode.GetString(Lta_mode.GetSelection())+'\n')
                    
                elif linea1[:-1] == 'usuario...............................:':
                    
                    fc.write('usuario...............................:'+os.environ['USERNAME']+'\n')
                    
                else:    
                    fc.write(linea1)
            
            fc.close()
            f.close()
            
            
            
        ##            fc = open(""+os.environ['HOME']+"/"+"pdvsa.cfg.copia", "r")
        ##            f  = open(""+os.environ['HOME']+"/"+"pdvsa.cfg", "w")           
        ##            
        ##            for linea in fc:
        ##                f.write(linea)
        ##                
        ##            fc.close()
        ##            f.close()

        except IOError:
            print "El fichero no existe."