from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_title = Label(text="Miles")
miles_title.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

value_km_label = Label(text="0")
value_km_label.grid(column=1, row=1)

km_title = Label(text="km")
km_title.grid(column=2, row=1)


def mi_to_km():
    mi_value = float(miles_input.get())
    km_value = 1.609 * mi_value
    value_km_label.config(text=f"{km_value}")


convert_button = Button(text="Convert", command=mi_to_km)
convert_button.grid(column=1, row=2)

window.mainloop()