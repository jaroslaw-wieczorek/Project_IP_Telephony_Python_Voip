import tkinter as tk
import pyaudio
import socket
import Klient
import hashlib

class App(tk.Tk):
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("LocalVoip")

        self.window.geometry("300x300")

        # window.iconbitmap("")

        lbl_Login = tk.Label(self.window, text="login")
        lbl_Login.pack()

        self.etr_Login = tk.Entry(self.window)
        self.etr_Login.pack()

        lbl_Password = tk.Label(self.window, text="haslo")
        lbl_Password.pack()

        self.etr_Password = tk.Entry(self.window)
        self.etr_Password.pack()

        self.btn = tk.Button(self.window, text="Zaloguj sie", command=self.login)

        self.btn.pack()

        self.window.configure(background="#AED84C")

        self.window.mainloop()

    def login(self):
        print(socket.gethostbyname(socket.gethostname()))

        login,password = self.etr_Login.get(), self.etr_Password.get()
        password = hashlib.sha256(password.encode()).hexdigest()

        Klient.Client(login, password)

        print(login, ' ', password)

app = App()