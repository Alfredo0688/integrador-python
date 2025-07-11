import tkinter as tk
from tkinter import ttk , messagebox
import modelo.consultas_dao_paseo as consulta

class Frame(tk.Frame):  
    def __init__(self, root = None):    
        super().__init__(root,width=480,height=320)    
        self.root = root    
        self.pack()
        self.id_paseo_gatos = None
        self.fondo = "#FBFCDD"   
        self.config(bg = self.fondo) # se pueden usar clores hexa o el nombre

        #self.label_form()
        self.label_form(0,'Elija un paseo: ',0)
        self.label_form(1,'Elija un gato : ',0)
        self.label_form(1,'Hora del paseo: ',2)
        self.label_form(2,'¿Está pagado?: ',0)
        self.label_form(3,'Observaciones sobre el gato: ',0)
        self.input_form()
        self.botones_principales()
        #self.mostrar_tabla()

    def label_form(self,fila,texto,columna):    
        
        self.label_nombre = tk.Label(self, text=texto)
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")
        self.label_nombre.grid(row= fila, column=columna,padx=10,pady=10)

    def input_form(self):   
        
        x = consulta.listar_paseos_cbb() 
        y = []
        for i in x:
            y.append(i[1]) #el 1 es por la segunda posición de la tabla que es el campo fecha

        self.paseos = ['Selecione Uno'] + y
        self.entry_paseos = ttk.Combobox(self, state="readonly")    
        self.entry_paseos.config(width=25, state='disabled')
        self.entry_paseos['values'] = self.paseos
        self.entry_paseos.current(0)  
        self.entry_paseos.bind("<<ComboboxSelected>>")    
        self.entry_paseos.grid(row= 0, column=1,padx=10,pady=10)
     


        z = consulta.listar_michis()
        o = []
        for i in z:
            o.append(i[2]) #el dos es por la tercera posición de la tabla que es el campo nombre

        self.michi = ['Selecione Uno'] + o
        self.entry_michi = ttk.Combobox(self, state="readonly")    
        self.entry_michi.config(width=25, state='disabled')
        self.entry_michi['values'] = self.michi
        self.entry_michi.current(0)  
        self.entry_michi.bind("<<ComboboxSelected>>")    
        self.entry_michi.grid(row= 1, column=1,padx=10,pady=10)
        

        self.hora = tk.StringVar()
        self.entry_hora = tk.Entry(self, textvariable=self.hora)    
        self.entry_hora.config(width=10, state='disabled')    
        self.entry_hora.grid(row= 1, column=3,padx=10,pady=10) 

        self.pagado = tk.StringVar()
        self.entry_pagado = tk.Entry(self, textvariable=self.pagado)
        self.entry_pagado.config(width=10,state='disabled')
        self.entry_pagado.grid(row=2,column=1,padx=10,pady=10)
        
        self.observaciones = tk.StringVar()
        self.entry_observaciones = tk.Entry(self, textvariable=self.observaciones)
        self.entry_observaciones.config(width=50,state='disabled')
        self.entry_observaciones.grid(row=3,column=1,padx=10,pady=10)


        
     
    def botones_principales(self):    
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)    
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_alta.grid(row= 6, column=0,padx=10,pady=10)   

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)    
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000', state='disabled')    
        self.btn_modi.grid(row= 6, column=1,padx=10,pady=10) 

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)    
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000', state='disabled')    
        self.btn_cance.grid(row= 6, column=2,padx=10,pady=10)
    
    def mostrar_tabla(self):

        self.lista_p = consulta.listar_paseos()

        self.lista_p.reverse()

        self.tabla = ttk.Treeview(self, columns=('Fecha del paseo','Hora del paseo','Valor del paseo', 'Nombre del gato', 'Paseador', 'Observaciones', 'Pagado'))
        self.tabla.grid(row=7, column=0, columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=4,column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Fecha del paseo')
        self.tabla.heading('#2', text='Hora del paseo')
        self.tabla.heading('#3', text='Valor del paseo')
        self.tabla.heading('#4', text='Nombre del gato')
        self.tabla.heading('#5', text='Paseador')
        self.tabla.heading('#6', text='Observaciones')
        self.tabla.heading('#6', text='Pagado')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7]))

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)    
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_editar.grid(row= 8, column=0,padx=10,pady=10)    
        
        self.btn_delete = tk.Button(self, text='Delete', command= self.eliminar_regristro)    
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_delete.grid(row= 8, column=1,padx=10,pady=10)

    def editar_registro(self):
        try:
            self.id_paseo_gatos = self.tabla.item(self.tabla.selection())['text']

            #self.nombre_peli = self.tabla.item(self.tabla.selection())['values'][0]
            #self.dura_peli = self.tabla.item(self.tabla.selection())['values'][1]
            #self.gene_peli = self.tabla.item(self.tabla.selection())['values'][2]

            #Declaramos variables que almacenan los campos del registro de la tabla
            self.fecha_paseo = self.tabla.item(self.tabla.selection())['values'][0]
            self.hora_paseo = self.tabla.item(self.tabla.selection())['values'][1]
            self.paseo_pagado = self.tabla.item(self.tabla.selection())['values'][6]
            self.nombre_gato = self.tabla.item(self.tabla.selection())['values'][3]
            self.observaciones_campo = self.tabla.item(self.tabla.selection())['values'][5]


            #setea los campos en las cajas de texto
            self.habilitar_campos()
            #self.fecha.set(self.nombre_peli)
            self.entry_paseos.current(self.paseos.index(self.fecha_paseo))
            self.entry_michi.current(self.michi.index(self.nombre_gato))
            self.hora.set(self.hora_paseo)
            self.pagado.set(self.paseo_pagado)
            self.observaciones.set(self.observaciones_campo)

            #self.entry_michi.current(self.michi.index(self.gene_peli))
        except:
            pass  
    
    def eliminar_regristro(self):
        self.id_paseo_gatos = self.tabla.item(self.tabla.selection())['text']

        response = messagebox.askyesno("Confirmar","Desea borrar el registro ?")
        
        if response:    
            consulta.borrar_gatos_paseos(int(self.id_paseo_gatos))
        else:
            messagebox.showinfo("MIRA BIEN", "CASI BORRAS ALGO EQUIVOCADO")
        
        self.id_peli = None
        self.mostrar_tabla()

    

    def guardar_campos(self):
        paseo_gatos = consulta.PaseoGatos(
            self.entry_michi.current(), #aqui debe ser el de michi
            self.entry_paseos.current(),
            self.hora.get(),
            self.observaciones.get(),
            self.pagado.get() 
        )
#ver aquí que tome el id de la clase paseo gatos
        if self.id_paseo_gatos == None:
            consulta.guardar_paseo_gato(paseo_gatos)
            #print(f"paseo : {paseo_gatos.id_paseo} , hora del paseo del gato : {paseo_gatos.hora_paseo} , pagado {paseo_gatos.pagado}, observaciones : {paseo_gatos.observaciones} , michi : {paseo_gatos.id_gato}")
        else:
            print("Entró en edición")
            consulta.editar_gatos_paseos(paseo_gatos,int(self.id_paseo_gatos))
        
        self.mostrar_tabla()
        self.limpiar_campos()
        #self.bloquear_campos()
        


    def habilitar_campos(self):    
        self.entry_paseos.config(state='normal')    
        self.entry_hora.config(state='normal')    
        self.entry_pagado.config(state='normal')
        self.entry_observaciones.config(state='normal')
        self.entry_michi.config(state='normal')   
        self.btn_modi.config(state='normal')    
        self.btn_cance.config(state='normal')    
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):    
        self.entry_paseos.config(state='disabled')
        self.entry_hora.config(state='disabled')    
        self.entry_pagado.config(state='disabled')
        self.entry_observaciones.config(state='disabled')
        self.entry_michi.config(state='disabled')    
        self.btn_modi.config(state='disabled')    
        self.btn_cance.config(state='disabled')    
        self.btn_alta.config(state='normal')
        self.fecha.set('')
        self.hora.set('')
        self.entry_michi.current(0)
        self.id_peli = None

    
    def limpiar_campos(self):    
        self.entry_michi.current(0)
        self.entry_paseos.current(0)
        self.hora.set('')
        self.pagado.set('')
        self.observaciones.set('')
        self.id_peli = None
