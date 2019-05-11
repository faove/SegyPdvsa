#!/usr/bin/python
#-*- coding:latin-1 -*-
import numpy 
import wx
import os
##import matplotlib.pyplot as plt
from matplotlib.figure import Figure
##import numpy as np
import pygame
from pygame.locals import *
from sys import exit
class pintargrilla:
    #'sushiplate.jpg'
    ##mouse_image_filename = 'fugu.png'
   
    
    
    def __init__(self):
##        import pygame
##        from pygame.locals import *
##        from sys import exit
        background_image_filename = '/home/fbonive/bonivework2/E102_MIG/E102_MIG-esc.jpg'
        SCREEN_SIZE = (1280,800)
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE,32)
        pygame.display.set_caption("GRAFICADOR DE LINEAS PARA TREMORES")
        background1 = pygame.image.load(background_image_filename).convert()
##        print background1
##        mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
        background=pygame.transform.scale(background1, SCREEN_SIZE)
        screen.blit(background, (0,0))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                screen.blit(background, (0,0))
##          screen.fill((255, 255, 255))
                mouse_pos = pygame.mouse.get_pos()
                for x in xrange(80,1100,20):
                    pygame.draw.line(screen, (255,0,  0), (x, 10), (x, 750),2)
##              pygame.draw.line(screen, (0, 0, 0), (x, 479), mouse_pos)
                for y in xrange(20,750,20):
                    pygame.draw.line(screen, (0, 0,255), (20, y), (1100, y),2)
##            pygame.draw.line(screen, (0, 0, 0), (639, y), mouse_pos)
###        x, y = pygame.mouse.get_pos()
##        x-= mouse_cursor.get_width() / 2
##        y-= mouse_cursor.get_height() / 2
##        screen.blit(mouse_cursor, (x, y))
                pygame.display.update()
class trans1:
    def __init__(self,cad):
        self.cad1=cad
        print 'iniciando convertidor'
    def pal2num(self):
        print 'pal2num'
        a2=''
        for pp in self.cad1:
            a1=pp.isspace()
            a2=a2+pp
        print a2
        
class lineagrid1:
    typegrid1=[]
    pixelx1=[]
    pixely1=[]
    dat=[-1,-1,-1,-1]
    def __init__(self,typegrid1,tag1):
        self.Marcado=0
        self.Color='b'
        self.ObjetoGrafico=[]
    def grafline(self,objgraf1):
        self.oblin1=objgraf1
        
    def leerdata(self):
        pass
    def __del__(self):
        try:
            del self.oblin1
            print 'Borrando el objeto linea #'+str(id(self))
        except:
            print 'El objeto grafico asociado a #'+str(id(self))+' fue borrado'
            

class ventana1(wx.Frame):
    nombredir1=''
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Archivos de GRILLA', size=(1000,600))
        p = wx.Panel(self)
        p.Show()
        self.nombrearchivoin=''
        self.listobj1=[]
##        statuBar = self.CreateStatusBar()    
    def LeerArchivo(self):
        print self.nombredir1
        print 'leerarchivo'
        p = wx.Panel(self)
        wildcard = "txx (*.txx)|*.txx|" 
##        os.getcwd()
##        print  a   
        dialog = wx.FileDialog(None,"Elige una Grilla", self.nombredir1,"",wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            a=dialog.Directory
            b=dialog.Filename
            self.nombrearchivoin=a+ '/' +b
##    def AsignarData(self
    def Graficar1(self):
        print 'Graficar1'
        print len(self.listobj1)
        
##        import matplotlib as mpl
##        mpl.use('GTKAgg') # to use GTK UI
        import matplotlib.pyplot as plt
        for k in range(len(self.listobj1)):
##            self.listobj1[k].grafline('1')
            
            tip1=self.listobj1[k].typegrid1
##            print tip1

            x1=self.listobj1[k].pixelx1
            y1=self.listobj1[k].pixely1
            a=[]
            if tip1 == [1]:
                self.listobj1[k].grafline(plt.plot(x1,y1,'r'))
            else:
                self.listobj1[k].grafline(plt.plot(x1,y1,'b'))
##            print wx.Newid()
            print id(a)

##            print x1
##            print k
        plt.show()

##    def graficagrillado(self):
##        wx.Frame.__init__(self, None, -1, 'ESTA ES LA GRILLA', size=(300, 300))
##        panel = wx.Panel(self, -1)
    def GuardarArchivo(self):#, self.nombredir1=''
        print self.nombredir1
        print 'GUARDARARCHIVO'
        p = wx.Panel(self)
        wildcard = "txx (*.txx)|*.txx|" 
##        os.getcwd()
##        print  a   
        dialog = wx.FileDialog(None,"Elige una Grilla", self.nombredir1,"",wildcard, wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            print 'adentro'
            a=dialog.Directory
            b=dialog.Filename
            self.nombrearchivoin=a+ '/' +b

    

class grilla1:
##    la grilla como objeto 0.1
##    atributos
     # esto permite manejar varias grillas
    numactivogrilla=0    
    idgrid1=[]
    numgrid1=0
##    DATOS DE NAVEGACIóN:
    cdp=[]
    shotpoint=[]
    typecoorgeo=[]
    coorgeo=[] 
##    # coordenadas geograficas y UTM
##    PARAMETROS DE PROYECCION:
    dxdp=[]
    dydp=[]
    bx1=[]
    by1=[]
##  metodos
##  {
##    leer
    def __init__(self):
        print 'Comenzando'
##        grilla1.
        grilla1.numactivogrilla +=1
        grilla1.idgrid1.append(id(self))
##        self.numactivogrilla +=2
        self.numgrid1 +=1
        self.objlingrid1=[]#self.__objlingrid1=[]
        self.idobjlingrid1=[]#self.__idobjlingrid1=[]
        self.__data=[]#self.__data     #data formato PDVI en forma matricial
        self.__NuLinHor=[] #numero de filas de la grilla
        self.__NuLinVer=[] # numero de columnas de la grilla
        self.__MantenerMarca=0 #Mantiene el estado actual de los objetos marcados(1)
##        return
    def CrearLinea(self):
        self.lin1=lineainterna()
        print 'CrearLinea'
        
    def BorrarLinea1(self):
        print 'BorrarLinea'
##        datamarca=self.__data[:,10]
        datamarca=numpy.nonzero(self.__data[:,10] > 0)
        datint=datamarca[0]
##        print type(datint[:])
        int111=[]
##            int111.append(int(aaa))
##        print type(int(int111))
##        print 'lo ultimo'
##        return
##        print self.__data
        data=numpy.delete(self.__data, datamarca[0],0)
        for aaa in datint:
            del(self.objlingrid1[aaa])
        print 'borrado'
##        dat1=data.reshape()
##        print data
        self.__NuLinHor
        self.__NuLinVer
      
    def LeerGrid1(self,nombredirx1=os.environ['HOME']):
##        os.O_DIRECTORY
##        print nombredirx1
        print 'leergrilla'
        app = wx.PySimpleApp()
        vent1=ventana1(parent=None, id=-1)
##        vent1.nombredir1=self.nombredir2
        vent1.nombredir1=nombredirx1
        vent1.LeerArchivo()
        vent1.Show()
        archivoin=vent1.nombrearchivoin
        print archivoin
        try:
            f = open(archivoin, 'r')
        except:
            print 'NO HAY ARCHIVO ESCOGIDO'
            return
        print type(f)
        tabla1=numpy.fromfile(archivoin,dtype=float, count=-1, sep='  ')
        tabla2=numpy.matrix(tabla1)
        numfila=tabla2.size/9
        tabla3=tabla2.reshape(numfila,9)
        tam1=tabla3.size
        contV=0
        contH=0
        tabla4=numpy.zeros((numfila,11))

        for i in range(numfila):            
            if tabla3[i,0]==1:
                odv1=lineagrid1(i,'Vert#'+str(i))
                contV +=1
##                print 'uno'
                odv1.typegrid1=[1]
            elif tabla3[i,0]==2:
                odv1=lineagrid1(i,'Hori#'+str(i))
                contH +=1
##                print '2'
                odv1.typegrid1=[2]
##            print tabla3[i,3:5]
            odv1.pixelx1=[tabla3[i,1],tabla3[i,2]]
            odv1.pixely1=[tabla3[i,3],tabla3[i,4]]
            odv1.dat=tabla3[i,5:8]
            tabla4[i,0:9]=tabla3[i,0:9]
            tabla4[i,9]=id(odv1)
            self.objlingrid1.append(odv1)
            self.idobjlingrid1.append(id(odv1))
            print 'fabricando el objeto '+ str(id(odv1));
        self.__data=tabla4
        self.__NuLinHor=contH
        self.__NuLinVer=contV
        f.close()
        
    def PasarDato(self,Tipo='DATA'):
        ''' esta funcion permite al usuario esterno acceder a los datos de grilla
        'DATA'de numero de lineas vericales y horizontales 'PNVH'
        '''
        print ''
        if Tipo=='DATA':
            return self.__data
        elif Tipo=='PNVH':
            return [self.__NuLinHor,self.__NuLinVer]
        else:
            'TIPO NO RECONOCIDO'
            return None
    def ProbarIntervaloDato(self,datvec=None,valor=None):
        '''Esta funcion retorna un None si el valor esta fuera del rango de
        y el valor si esta dentro del intervalo
        '''
        print ''
        if datvec!=None and valor!=None:
            max1=max(datvec)
            min1=min(datvec)
            if (valor>=min1) and (valor<max1):
                valor=valor
            else:
                valor=None
        else:
            print 'NO HAY VALORES CON LOS CUALES TRABAJAR'
        return valor
    
    def SelecionarLineas(self,Para_De_Escog=None,*parametros):
        '''
        funcion para selecionar definiremos 6 tipo de parametros para realizar la selecion
        estos parametros son:'OBJX':objetos;'XPIX':Xpixeles;'YPIX':Ypixeles;
        'LATY':Latitud;'LONX':Longitud;'UTMX':XUTM;'UTMY':YUTM;'CDPX',CDP;'SPXY':
        Shot Point;'ALLV':Todas las verticales;'ALLH':todas las Horizontales;
        'ALLW':;'TIME':Tiempo
        Los parametros esta dado en este orden parametros(1) es una lista de valores de
         los parametros ya escogido y lo que necesita es ser registrado por la matrix
          parametros(2) señala la escogencia en funcion de parametros maximos y 
        minimos dadas
        '''
        print 'SelecionarLineas'
        dat=self.__data
        if Para_De_Escog==None:
            print 'NO HAY TIPO DE VARIABLE ESCOGIDO'
            return 0 #no hizo nada
        elif Para_De_Escog=='INHOLD':
            print 'Manteniendo la MARCA'
            self.__MantenerMarca=1
        elif Para_De_Escog=='NOHOLD':
            print 'Se puede alterar la MARCA'
            self.__MantenerMarca=0
        Para_De_Escog=Para_De_Escog.upper()
        if len(parametros)==0:
            print 'NO HAY PARAMETROS PARA TRABAJAR'
            return 0 #no hizo nada
        print (parametros)
        max1=[]
        min1=[]
##        print 'hasta aqui'
        for k in range(0,9):
            max1.append(max(dat[:,k]))
            min1.append(min(dat[:,k]))
        if len(parametros)==1:
            dataesc=parametros[0]
            inter1=None
##            print dataesc
##            print inter1
        elif len(parametros)==2:
            dataesc=parametros[0]
            inter1=parametros[1]
            if inter1(1)>inter1(2):
##                print inter1
                inter2.append(inter1(2))
                inter2.append(inter1(1))
                inter1==inter2
            elif inter1(1)==inter1(2):
                print 'PASANDO A MODALIDAD DIRECTA'
                dataesc=inter1(1)
                
            
        
##        for par1 in parametros:
##            print par1
##            pass
        
##        print parametros
##        return
        limx=limy=[]
        self.objlingrid1
        NumeroDeLineas=len(self.objlingrid1)
        if Para_De_Escog=='OBJX':
            lindef=9
            
        elif Para_De_Escog=='XPIX':
            lindef=1
        elif Para_De_Escog=='YPIX':
            lindef=3
        elif Para_De_Escog=='LATY':
            lindef=[]
        elif Para_De_Escog=='LONX':
            lindef=[]
        elif Para_De_Escog=='UTMX':
            lindef=[]
        elif Para_De_Escog=='UTMY':
            lindef=[]
        elif Para_De_Escog=='CDPX':
            lindef=[]
        elif Para_De_Escog=='SPXY':
            lindef=[]
        elif Para_De_Escog=='ALLV':
            lindef=2
        elif Para_De_Escog=='ALLH':
            lindef=1
        elif Para_De_Escog=='ALLW':
            lindef=[]
        elif Para_De_Escog=='TIME':
            lindef=[]
        else:
            print 'NO HAY SELECCION PARA LA VARIABLE'+Para_De_Escog
            return 0 #no hizo nada
        resultbol=dat[:,0]*0
        print dat[:,lindef]
        if len(parametros)>=1:
##            print dataesc
            for k in range(len(dataesc)):
                c=numpy.where(dat[:,lindef]==dataesc[k],dat[:,0]*0+1, dat[:,0]*0)
##                print c
                resultbol=resultbol+c        
##        print resultbol
        self.__data[:,10]=resultbol
        return 1
    
    def GuardarGrilla1(self):
        pass
        
    def GraficarGrilla(self):
        print 'GraficarGrilla'
        print 'LINEAS PARA GRAFICAR '+str(len(self.objlingrid1))
        app = wx.PySimpleApp()
        vent1=ventana1(parent=None, id=-1)
##        vent1.nombredir1=self.nombredir2
##        print self.objlingrid1
        vent1.listobj1=self.objlingrid1
        vent1.Graficar1()
        vent1.Show()
    
        
    def __doc__(self):
        print 'DOCU'
##        grilla1.numactivogrilla -=1
        ##        return 
    def inn(self):
        for x in range(1,10,2):#['uno','dos','tres','probando']:
            print x
    def delete1(self):
        
        print 'deleting instance'#, self
    def __del__(self):
        print 'BORRANDO GRILLA'
        del(self.objlingrid1)

print 'termine' 

if __name__=='__main__':
    print 'COMENZANDO PROCEDIMIENTO DE GRILLA'
    odv1=grilla1()
    
##    print [odv1.idgrid1,odv1.numactivogrilla]
##    odv2=grilla1()
##    print [odv2.idgrid1,odv2.numactivogrilla]
##    odv3=odv1
    odv1.nombredir2='/home/fbonive/bonivework2/80GEB189/GRID'
    strdir1='/home/fbonive/bonivework2/80GEB189/GRID'
    odv1.LeerGrid1(strdir1)
    dat=odv1.PasarDato('DATA')
    VH=odv1.PasarDato('PNVH')
    print odv1.SelecionarLineas('objx',[1,odv1.idobjlingrid1[0],odv1.idobjlingrid1[1]])
##    odv1.SelecionarLineas('objx',[1,odv1.idobjlingrid1[0]])
##    print min1
##    print max1
    odv1.GraficarGrilla(),#[1,2],[3,6]
    odv1.BorrarLinea1()
    c = numpy.where(dat[:,0]==2,dat[:,0]*0+1, dat[:,0]*0)
    n=120/(1.80*1.80)
    print n

##    del odv1
##    print (dat)
##    print c
##    print odv1.objlingrid1.pixelx1
##    odv1.BorrarLinea(None,[1,odv1.idobjlingrid1[0]])
    odv1.GraficarGrilla(),#[1,2],[3,6]
    
    print 'QUISE BORRAR'
    
    