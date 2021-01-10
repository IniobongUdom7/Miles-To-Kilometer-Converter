from tkinter import *

def miles_kmt():
    miles = float(miles_input.get())
    kml = round(miles * 1.689)
    kilometer_result_label.config(text=f"{kml}")


#screen setup
screen = Tk()
screen.title("Miles to Km Converter")
screen.minsize(width=500, height=300)
screen.config(padx=200, pady=200)
#screen.bgcolor("red")

#miles input and label
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


#equal to label setup
equal_label = Label(text="Is Equal To")
equal_label.grid(column=0, row=1)

#kilometer label and result
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


kilometer_label = LabelFrame(text="Kilometers")
kilometer_label.grid(column=2, row=1)

#calculator area
calculate_button = Button(text="Calculate", command=miles_kmt)
calculate_button.grid(column=1, row=2)










