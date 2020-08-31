from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from tkinter import messagebox
import time
import os

from App.Login import username, password, security_question


class Core:
    def __init__(self, file_path, driver):
        self.driver = driver
        self.file_path = file_path
        self.file_content = self.readFileContent()
        self.file_name = os.path.split(file_path)[1]

        self.IDs_list = []

        if self.file_content:
            try:
                self.collectCheckboxsIDs()
                self.selectCheckbox()
            except NoSuchElementException:
                self.driver.close()
                messagebox.showinfo(
                    "Bet Selector", "Loading took too much time or Not yet defined.")
        else:
            messagebox.showinfo(
                "Bet Selector", "Your Bet File '{}' is Empty.".format(self.file_name))

    def readFileContent(self):
        with open(self.file_path, 'r') as f:
            file_content = f.read().split('\n')
            file_content = list(filter(None, file_content))
            return file_content

    def collectCheckboxsIDs(self):
        checkboxs = self.driver.find_elements_by_class_name("checkbox")
        IDs_list = []
        for el in checkboxs:
            IDs_list.append(el.get_attribute('id'))

        IDs_list = [IDs_list[x:x+9] for x in range(0, len(IDs_list), 9)]

        IDs_list.insert(0, [])
        for lis in IDs_list:
            lis.insert(0, "")
        self.IDs_list = IDs_list

    def selectCheckbox(self):
        for line in self.file_content:
            line = line.split(',')
            row = 1
            for choice in line:
                i = 0
                while i < len(choice):
                    self.driver.find_element_by_id(
                        self.IDs_list[row][int(choice[i])]).click()
                    i += 1
                row += 1
            self.driver.find_element_by_xpath(
                '//*[@title="Add to Slip"]').click()
