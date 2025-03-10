import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejandro Daniel
apellido: López Pino
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        lampara = 800
        cantidad = self.combobox_cantidad.get()
        marca = self.combobox_marca.get()
        cantidad_numero = int(cantidad)        
        
        if cantidad_numero > 5: #A
            descuento = 50

        elif cantidad_numero == 5: #B
            if marca == 'ArgentinaLuz':
               descuento = 40
            else:
                descuento = 30

        elif cantidad_numero == 4: #C
            if marca == 'ArgentinaLuz' or marca == 'FelipeLamparas':
                descuento = 25
            else:
                descuento = 20

        elif cantidad_numero == 3: #D
            if marca == 'ArgentinaLuz':
                descuento = 15
            elif marca == 'FelipeLamparas':
                descuento = 10
            else:
                descuento = 5

        precio = lampara * cantidad_numero
        precio_y_descuento = precio * (descuento / 100)
        precio_con_descuento_aplicado = precio - precio_y_descuento
        precio_y_descuento_extra = 0
        
        if precio_con_descuento_aplicado > 4000:
                precio_y_descuento_extra = precio_con_descuento_aplicado * (5 / 100)
        
        total = precio_con_descuento_aplicado - precio_y_descuento_extra
        



        mensaje = f"Se compraron en total {cantidad} de lamparitas marca {marca}, por ende, se aplica un descuento del {descuento}%, dando un total de {total}, "
        alert('', mensaje)

if __name__ == "__main__":
    app = App()                  
    app.geometry("300x300")
    app.mainloop()