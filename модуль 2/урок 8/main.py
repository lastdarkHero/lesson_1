from course import get_course, today
from tkinter import *

window = Tk()
window.title("Банк")
window.resizable(width=False, height=False)
window.geometry("500x500")
background = PhotoImage(file=r"C:\Users\user\Desktop\vs\gwufc.gif")

img_logo = PhotoImage(file=r"C:\Users\user\Desktop\vs\gwufc.gif")
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)

title_label = Label(window, text="Банк КРЫМА", font="TimesNewsRoman 34")
title_label.place(x=120, y=40)

course_label = Label(window, text=f"Курсы валют на {today} число:", font="TimesNewsRoman 20")
course_label.place(x=35, y=160)

dollar_info = f"{get_course('R01235').get('name')} {get_course('R01235').get('value')} руб."
dollar_label = Label(window, text=dollar_info, font="TimesNewsRoman 16")
dollar_label.place(x=80, y=215)


euro_info = f"{get_course('R01239').get('name')} {get_course('R01239').get('value')} руб."
euro_label = Label(window, text=euro_info, font="TimesNewsRoman 16")
euro_label.place(x=80, y=245)

yan_info = f"{get_course('R01375').get('name')} {get_course('R01375').get('value')} руб."
yan_label = Label(window, text=yan_info, font="TimesNewsRoman 16")
yan_label.place(x=80, y=275)



entry = Entry(font="TimesNewsRoman 16", width=10)
entry.place(x=80, y=400)



y = 30


def search():
    global y

    currency_id = entry.get()
    currency_info = f"{get_course(currency_id).get('name')} {get_course(currency_id).get('value')} руб."
    currency_label = Label(window, text=currency_info, font="TimesNewsRoman 16")
    currency_label.place(x=80, y=245 + y)

    y += 30


button = Button(text="Поиск", font="TimesNewsRoman 18", command=search)
button.place(x=200, y=400)

window.mainloop()





