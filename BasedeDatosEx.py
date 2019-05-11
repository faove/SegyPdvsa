#!/usr/bin/python

import wx
import MySQLdb, _mysql, _mysql_exceptions


class BD():
    def __init__(self):
        pass
    
    
##    , host, user, password, db):
##        self.dbc=MySQLdb.connect(host, user, password, db)
##        self.cursor=self.dbc.cursor()

    def Conexion(self, host, user, password, db):
        self.dbc=MySQLdb.connect(host, user, password, db)
        self.cursor=self.dbc.cursor()
        print 'usted esta conectado'
        

    def Select(self, tabla, columna, valor):
        sql= "SELECT * FROM " + tabla + " WHERE " + columna + "=" + valor
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        return resultado

    def Insert(self, tabla, columna1, columna2, columna3, valor1, valor2, valor3):
        sql="INSERT INTO" + tabla + "(" + columna1 + "," + columna2 + "," + columna3 + ")" + "VALUES" + "(" + valor1 + "," + valor2 + "," + valor3 + ")" 


class Dialogo(wx.Dialog, BD):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(800,600), style=wx.DEFAULT_DIALOG_STYLE)
        
        hbox  = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(2,2,0,0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.lc.InsertColumn(0, 'Busqueda')

        self.lc.SetColumnWidth(0, 1024)
        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 3)
        self.Host = wx.TextCtrl(pnl1, -1)
        self.Usuario = wx.TextCtrl(pnl1, -1)
        self.Clave = wx.TextCtrl(pnl1, -1)
        self.BaseDatos= wx.TextCtrl(pnl1, -1)
        self.Tabla = wx.TextCtrl(pnl1, -1)
        self.Columna = wx.TextCtrl(pnl1, -1)
        self.Valor = wx.TextCtrl(pnl1, -1)

        vbox3.AddMany([ (wx.StaticText(pnl1, -1, 'Host'),0, wx.ALIGN_CENTER),
                        (self.Host, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Usuario'),0, wx.ALIGN_CENTER),
                        (self.Usuario,0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Clave'),0, wx.ALIGN_CENTER),
                        (self.Clave, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Base de Datos'),0, wx.ALIGN_CENTER),
                        (self.BaseDatos, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Tabla'),0, wx.ALIGN_CENTER),
                        (self.Tabla, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Columna'),0, wx.ALIGN_CENTER),
                        (self.Columna, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Valor'),0, wx.ALIGN_CENTER),
                        (self.Valor, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        ])
        pnl1.SetSizer(vbox3)
        vbox4.Add(wx.Button(pnl2, 10, 'Buscar'),   0, wx.ALIGN_CENTER| wx.TOP, 45)
        vbox4.Add(wx.Button(pnl2, 11, 'Remover'), 0, wx.ALIGN_CENTER|wx.TOP, 15)
        vbox4.Add(wx.Button(pnl2, 12, 'Limpiar'), 0, wx.ALIGN_CENTER| wx.TOP, 15)
        vbox4.Add(wx.Button(pnl2, 13, 'Cerrar'), 0, wx.ALIGN_CENTER| wx.TOP, 15)
        pnl2.SetSizer(vbox4)

        self.Bind (wx.EVT_BUTTON, self.Buscar, id=10)
        self.Bind (wx.EVT_BUTTON, self.OnRemove, id=11)
        self.Bind (wx.EVT_BUTTON, self.OnClear, id=12)
        self.Bind (wx.EVT_BUTTON, self.OnClose, id=13)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        self.SetSizer(hbox)

    def Buscar(self, event):
        if not self.Host.GetValue() or not self.Usuario.GetValue() or not self.Clave.GetValue() or not self.BaseDatos.GetValue() or not self.Tabla.GetValue() or not self.Columna.GetValue() or not self.Valor.GetValue() :
            return
        host= self.Host.GetValue()
        user= self.Usuario.GetValue()
        password= self.Clave.GetValue()
        db= self.BaseDatos.GetValue()
        b=BD()
        b.Conexion( host, user, password, db)
        num_items = self.lc.GetItemCount()
        tabla=self.Tabla.GetValue()
        columna=self.Columna.GetValue()
        valor=self.Valor.GetValue()
        resultado=b.Select( tabla, columna, valor)
        for registro in resultado:
            r=registro
            self.lc.InsertStringItem(num_items, str(r) )
        self.Host.Clear()
        self.Usuario.Clear()
        self.Clave.Clear()
        self.BaseDatos.Clear()
        self.Tabla.Clear()
        self.Columna.Clear()
        self.Valor.Clear()

    def OnClose(self, event):
        self.Close()

    def OnClear(self, event):
        self.Host.Clear()
        self.Usuario.Clear()
        self.Clave.Clear()
        self.BaseDatos.Clear()
        self.Tabla.Clear()
        self.Columna.Clear()
        self.Valor.Clear()

    def OnRemove(self, event):
        index = self.lc.GetFocusedItem()
        self.lc.DeleteItem(index)

class MyApp(wx.App):
    def OnInit(self):
        a=Dialogo(None, -1, 'Parametros.py')
        a.ShowModal()
        a.Destroy()
        return True

app = MyApp(0)
app.MainLoop()