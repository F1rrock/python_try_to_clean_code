from tkinter import *

from feature.domain.use_cases.power import Power
from feature.presentation.business_logic.power_business_logic import PowerBusinessLogic


class MainPage:
    powerBusinessLogic: PowerBusinessLogic

    def __init__(self):
        self.powerBusinessLogic = PowerBusinessLogic(Power())
        root = Tk(className='первое задание')
        Label(root, text='Сколько штук?').grid(column=0, row=0, pady=10)
        input1 = Entry(root)
        input2 = Entry(root)
        input1.grid(column=0, row=1, pady=20, padx=50)
        input2.grid(column=0, row=2, pady=20)
        input1.get()
        input2.get()
        Button(root, text="push me", command=lambda: ).grid(column=0,
                                                                                                              row=3,
                                                                                                              pady=20)
        root.mainloop()
