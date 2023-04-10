import tkinter as tk
from tkinter import messagebox


class TresEnRaya:
    def __init__(self):
        self.turno = "X"
        self.tablero = [["", "", ""], ["", "", ""], ["", "", ""]]

        self.ventana = tk.Tk()
        self.ventana.title("Tres en Raya")

        self.botones = []
        for i in range(3):
            fila = []
            for j in range(3):
                boton = tk.Button(self.ventana, text="", width=10, height=5, command=lambda i=i, j=j: self.jugar(i, j))
                boton.grid(row=i, column=j)
                fila.append(boton)
            self.botones.append(fila)

    def jugar(self, i, j):
        if self.tablero[i][j] == "":
            self.tablero[i][j] = self.turno
            self.botones[i][j].config(text=self.turno)
            if self.ganador():
                tk.messagebox.showinfo("Tres en Raya", "Ganó " + self.turno)
                self.ventana.destroy()
            elif self.empate():
                tk.messagebox.showinfo("Tres en Raya", "Empate")
                self.ventana.destroy()
            else:
                if self.turno == "X":
                    self.turno = "O"
                else:
                    self.turno = "X"

    def ganador(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != "":
                return True
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != "":
                return True
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != "":
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != "":
            return True
        return False

    def empate(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == "":
                    return False
        return True

    def empezar(self):
        self.ventana.mainloop()

juego = TresEnRaya()
juego.empezar()
