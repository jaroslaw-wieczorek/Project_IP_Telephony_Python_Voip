import tkinter as tk
import pyaudio
import socket
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

        self.login = tk.Button(self.window, text="Zaloguj się", command=self.login)
        self.login.pack()

        #self.logout = tk.Button(self.window, text="Wyloguj się", command=self.logout)
        #self.logout.pack()

        self.window.configure(background="#AED84C")

        self.window.mainloop()

    def login(self):
        print(socket.gethostbyname(socket.gethostname()))

        login, password = self.etr_Login.get(), self.etr_Password.get()
        password = hashlib.sha256(password.encode()).hexdigest()

        # wysyłanie login password do serwera
        # Klient.Client(login, password)

        print(self.login, ' ', password)

    #def logout(self):


app = App()