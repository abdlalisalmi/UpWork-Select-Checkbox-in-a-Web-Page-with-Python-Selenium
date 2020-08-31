from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from selenium import webdriver

import os
import time

from App.Core import Core


class GUIApp:
    def __init__(self, master, screen_width, screen_height):
        self.driver = master
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.files_paths = None

        self.chromeDriver = os.path.realpath(__file__)
        self.chromeDriver = os.path.split(self.chromeDriver)[0]
        self.chromeDriver = os.path.join(self.chromeDriver, 'chromedriver')

        self.showLogo()
        self.showStartBtn()
        self.showSelectFileBtn()
        self.showTextField()
        self.showQuitBtn()

    def showLogo(self):
        Label(self.driver, text="☑ Bet Selector", bg='#ecf0f1',
              fg='#574b90', font=('Helvetica', 30)).place(x=205, y=10)
        Label(self.driver, text="Make it easy ¯\_(ツ)_/¯", bg='#ecf0f1',
              fg='#574b90', font=('Helvetica', 10)).place(x=205, y=50)

    def showStartBtn(self):
        def startProgramme():
            if self.files_paths:
                try:
                    URL = 'https://bet.hkjc.com/football/odds/odds_hfmp.aspx?lang=en'
                    driver = webdriver.Chrome(self.chromeDriver)
                    driver.get(URL)
                    time.sleep(5)
                except Exception:
                    messagebox.showinfo(
                        "Bet Selector", "The WebDriver Not found.")

                if messagebox.askquestion("askquestion", "Are you logged in?") == 'yes':
                    i = 0
                    for file_path in self.files_paths:
                        Core(file_path, driver)
                        if i < len(self.files_paths) - 1:
                            q = messagebox.askquestion(
                                "Bet Selector", "Do you want to continue to the next file?")
                            if not q == 'yes':
                                break
                        i += 1

            else:
                messagebox.showinfo("Bet Selector",
                                    "You need to select at least one Bet file.")
        Button(
            self.driver, font=("Arial Bold", 10),
            fg="white", bg='#40407a',
            text="Start Program  ▶", command=startProgramme
        ).place(x=250, y=150)

    def showSelectFileBtn(self):
        self.showBorder(50, 93, width=67)

        def importFromFile():
            try:
                self.filePATH.destroy()
            except:
                pass
            filesPATHs = filedialog.askopenfilenames(
                initialdir=os.path.dirname(os.path.realpath(__file__)),
                title="Select file",
                filetypes=(("text files", "*.txt"),)
            )
            files_names = ""
            files_paths = ""
            for path in filesPATHs:
                files_paths += '{}\n'.format(path)
                files_names += '{}, '.format(os.path.split(path)[1])

            self.filePATH = Label(self.driver, text=files_names,
                                  fg='#575fcf', bg='#ecf0f1', font=("Arial Bold", 9))
            self.filePATH.place(x=55, y=105)
            self.showTextField(content=files_paths)
            self.files_paths = filesPATHs

        Label(self.driver, text="Select Bet Files:",
              fg='#303952', bg='#ecf0f1', font=("Arial Bold", 11)).place(x=50, y=80)
        Button(
            self.driver, font=("Arial Bold", 8),
            fg="white", bg='#575fcf',
            text="Browse", command=importFromFile
        ).place(x=500, y=100)

    def showTextField(self, content=''):
        Label(self.driver, text="Files open:",
              fg='#303952', bg='#ecf0f1', font=("Arial Bold", 11)).place(x=50, y=180)
        self.texField = Text(self.driver, bg='#f1f2f6', fg="#1e272e", borderwidth=2, height=12,
                             width=67, font=("Arial Bold", 9))
        self.texField.insert(END, content)
        self.texField.config(state=DISABLED)
        self.texField.place(x=50, y=200)

    def showQuitBtn(self):
        frame = Frame(self.driver)
        frame.place(x=535,
                    y=400)
        self.quit = Button(frame,
                           text="QUIT", fg="white", bg='#ff5e57',
                           command=frame.quit, font=("Arial Bold", 9))
        self.quit.grid(row=0, column=0)

    def showBorder(self, x, y, height=2, width=48):
        Label(self.driver,
              borderwidth=2,
              bg='#ecf0f1',
              width=width,
              height=height,
              relief="ridge",).place(x=x, y=y)
