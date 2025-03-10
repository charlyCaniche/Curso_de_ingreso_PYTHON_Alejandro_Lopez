import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejandro Daniel
apellido: López Pino
---
Ejercicio: listas_05
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad - Validar (Entre 15 y 90 años).
    Genero - Validar (Femenino/Masculino/No Binario).
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los masculinos.
    B. Porcentaje de femeninos mayores de 18 respecto al total de personas.
    C. Porcentaje de personas de cada genero.
    D. Informar edad y genero de la persona con menor edad, puede ser mas de una.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label = customtkinter.CTkLabel(master=self, text="Edad")
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Genero")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_genero = customtkinter.CTkEntry(master=self)
        self.txt_genero.grid(row=1, column=1)

        self.btn_ingresar = customtkinter.CTkButton(master=self, text="INGRESAR", command=self.btn_ingresar_on_click)
        self.btn_ingresar.grid(row=2, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(master=self, text="INFORMAR", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=3, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.lista_edades = []
        self.lista_generos = []


    def btn_ingresar_on_click(self):
        pass

    def btn_informar_on_click(self):
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()