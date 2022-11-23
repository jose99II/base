# Personalizacion de Intarfaz Grafica
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import  Tk, x, Label, ttk, PhotoImage
from tkinter import  Frame, Toplevel

class Aplicacion(Frame):
	def __init__(self, master, *args):
		super().__init__(master,*args)
		self.x = 0
		self.y = 0
		self.x0 = 50
		self.y0 = 50
		self.x1 = 100
		self.y1 = 100
		self.click  = True

		self.ventana = Toplevel(self.master)
		self.ventana.overrideredirect(1)
		self.ventana.minsize(width=300, height=200)
		self.ventana.geometry('800x500+300+90')

		#FRAME BARRA DE TITULO
		self.frame_top = Frame(self.ventana, bg='DarkOrchid1', height=60) #width=50, 
		self.frame_top.grid_propagate(0)
		self.frame_top.grid(column=0, row = 0, sticky='nsew')

		#FRAME DEL CONTENIDO
		self.frame_principal = Frame(self.ventana, bg='black')  #brown2
		self.frame_principal.grid(column=0, row=1, sticky='nsew')

		self.ventana.columnconfigure(0, weight=1)
		self.ventana.rowconfigure(1, weight=1)

		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.columnconfigure(1, weight=1)		
		self.frame_principal.columnconfigure(2, weight=1)		
		self.frame_principal.rowconfigure(0, weight=1)
		self.frame_principal.rowconfigure(1, weight=1)

		self.frame_top.bind("<ButtonPress-1>", self.start)                                                                           
		self.frame_top.bind("<B1-Motion>", self.mover) 
		self.master.bind("<Map>", self.on_deiconify)
		self.master.bind("<Unmap>", self.on_iconify)

		self.grip = ttk.Sizegrip(self.frame_principal, style = "TSizegrip")
		self.grip.place(relx=1.0, rely=1.0, anchor="se")
		self.grip.bind("<B1-Motion>", self.redimencionar)
		ttk.Style().configure("TSizegrip", background='black')

		self.widgets()

	def redimencionar(self, event):
		self.x1 = self.ventana.winfo_pointerx()
		self.y1 = self.ventana.winfo_pointery()
		self.x0 = self.ventana.winfo_rootx()
		self.y0 = self.ventana.winfo_rooty()
		print(self.x0, self.y0, self.x1, self.y1)
		try:
			self.ventana.geometry("%sx%s" % ((self.x1-self.x0),(self.y1-self.y0)))
		except:
			pass

	def salir(self):
		self.ventana.destroy()
		self.ventana.quit()

	def start(self, event):
	    self.x = event.x
	    self.y = event.y

	def mover(self, event):
	    deltax = event.x - self.x
	    deltay = event.y - self.y
	    if self.ventana.winfo_y()>0:
		    self.ventana.geometry("+%s+%s" % (self.ventana.winfo_x() + 
		        deltax, self.ventana.winfo_y() + deltay))
		    self.ventana.update()
	    elif self.ventana.winfo_y()<= 1:
		    self.ventana.geometry("+%s+%s" % (self.ventana.winfo_x() + 
		        deltax, self.ventana.winfo_y() + deltay))
		    self.ventana.update()
		    self.pantalla_completa()
		    self.cambiar_tamaño.config(image = self.imagen_ecogimiento)
		    self.click = False
		    if self.ventana.winfo_y()<=50 and self.ventana.winfo_y()>0:
		    	self.click = True
		    	self.cambiar_tamaño.config(image = self.imagen_maximizar)
		    	self.ventana.geometry("%sx%s+%s+%s" % ((self.x1-self.x0),(self.y1-self.y0), self.x0, self.y0))
		    	self.ventana.geometry("+%s+%s" % (self.ventana.winfo_x() + 
			        deltax, self.ventana.winfo_y() + deltay))
		    	self.ventana.update()

	def pantalla_completa(self):
		self.ventana.geometry("{0}x{1}+0+0".format(self.ventana.winfo_screenwidth(), 
			self.ventana.winfo_screenheight()-30))   #ventana.attributes("-zoomed", True) ventana.attributes('-fullscreen', True) 

	def cambiar_dimencion(self):
		if self.click == True :
			self.cambiar_tamaño.config(image = self.imagen_ecogimiento)
			self.pantalla_completa()
			self.click = False
		else:
			self.cambiar_tamaño.config(image = self.imagen_maximizar)			
			self.ventana.geometry("%sx%s+%s+%s" % ((self.x1-self.x0),(self.y1-self.y0), self.x0 ,self.y0))
			self.click = True

	def on_deiconify(self, event):
		self.ventana.deiconify()
		self.master.lower()

	def on_iconify(self, event):
		self.ventana.withdraw()
		self.master.iconify()
	

	def widgets(self):
		self.imagen_cerrar = PhotoImage(file ='imagenes/cerrar.png')
		self.imagen_maximizar = PhotoImage(file ='imagenes/maximizar.png')
		self.imagen_minimizar = PhotoImage(file ='imagenes/minimizar.png')
		self.imagen_ecogimiento = PhotoImage(file ='imagenes/encogimiento.png')

		self.cerrar = Button(self.frame_top, image = self.imagen_cerrar, bg='DarkOrchid1',
			activebackground='DarkOrchid1', bd=0, command= self.salir)
		self.cerrar.pack(ipadx=5, padx=5, side='right', ipady = 2) 
		self.cambiar_tamaño = Button(self.frame_top, image = self.imagen_maximizar , bg='DarkOrchid1',
			activebackground='DarkOrchid1', bd=0, command= self.cambiar_dimencion)
		self.cambiar_tamaño.pack(ipadx=5, padx=5, side='right')		
		self.minimizar = Button(self.frame_top,  image = self.imagen_minimizar , bg='DarkOrchid1',
			activebackground='DarkOrchid1', bd=0, command= lambda : self.master.iconify())
		self.minimizar.pack(ipadx=5, padx=5, side='right') 

		self.titulo = Label(self.frame_top, text= 'Menu Aplicacion de Escritorio', bg='DarkOrchid1', fg= 'black', 
			font= ('Arial', 12, 'bold'))
		self.titulo.pack(padx=10, side = 'left')
		self.titulo.bind("<B1-Motion>", self.mover)
		self.titulo.bind("<ButtonPress-1>", self.start)

		frame_uno = Frame(self.frame_principal, bg= 'spring green', width=100, height=200, highlightbackground="gray25",highlightthickness=2)
		frame_uno.grid(padx=10, pady = 10, columnspan=2, row=0, sticky='nsew')
		frame_dos = Frame(self.frame_principal, bg= 'spring green', width=100, height=200, highlightbackground="gray25",highlightthickness=2)
		frame_dos.grid(padx=10, pady = 10, column=2, row=0, sticky='nsew')
		frame_tres = Frame(self.frame_principal, bg= 'magenta2', width=100, height=200, highlightbackground="gray25",highlightthickness=2)
		frame_tres.grid(padx=10, pady = 10, column=0, row=1, sticky='nsew')
		frame_cuatro = Frame(self.frame_principal, bg= 'gold', width=100, height=200, highlightbackground="gray25",highlightthickness=2)
		frame_cuatro.grid(padx=10, pady = 10, column=1, row=1, sticky='nsew')
		frame_cinco = Frame(self.frame_principal, bg= 'tomato', width=100, height=200, highlightbackground="gray25",highlightthickness=2)
		frame_cinco.grid(padx=10, pady = 10, column=2, row=1, sticky='nsew')

		Label(frame_uno, text= 'PYTHON \n  ', bg='spring green', fg= 'black', 
			font= ('Tarrget 3D', 50, 'bold')).pack(pady=5, expand= True) #SolsticeOfSuffering
		Button(frame_dos, text= 'Button 1', bg='gold',fg = 'black',font =('Tahoma',12)).pack(pady=10)
		Button(frame_dos, text= 'Button 2', bg='magenta2',fg = 'black',font =('Tahoma',12)).pack(pady=10)
		Button(frame_dos, text= 'Button 3', bg='tomato',fg = 'black',font =('Tahoma',12)).pack(pady=10)
		Label(frame_tres, text= 'Python', bg='magenta2', fg= 'black', 
			font= ('ayuenda shadow', 30, 'bold')).pack(pady=5) 
		Label(frame_cuatro, text= 'Python', bg='gold', fg= 'black', 
			font= ('Kaufmann BT', 30, 'bold')).pack(pady=5)
		Label(frame_cinco, text= 'Python', bg='tomato', fg= 'black', 
			font= ('Magnum', 30, 'bold')).pack(pady=5)		

if __name__ == "__main__":
	root = Tk()
	root.title('Aplicacion Moderna')
	root.call('wm', 'iconphoto', root._w, PhotoImage(file='logo.png'))
	root.attributes('-alpha' , 0.0) 
	root.config(bg = 'DarkOrchid1')
	app = Aplicacion(root)
	app.mainloop()






























