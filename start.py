from tkinter import *
import time
import os

from App.GUI import GUIApp


App = Tk()

screen_width = 640
screen_height = 440

App.title('Bet Selector')
App.geometry("{}x{}".format(screen_width, screen_height))
App.resizable(False, False)
App.configure(bg='#ecf0f1')

GUIApp(App, screen_width, screen_height)

App.mainloop()
