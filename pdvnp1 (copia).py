#!/usr/bin/env python
#-*- coding:latin-1 -*-

#Importamos el modulo de wxPython
import wx

import os,sys

import wx.lib.imagebrowser as imagebrowser 

#El objeto de la figura a traves de MatplotLib
##from matplotlib.figure import Figure
##import matplotlib.pyplot as plt

#Funciones para la creacion de imagenes Numpy
import numpy as np

###importas el objecto WxAgg, este se une con Figure
##from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
###importas el objecto WxAgg, este se une con Figure
##from matplotlib.backends.backend_wx import NavigationToolbar2Wx

#Para manejar imagenes 
##from pylab import *

#Librerias PIL
from PIL import Image

import bitacora

import ArchiConfig

class MDIFrame(wx.MDIParentFrame):

    def __init__(self):
        
        #----------------------------OJO----------------------------------
        #Se debe configurar la primera vez que se instala pdvnp
        #Utilizando las variables de entorno del sistema os.environ['HOME']
        #----------------------------OJO----------------------------------
        
        
        #Atributos globales de Frame
        global win,win_bita,txt_bitapatch,txt_bita,Lta_mode,bto_examinar,bto_guardar,bto_cerrar

        #Atributos globales de Bitacora
        global bita
        
        #Atributos globales de ArchiConfig
        global  arch
        
        arch = ArchiConfig.ArchConfig()
        
        #Se debe activar todos los valores por defecto
        #estos valores lo tiene la clase ArchiConfig
        a = arch.Abrir()
        
        #a[0] es la rutadeGuardado
        #a[1] es el nombredearchivobitacora
        #a[2] es el modo 
        #a[3] es el usuario
        print a
        #Instancio Bitacora
        bita = bitacora.bitacora()
        
        #llamar a configurar_bitacora 
        bita.ConfigurarBitacora(a[0],a[1],a[2],a[3])
        
        print bita.modo + bita.rutaGuardado + bita.nombredearchivobitacora + bita.usuario
        
        #wx.Frame.__init__(self, parent,id,'Procesador de Imagen Raster Version 1.1.1.1', size=(1000,600))
        
        wx.MDIParentFrame.__init__(self, None, -1, "MDI Padre")
        
        win            = wx.MDIChildFrame(self, -1, "Hijo",style = 0)
        win_bita       = wx.MDIChildFrame(self, 2, "Configurar Bitacora")
        
        lbl_bita       = wx.StaticText(win_bita,-1,"Nombre del archivo:",(80,50))
        txt_bita       = wx.TextCtrl(win_bita,-1,bita.nombredearchivobitacora,(300,50),size=(175, -1))
        
        lbl_bitapatch  = wx.StaticText(win_bita,-1,"Ruta donde se guarda los archivos:",(80,80))
        txt_bitapatch  = wx.TextCtrl(win_bita,-1,bita.rutaGuardado,(300,80),size=(175, -1))

        lbl_bitalista  = wx.StaticText(win_bita,-1,"Sobrescribir (w) Anadir (a):",(80,110))
        
        Lista          = ['a','w']
        Lta_mode       = wx.Choice(win_bita,-1,(300,110),choices=Lista)
        
        bto_examinar   = wx.Button(win_bita,-1,"Examinar",pos=(500,80))
        self.Bind(wx.EVT_BUTTON,self.OnDirectorio,bto_examinar)
    
        bto_guardar    = wx.Button(win_bita,-1,"Guardar",pos=(400,150))
        self.Bind(wx.EVT_BUTTON,self.Onfile,bto_guardar)
    
        bto_cerrar     = wx.Button(win_bita,-1,"Cerrar",pos=(500,150))
        self.Bind(wx.EVT_BUTTON,self.OnExitWindow,bto_cerrar)
        
        
##        print ArchiConfig.ver
##        arch = ArchiConfig.ArchConfig()
##        
##        #Se debe activar todos los valores por defecto
##        #estos valores lo tiene la clase ArchiConfig
##        a = arch.Abrir()
##        
##        #a[0] es la rutadeGuardado
##        #a[1] es el nombredearchivobitacora
##        #a[2] es el modo 
##        #a[3] es el usuario
####        print a[3]
##
##        #Instancio Bitacora
##        bita = bitacora.bitacora()
##        
##        #llamar a configurar_bitacora 
##        bita.ConfigurarBitacora(a[0],a[1],a[2],a[3])
        
##        print modo
##        print bita.modo + bita.rutaGuardado + bita.nombredearchivobitacora + bita.usuario
        
##        bitacora.bitacora.modo = Lta_mode.GetString(Lta_mode.GetSelection())
        
##        p = wx.Panel(self)
        self.MakeMenuBar()  
              
##        self.initpos = 100
##        self.sp = wx.SplitterWindow(self)
##        self.p1 = wx.Panel(self.sp)
##        self.p2 = wx.Panel(self.sp,style=wx.SUNKEN_BORDER)            
        #self.p2.Hide()
        #self.p1.wx.SetBackgroundColour("pink")
        #self.p2.wx.SetBackgroundColour("sky blue")
##        self.sp.Initialize(self.p1)
##        self.sp.SetMinimumPaneSize(10)
##        
##        self.sp.SplitVertically(self.p1, self.p2,self.initpos)
##        #ListBox
##        dirlist = ['o','u','y']
##        listBox = wx.ListBox(self.p1,-1,(20,20),(80,120),dirlist, wx.LB_SINGLE)
##        listBox.SetSelection(3)
        
        #self.figure = Figure()
        #self.axes = self.figure.add_subplot(111)    
        
    
##        self.figure = Figure()
##        self.axes = self.figure.add_subplot(111)
##        self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)
##        self.sizer = wx.BoxSizer(wx.VERTICAL)
##        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
##        self.toolbar = NavigationToolbar2Wx(self.canvas)
##        self.toolbar.Realize()
##        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
##        self.toolbar.Show()
##        self.SetSizer(self.sizer)
##        self.Fit()
    def MakeMenuBar(self):    
        statuBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        abririmage=toolbar.AddSimpleTool(wx.NewId(),wx.Image('folder_picture.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo de Imagen","")
        toolbar.AddSimpleTool(1,wx.Image('folder_table.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo de Grilla","")
        toolbar.AddSimpleTool(2,wx.Image('folder_image.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo de Proyeccion","")
        toolbar.AddSimpleTool(3,wx.Image('folder_bell.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo de Perfil Temporal","")
        toolbar.AddSimpleTool(4,wx.Image('folder_page.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo de Perfil","")
        toolbar.AddSimpleTool(5,wx.Image('folder_go.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo de Arribos","")
        toolbar.AddSimpleTool(6,wx.Image('folder_feed.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Abrir Archivo SEGY","")
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(7,wx.Image('guardar_image.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo de Imagen","")
        toolbar.AddSimpleTool(8,wx.Image('guardar_grid.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo de Grilla","")
        toolbar.AddSimpleTool(9,wx.Image('guardar_proyeccion.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo de Proyeccion","")
        toolbar.AddSimpleTool(10,wx.Image('guardar_temp_perfil.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo de Perfil Temporal","")
        toolbar.AddSimpleTool(11,wx.Image('guardar_perfil.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo de Perfil","")
        toolbar.AddSimpleTool(12,wx.Image('guardar_arribos.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo de Arribos","")
        toolbar.AddSimpleTool(13,wx.Image('guardar_segy.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Guardar Archivo SEGY","")
        toolbar.AddSeparator()        
        toolbar.AddSimpleTool(14,wx.Image('calcular_image.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular Imagen","")
        toolbar.AddSimpleTool(15,wx.Image('calcular_grid.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular Grilla","")
        toolbar.AddSimpleTool(16,wx.Image('calcular_proyeccion.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular Proyeccion","")
        toolbar.AddSimpleTool(17,wx.Image('calcular_perfil_t.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular Perfil Temporal","")
        toolbar.AddSimpleTool(18,wx.Image('calcular_perfil.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular Perfil","")
        toolbar.AddSimpleTool(19,wx.Image('calcular_arribos.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular Arribos","")
        toolbar.AddSimpleTool(20,wx.Image('calcular_segy.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Calcular SEGY","")
        toolbar.AddSeparator()        
        toolbar.AddSimpleTool(21,wx.Image('zoom.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Zoom","")
        toolbar.AddSimpleTool(22,wx.Image('hand.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Pan","")
        toolbar.AddSimpleTool(23,wx.Image('datacursor.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Data Cursor","")
        toolbar.AddSimpleTool(24,wx.Image('graficargrilla.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Graficar el Grupo de Grilla","")
        toolbar.AddSimpleTool(25,wx.Image('calcular_perfil.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Uso de la data calculada","")
        toolbar.AddSimpleTool(26,wx.Image('borrargrill.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Borrar Grilla","")
        toolbar.AddSimpleTool(27,wx.Image('image.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Imagen","")
        toolbar.AddSimpleTool(27,wx.Image('calcular_segy.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), "Actualizar Grupo de Grilla","")
        toolbar.Realize()
    
        #self.Bind(wx.EVT_TOOL, self.OnNew, id=1)
        #self.figure = Figure()
        #self.axes = self.figure.add_subplot(111)    
        #self.figure = Figure()
        #self.axes = self.figure.add_subplot(111)
        #self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)
        
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menuBar.Append(menu, "&Archivo")
        
        nuevoframe = menu.Append(-1,"Archivo Nuevo\tCtrl-N")
        abririmage = menu.Append(-1,"Abrir Archivo de &Imagen\tCtrl-I")
        guardarimagen = menu.Append(-1,"Guardar Imagen\tCtrl-S")
        
        submenuproyt = wx.Menu() 
        abrirproyect = submenuproyt.Append(-1,"Abrir de Proyeccion\tCtrl-P")
        guardarproyect = submenuproyt.Append(-1,"Guardar datos de Proyeccion\tCtrl-G")      
        menu.AppendMenu(-1, "Datos de Proyeccion",submenuproyt)
        
        submenuperfil = wx.Menu()
        abrirperfil = submenuperfil.Append(-1,"Abrir de Perfil\tCtrl-shift-P")
        guardarperfil = submenuperfil.Append(-1,"Guardar datos de Perfil\tCtrl-shift-G")      
        menu.AppendMenu(-1,"Datos de Perfil",submenuperfil)
        
        submenutperfil = wx.Menu()
        abrirtperfil = submenutperfil.Append(-1,"Abrir Archivo de Perfil Temporal\tCtrl-shift-T")
        guardartperfil = submenutperfil.Append(-1,"Guardar datos de Perfil Temporal\tCtrl-shift-H")      
        menu.AppendMenu(-1,"Datos de Perfil Temporal",submenutperfil)
        
        submenuarribo = wx.Menu()
        abrirarribo = submenuarribo.Append(-1,"Abrir Archivo de Arribos\tCtrl-shift-A")
        guardararribo = submenuarribo.Append(-1,"Guardar datos de Arribos\tCtrl-shift-B")      
        menu.AppendMenu(-1,"Datos de Arribos",submenuarribo)
        
        
        directoriotrabaj = menu.Append(-1,"Seleccione el &Directorio de Trabajo\tCtrl-D")
        
        menu.AppendSeparator()
        exit = menu.Append(-1,"Cerrar\tCtrl-W")
        
        self.Bind(wx.EVT_MENU, self.OnAbrirNuevo, nuevoframe)
        self.Bind(wx.EVT_MENU, self.OnAbrirImage, abririmage)
        self.Bind(wx.EVT_MENU, self.OnAbrirProyect, abrirproyect) 
        self.Bind(wx.EVT_MENU, self.OnAbrirPerfil, abrirperfil)
        self.Bind(wx.EVT_MENU, self.OnAbrirTPerfil, abrirtperfil)
        self.Bind(wx.EVT_MENU, self.OnAbrirArribo, abrirarribo)
        self.Bind(wx.EVT_MENU, self.OnGuardarImagen, guardarimagen) 
        self.Bind(wx.EVT_MENU, self.OnGuardarProyect, guardarproyect)
        self.Bind(wx.EVT_MENU, self.OnGuardarPerfil, guardarperfil) 
        self.Bind(wx.EVT_MENU, self.OnGuardarTPerfil, guardartperfil)
        self.Bind(wx.EVT_MENU, self.OnGuardarArribo, guardararribo)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        
        #Elaboracion de menu Imagen
        menuimagen = wx.Menu()
        menuBar.Append(menuimagen, "&Imagen")
        #Submenu de Imagen
        extraerimage = menuimagen.Append(-1,"&Extraer region de la Imagen\tCtrl-E")
        imagenimagen = menuimagen.Append(-1,"Imagen\tCtrl-M")        
        zoomimagen = menuimagen.Append(-1,"&Zoom\tCtrl-Z")
        panimage = menuimagen.Append(-1,"&Pan\tCtrl-P")
        datacurseimage = menuimagen.Append(-1,"&Data Cursor\tCtrl-D")
        
        #Elaboracion de menu Grid
        menugrid = wx.Menu()
        menuBar.Append(menugrid, "&Grid")
        
        #Submenu de Grid
        submenugridfile = wx.Menu() 
        abrirgridfile = submenugridfile.Append(-1,"Abrir Grilla\tCtrl-L")
        guardargridfile = submenugridfile.Append(-1,"Guardar datos de la Grilla\tCtrl-U")      
        menugrid.AppendMenu(-1, "Datos de la Grilla",submenugridfile)
        
        submenugridinsert = wx.Menu() 
        verticalgridinsert = submenugridinsert.Append(-1,"Insertar Grilla Vertical\tCtrl-shift-V")
        horizontalgridinsert = submenugridinsert.Append(-1,"Insertar Grilla Horizontal\tCtrl-shift-H")      
        menugrid.AppendMenu(-1, "Insertar Grilla",submenugridinsert)
        
        gridborrar = menugrid.Append(-1,"&Borrar Grilla\tCtrl-B")
        gridproyect = menugrid.Append(-1,"&Proyectar Variables\tCtrl-P")
        gridcalcular = menugrid.Append(-1,"&Calcular Grilla\tCtrl-G")
        gridactualdata = menugrid.Append(-1,"&Actualizar datos\tCtrl-shift-A")
        gridzonificacion = menugrid.Append(-1,"&Zonificacion\tCtrl-shift-Z")
        
        #Elaboracion de menu Registro
        menuregistro = wx.Menu()
        menuBar.Append(menuregistro, "&Registro")
        registrotraductor = menuregistro.Append(-1,"&Traducdor Normal\tCtrl-N")
        registrofabricar1 = menuregistro.Append(-1,"&Fabricar Registro Preliminar\tCtrl-F")
        registrofabricar2 = menuregistro.Append(-1,"&Fabricar Registro Definitivo\tCtrl-R")
        registrosavesegy = menuregistro.Append(-1,"G&uardar SEGY\tCtrl-Y")
        registroreadysegy = menuregistro.Append(-1,"&Leer SEGY\tCtrl-shift-L")  
        registrorgraficarsegy = menuregistro.Append(-1,"&Graficar SEGY\tCtrl-shift-Y")
        registrormarcarllegadas = menuregistro.Append(-1,"&Marcar Llegadas\tCtrl-shift-M")
        
        #Elaboracion del menu Configuracion
        menuconfigurar = wx.Menu()        
        menuBar.Append(menuconfigurar, "&Configuracion")
        
        #Elaboracion del menu Configuracion de la bitacora
        configurarbita = menuconfigurar.Append(-1,"&Bitacora\tCtrl-shift-B")
        
        self.Bind(wx.EVT_MENU, self.OnAbrirBitacora, configurarbita)
        
        menuregistro = wx.Menu()
        
        menuBar.Append(menuregistro, "&Ayuda")
        
        self.SetMenuBar(menuBar)
        
    def OnSplitH(self, evt):
        sp.SplitHorizontally(p, p2,self.initpos)

    def OnSplitV(self, evt):
        sp.SplitVertically(p, p2,self.initpos)
        
    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()
    
    def OnMouseDown(self, event):
        self.button.SetLabel('Again')        
        event.Skip()
        
    def OnGuardarImagen(self,event):
        wx.MessageBox("Falta 2")
        #x = np.arange(0, 6, .01) 
        #y = np.sin(x**2)*np.exp(-x)
        #self.axes.plot(x, y)
        # initialize the FigureCanvas, mapping the figure to
        # the Wx backend
        #self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)
        
    def OnAbrirNuevo(self, event):
        
##        win = wx.MDIChildFrame(self, -1, "Hijo",style = -1)
        
        win.figure = Figure()
        win.axes = win.figure.add_subplot(111)
        win.canvas = FigureCanvas(win, wx.ID_ANY, win.figure)
        win.sizer = wx.BoxSizer(wx.VERTICAL)
        win.sizer.Add(win.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        win.toolbar = NavigationToolbar2Wx(win.canvas)
        win.toolbar.Realize()
        win.sizer.Add(win.toolbar, 0, wx.LEFT | wx.EXPAND)
        win.toolbar.Show()
        win.SetSizer(win.sizer)
        win.Fit()
        win.Show(True)
##        return win
        
        
    def OnAbrirImage1(self,event):
        wildcard = "JPG (*.jpg)|*.jpg|" "PNG (*.png)|*.png|" "GIF (*.gif)|*.gif|" 
        dialog = imagebrowser.ImageDialog(None)
        
        if dialog.ShowModal() == wx.ID_OK:
##            wx.MessageBox(dialog.GetFile())GetPath()
##            wx.MessageDialog(dialog)
            #------------------------------------------------------------------
            #El siguiente codigo funciona    
            #------------------------------------------------------------------
##            f = np.arange(0, 6, .01)
##            y = np.sin(x**4)*np.exp(-x)
##            self.axes.plot(x,y)
##            self.canvas = FigureCanvas(self.p2, wx.ID_ANY, self.figure)
            #------------------------------------------------------------------
            
            #img = wx.Image(name,wx.BITMAP_TYPE_ANY)    
            #x = np.arange(0, 6, .01)
            #y = np.sin(x**2)*np.exp(-x)
            #ellipses = x*x/9 + y*y/4 -1
            #plt.imshow(ellipses)
            
            #plt.imshow(ellipses)
##            f = plt.imread(dialog.GetFile())

            f = plt.imread('/home/falvarez/matwork/E61EXT_MIG.jpg')
            win.axes.imshow(f,cmap=cm.gray)
            
##            win.axes.imshow(f)
            #contour(self.canvas, origin='lower', extent=[-1,1,-1,1])
            #xlabel('x')
            #ylabel('y')
            #title('A spiral !')
            #BW = im2bw(f, graythresh(f))
##            win.canvas = FigureCanvas(f, wx.ID_ANY, win.figure)
            
            #plt.imshow(self.figure)
            #wx.MessageBox(dialog.GetFile())
            #f = plt.imread('/home/falvarez/matwork/E61EXT_MIG.jpg')
            #plt.imshow(f)
            #im = Image.open(dialog,self.p1)
            #im.show(self.p1)
            
            #im = Image.open(dialog)
            
            #im.show()
            
    def OnAbrirImage1(self,event):
        p = wx.Panel(self)
        wildcard = "JPG (*.jpg)|*.jpg|" "PNG (*.png)|*.png|" "GIF (*.gif)|*.gif|"    
        dialog = wx.FileDialog(None,"Elige una imagen", os.getcwd(),"",wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            wx.MessageBox(dialog.GetPath())
            fgs = wx.FlexGridSizer(rows=1,cols=0,vgap=0,hgap=0)
            img = wx.Image(dialog.GetPath(),wx.BITMAP_TYPE_ANY)
            img = img.Scale(1000,600)
            sb= wx.StaticBitmap(p,-1,wx.BitmapFromImage(img))
            fgs.Add(sb)
            p.SetSizerAndFit(fgs) 
            self.Fit()   
            
            f = plt.imread('/home/falvarez/matwork/E61EXT_MIG.jpg')
            win.axes.imshow(f,cmap=cm.gray)
            
    def OnAbrirImage(self,event):
##        p = wx.Panel(self)
        wildcard = "JPG (*.jpg)|*.jpg|" "PNG (*.png)|*.png|" "GIF (*.gif)|*.gif|"    
        dialog = wx.FileDialog(None,"Elige una imagen", os.getcwd(),"",wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
##            wx.MessageBox(dialog.GetPath())
            f = plt.imread(dialog.GetPath())            
            win.axes.imshow(f,cmap=cm.gray)
            win.axes.grid(True)
##            plt.plot([100,200,300],[200,150,200],'o') drawnow
##            plt.show()
##            fgs = wx.FlexGridSizer(rows=1,cols=0,vgap=0,hgap=0)
##            img = wx.Image(dialog.GetPath(),wx.BITMAP_TYPE_ANY)
##            img = img.Scale(1000,600)
##            sb= wx.StaticBitmap(p,-1,wx.BitmapFromImage(img))
##            fgs.Add(sb)
##            p.SetSizerAndFit(fgs) 
##            self.Fit()   
    def OnGuardarImagen(self,event):
        wx.MessageBox("Falta")
        
    def OnAbrirProyect(self,event):
        wx.MessageBox("Falta Abrir datos de Proyeccion")
        
    def OnAbrirPerfil(self,event):
        wx.MessageBox("Falta Abrir datos de Perfil")
        
    def OnAbrirTPerfil(self,event):
        wx.MessageBox("Falta Abrir datos de Perfil Temporal")
        
    def OnAbrirArribo(self,event):
        wx.MessageBox("Falta Abrir datos de Arribo")
        
##    def OnGuardarImagen(self,event):
##        wx.MessageBox("Falta Imagen")
        
    def OnGuardarPerfil(self,event):
        wx.MessageBox("Falta Guardar datos de Perfil")

    def OnGuardarTPerfil(self,event):
        wx.MessageBox("Falta Guardar datos de Perfil Temporal")
        
    def OnGuardarProyect(self,event):
        wx.MessageBox("Falta Guardar datos de Proyeccion")
    
    def OnGuardarArribo(self,event):
        wx.MessageBox("Falta Guardar datos de Arribo")
        
    def OnExit(self, event):
        self.Close()
        
    def OnExitWindow(self, event):
        try:
            win_bita.Hide()
            bto_guardar.Enable(True)
        except:
            print "fallo el ocultar"
                
    def Onfile(self,event):
        try:  
            arch.Modificar(txt_bitapatch.Value,txt_bita.Value,Lta_mode.GetString(Lta_mode.GetSelection()),os.environ['USERNAME'])
            a = arch.Abrir()
##            print arch.rutaGuardado
            
            #llamar a configurar_bitacora 
            bita.ConfigurarBitacora(a[0],a[1],a[2],a[3])
        
##            print bita.modo + bita.rutaGuardado + bita.nombredearchivobitacora + bita.usuario

##            print bita.nombredearchivobitacora
            bto_guardar.Enable(False)
            
            
        except IOError:
            print "Error, al modificar el archivo de configuración."
            
        
    def OnDirectorio(self,event):
        dialog = wx.DirDialog(None,"Elige otro directorio:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetPath
        dialog.Destroy()

    
    #Metodo que abre un frame para configurar bitacora
    ##      bitatxt.SetInsertionPoint(0)
    ##        win_bita      = wx.MDIChildFrame(self, -1, "Configurar Bitacora")
    ##        self.Bind(wx.EVT_BUTTON,self.OnExit,bto_guardar)            

    def OnAbrirBitacora(self,evt):

        try:
 
            #El siguiente codigo da error
            print win_bita.txt_bita
            
##            print Lta_mode.GetSelection()
##            print Lta_mode.GetString(Lta_mode.GetSelection())
            win_bita.Show(True)
            
##        except (NameError, ValueError):
        except:
                        
            bita.construirmensaje('DEBUG','KeyError')
            print "Error"
            print sys.stderr.readline
            print sys.exc_info()[0]
            
            
##        else:
##            print "Sigue..."
        


if __name__=='__main__':
    
    app = wx.PySimpleApp()
    frame = MDIFrame()
    frame.SetSize((1200,700))
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()
    
