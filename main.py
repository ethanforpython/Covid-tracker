from tkinter import *
import bs4
import requests
import speech_recognition as sr
import pyttsx3

result = requests.get("https://www.worldometers.info/coronavirus/#countries")
info = bs4.BeautifulSoup(result.text, "lxml")

root = Tk()
root.geometry("700x500")

total_world_cases = info.select('span')[4].text
total_world_deaths = info.select('span')[5].text
total_world_recoveries = info.select('span')[6].text


class MainScreen:
    def __init__(self):
        self.total_world_cases = total_world_cases
        self.total_world_deaths = total_world_deaths
        self.total_world_recoveries = total_world_recoveries

    def startup_screen(self):
        world_headers = Label(root,
                              text=f'Worldwide cases    Worldwide deaths    Worldwide recoveries',
                              font=('helvetica', 16))
        value_of_worldwide_cases = Label(root,
                                         text=self.total_world_cases,
                                         font=('helvetica', 16))
        value_of_worldwide_deaths = Label(root,
                                          text=self.total_world_deaths,
                                          font=('helvetica', 16))
        value_of_worldwide_recover = Label(root,
                                           text=self.total_world_recoveries,
                                           font=('helvetica', 16))

        world_headers.place(x=60, y=20)
        value_of_worldwide_cases.place(x=80, y=60)
        value_of_worldwide_deaths.place(x=265, y=60)
        value_of_worldwide_recover.place(x=450, y=60)

    def usa_updates(self):
        total_cases = info.select('td')[5436].text
        print(total_cases)


s = MainScreen()
s.usa_updates()
root.mainloop()
