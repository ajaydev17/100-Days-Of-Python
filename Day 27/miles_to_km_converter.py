from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)


def miles_to_km():
    miles_value = float(miles_input_field.get())
    km_value = round(miles_value * 1.609)
    km_result_label.config(text=str(km_value))


miles_input_field = Entry(width=7)
miles_input_field.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="Is Equal To")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()

