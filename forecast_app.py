import tkinter as tk
from tkinter import Button, Label, StringVar, ttk
import requests
import webbrowser

#------------------------------Main Class----------------------------------
class ForecastApp:
    def __init__(self, title="Weather Forecast"):
        self.main_w = tk.Tk()
        self.main_w.geometry('400x250')
        self.main_w.title(title)
        self.main_w.iconbitmap(r'sunny_sunshine.ico')
        self.citys = ["Astrakhan", "Moscow", "St.Petersburg", "Volgograd", "Omsk", "Kaliningrad"]
        self.citys.sort()

#--------------------------------Widgets---------------------------------------
    def widgets(self):
        self.city = StringVar()
        self.input_l = Label(self.main_w, text="Ваш город: ").grid(row=0, column=0, padx=10, pady=10)
        self.city_comb = ttk.Combobox(self.main_w, textvariable=self.city, values=self.citys).grid(row=0, column=1, padx=20, pady=10)
        self.button_show = Button(self.main_w, text='Показать прогноз', command= self.showForecast).grid(row=1, column=0, padx=10, pady=10)
        self.button_exit = Button(self.main_w, text='Выйти', width=14, command=self.main_w.quit).grid(row=2, column=0, padx=10, pady=3)
#----------------------------Open Browser's Page------------------------
    def showForecast(self):
        url = 'https://wttr.in/{}'.format(self.city.get())
        reqs = requests.get(url)
        webbrowser.open(url, new=1)

    def run(self):
        self.widgets()
        self.main_w.mainloop()


# print('\n')
# print('\t\t\t ' + '-' * 22)
# print('\t\t\t|    ' + 'ПРОГНОЗ ПОГОДЫ' + '    |')
# print('\t\t\t ' + '-' * 22, "Special thanks to @igor_chubin")
# print("~" * 24 + '\t' * 3 + "~" * 30)

#--------------------------------------------------------------------------------------------

app = ForecastApp()
app.run()

#-------------------------------------------------------------------------------------------- 


    


