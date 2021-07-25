import phonenumbers
from phonenumbers import carrier, geocoder, timezone

import tkinter as tk
from tkinter import Button, Entry, Label, StringVar, Text
from tkinter.constants import END, DISABLED

from phonenumbers.phonenumberutil import NumberParseException

#---------------------------------------------------
#main class of main application

class PhoneNum:

    #-------------------initialize window of application---------------------------
    def __init__(self, title="Phone Number Recognition"):
        self.main_w = tk.Tk()
        self.main_w.geometry('900x380')
        self.main_w.title(title)
        self.main_w.resizable(width=False, height=False)
        self.main_w.iconbitmap(r'Phone.ico')

    #--------------------------------Widgets---------------------------------------
    def widgets(self):
        self.number = StringVar()
        self.error = StringVar()
        self.c = StringVar()
        self.op = StringVar()

        Label(self.main_w, text="Введите номер телефона с '+': ", font='Arial 12').grid(row=0, column=0, padx=10, pady=10)
        Entry(self.main_w, textvariable=self.number, width=60, font='Arial 12').grid(row=0, column=1)
        Button(self.main_w, text='Показать данные', width=30, command= self.showDataNumber, font='Arial 12').grid(row=1, column=0, padx=10, pady=10)
        Button(self.main_w, text='Сброс', width=30, command=self.clearAllWidgets, font='Arial 12').grid(row=1, column=1, padx=10, pady=10)
        self.error_msg = Label(self.main_w, textvariable=self.error, font="Arial 14 bold", fg="#ED0000")
        self.error_msg.place(x=120, y=100)
        Label(self.main_w, text='Регионы: ', font='Arial 12').place(x=20, y=120)
        self.textBox = Text(self.main_w, width=30, height=5, font='Arial 12')
        self.textBox.place(x=20, y=160)
        self.c.set("Страна:   ")
        self.op.set("Оператор:   ")
        Label(self.main_w, textvariable=self.c, font='Arial 12').place(x=20, y=260)
        Label(self.main_w, textvariable=self.op, font='Arial 12').place(x=20, y=280)
    
    #--------------------------------Show Data of number---------------------------------------
    def showDataNumber(self):
        try:
            self.phone_num = phonenumbers.parse(self.number.get())
            #get and show timezone of number
            regions_list = timezone.time_zones_for_number(self.phone_num)
            if(regions_list):
                self.str_list = "\n".join([city for city in regions_list])
                self.textBox.config(state='normal')
                self.textBox.insert(END, self.str_list)
                self.textBox.config(state='disabled')

            self.error_msg.after(10, self.error_msg.destroy)
            #get and show country
            country = geocoder.description_for_number(self.phone_num, "ru")
            if(len(country) > 0):
                self.c.set(self.c.get() + '{}'.format(country))
            else:
                self.c.set(self.c.get() + "Н.Д")
            #get and show carrier
            operator = carrier.name_for_number(self.phone_num, "ru")
            if(len(operator) > 0):
                self.op.set(self.op.get() + '{}'.format(operator))
            else:
                self.op.set(self.op.get() + "Н.Д")
        except NumberParseException:
            self.error.set("Введенный номер не существует или неверный формат ввода!")

    def clearAllWidgets(self):
        self.number.set("")
        self.error.set("")
        self.textBox.config(state='normal')
        self.textBox.delete('1.0', END)
        self.textBox.config(state=DISABLED)
        self.c.set("Страна:   ")
        self.op.set("Оператор:   ")

    #--------------------------------------Run App-------------------------------------------
    def run(self):
        self.widgets()
        self.main_w.mainloop()

#--------------------------------------------------------------------------------------------

app = PhoneNum()
app.run()

#-------------------------------------------------------------------------------------------- 
    