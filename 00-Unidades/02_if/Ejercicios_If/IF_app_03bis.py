import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Alejandro Daniel
apellido: López Pino
---
Ejercicio: if_03bis
---
Enunciado:
A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir mas de 1.80 metros
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Altura (en metros)") # modifique el texto porque decia edad
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_altura = customtkinter.CTkEntry(master=self) #modifique self.txt_edad y le puse txt_altura, así coincidía con el enunciado.
        self.txt_altura.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        altura = float(self.txt_altura.get())
        minimo = 1.80

        if altura >= minimo:
            alert("Basquet", "Serás pivot")
        else:
            alert("Basquet", "No serás pivot")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()