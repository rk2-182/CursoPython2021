from tkinter import *
from tkinter import ttk

# Modulo bd
import sqlite3


class Product:
    # Archivo BD
    db_name = 'database.db'

    # Constructor Objeto
    def __init__(self, titulo, tamaño):
        self.titulo = titulo
        self.tamaño = tamaño

    # *****************Interfaz grafica******************
    def cargarVentana(self):
        ventana = Tk()
        # crear una propiedad ventana
        self.ventana = ventana
        self.ventana.config(bg="#D9D8DA")

        ventana.title(self.titulo)
        ventana.geometry(self.tamaño)

        marco = LabelFrame(self.ventana, width=460,
                           height=500, text="Registrar Un Producto")
        self.marco = marco
        marco.config(bg="#EAEAEA", relief=SOLID, bd=1,
                     font=("consolas", 13), fg='Blue')
        marco.grid(row=0, column=0, columnspan=3, padx=20)

        # Name input
        nombreL = Label(marco, text='Nombre: ')
        nombreL.config(font=('Consolas', 10))
        nombreL.grid(row=1, column=0)
        self.nombre = Entry(marco)
        self.nombre.focus()  # dejar marcado
        self.nombre.grid(row=1, column=1, padx=10)

        # Precio input
        precioL = Label(marco, text='Precio: ')
        precioL.config(font=('Consolas', 10))
        precioL.grid(row=2, column=0)
        self.precio = Entry(marco)
        self.precio.grid(row=2, column=1, padx=10)

        # **********Button add price*********
        self.guardar = Button(
            marco, text="Guardar Producto", command=self.addProduct)
        self.guardar.config(font=('Consolas', 10))
        self.guardar.grid(row=3, columnspan=2, sticky=W+E)

         # table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)

        # Botones debajo de la tabla
        # Boton eliminar
        self.eliminar = Button(text="Eliminar", command=self.deleteProduct)
        self.eliminar.config(font=('Consolas', 10))
        self.eliminar.grid(row=5, column=0, sticky=W+E)

        # Boton editar
        self.editar = Button(text="Editar", command=self.editProduct)
        self.editar.config(font=('Consolas', 10))
        self.editar.grid(row=5, column=1, sticky=W+E)

        self.get_products()

        # Mostrar mensaje
        self.message = Label(text='', fg='#FF5959')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)
    # ********************************Fin intefaz grafica*****************************

    def EjecutarVentana(self):
        self.ventana.mainloop()

    # ***************BD**********************
    def runquery(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # **************Metodos CRUD******************
    # Mostrar
    def get_products(self):
        records = self.tree.get_children()  # obtener todos los datos dentro de la  tabla
        # limpiar tabla
        for element in records:
            self.tree.delete(element)

        # Consultar
        query = "SELECT * FROM product ORDER BY name DESC"
        db_rows = self.runquery(query)
        # print(db_rows)
        for row in db_rows:
            # print(row)
            # rellenar los datos en la tabla
            self.tree.insert('', 0, text=row[1], values=row[2])

    # insertar
    def addProduct(self):
        # print(self.nombre.get())
        # print(self.precio.get())
        query = 'INSERT INTO product VALUES (NULL,?,?)'
        parameters = self.nombre.get(), self.precio.get()
        if len(self.nombre.get()) != 0 and len(self.precio.get()) != 0:
            self.runquery(query, parameters)
            self.message['text'] = 'Producto {} agregado correctamente!'.format(
                self.nombre.get())
            # limpiar inputs
            self.nombre.delete(0, END)
            self.precio.delete(0, END)
        else:
            self.message['text'] = 'Nombre y Precio requeridos'

        self.get_products()  # mostrar cambios

    # Eliminar producto
    def deleteProduct(self):
        try:
            # ver si un producto esta seleccionado
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Selecciona un producto'
            return
        name = self.tree.item(self.tree.selection())['text']
        query = ' DELETE FROM product WHERE name = ?'
        self.runquery(query, (name,))
        self.message['text'] = 'Producto: {} a sido eliminado'.format(name)

        self.get_products()  # Mostrar cambios

    # Actualizar producto
    def editProduct(self):
        try:
            # ver si un producto esta seleccionado
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Selecciona un producto'
            return
        
        #obtener valores
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]

       
        #Abrir una nueva ventana con toplevel
        self.edit_wind=Toplevel()
        self.edit_wind.title('Editar')

        #Obtener valores anteriores y mostraron en nueva ventana

        #Antiguo nombre
        Label(self.edit_wind, text="Nombre anterior: ").grid(row=0,column=1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row=0,column=2)
        #Nuevo nombre
        Label(self.edit_wind, text="Nombre nuevo: ").grid(row=1,column=1)
        nuevo_nombre = Entry(self.edit_wind)
        nuevo_nombre.grid(row=1,column=2)

        #Antiguo Valor
        Label(self.edit_wind, text="Precio anterior: ").grid(row=2,column=1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row=2,column=2)

        #Nuevo valor
        Label(self.edit_wind, text="Precio nuevo: ").grid(row=3,column=1)
        nuevo_precio = Entry(self.edit_wind)
        nuevo_precio.grid(row=3,column=2)

        Button(self.edit_wind, text='Actualizar', command= lambda: self.edit_records(nuevo_nombre.get(),name,nuevo_precio.get(), old_price )).grid(row=4, column=2, sticky= W)

  
    def edit_records(self, nuevo_nombre, nombre, nuevo_precio, antigo_precio):

        query = 'UPDATE product SET name =?, price =? WHERE name = ? AND price = ?'
        parameters = (nuevo_nombre, nuevo_precio, nombre, antigo_precio)

        self.runquery(query, parameters)
        self.edit_wind.destroy() #destruir ventana
        self.message['text'] ='El producto a sido agregado correctamente!'
        self.get_products() #Mostrar cambios


# >>>>>>>>>>>>Bloque principal<<<<<<<<<<<<<<<<
producto = Product("Productos","400x380")

producto.cargarVentana()
producto.get_products()
producto.EjecutarVentana()
