import mysql.connector
from _global import *
from init import init
from services import *
from tkinter import *

class Row:
    def __init__(self, row_num, name, display_frame):
        self.row_num = row_num
        self.name = name
        self.display_frame = display_frame
        self.row_font = ('Arial', 15)

    def delete(self, name):
        print(f"name to be deleted -> {name}")

        # delete code

        temp = get_details()
        render_row(temp)

    def plot(self):
        self.row_frame = Frame(self.display_frame, borderwidth=1, relief="solid", width=550)
        self.row_frame.grid(row=self.row_num, column=0, padx=5, pady=5, sticky=(W, E))
        Label(self.row_frame, text=self.row_num, font=self.row_font).grid(row=0, column=0, padx=5, pady=5, sticky=W)
        Label(self.row_frame, text=self.name, font=self.row_font, width=40).grid(row=0, column=1, padx=5, pady=5, sticky=E)
        Button(self.row_frame, text="X", font=self.row_font, command=lambda: self.delete(self.name)).grid(row=0, column=2, padx=5, pady=5, sticky=E)

def add_emp():
    # insert code 

    temp = get_details()
    render_row(temp)

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def search():
    temp_name = search_entry.get()
    print(temp_name)
    temp = []
    if temp_name == "":
        render_row(emp_array)
        return
    for i in emp_array:
        if temp_name == i[1]:
            temp.append(i)

    emp_array[:] = temp
    print(temp, emp_array)
    render_row(temp)

def render_row(array):
    clear(display_frame)
    header_font = ('Arial', 12, 'bold')
    headers = ["ID", "Name"]
    header_frame = Frame(display_frame, width=550, background='white')
    header_frame.grid(row=0, column=0, sticky=W)
    for col_num, header in enumerate(headers):
        Label(header_frame, text=header, font=header_font, background='white').grid(row=0, column=col_num, padx=10, pady=5, sticky=W)
    row_array = []
    for row_num, (id, name, unit, phone) in enumerate(array, start=1):
        row_array.append(Row(row_num, name, display_frame))
        row_array[-1].plot()

init()
emp_array = get_details()
print(emp_array)
root = Tk()
root.geometry("800x600")
root.title("home")

side_frame = Frame(root, height=600, width=200)
side_frame.place(x=0, y=0)

main_frame = Frame(root, background='white', height=600, width=600)
main_frame.place(x=200, y=0)

search_frame = Frame(main_frame, bg="light grey", width=550, border=2, borderwidth=2)
search_frame.place(x=25, y=25)
search_entry = Entry(search_frame, width=71)
search_entry.grid(row=0, column=0, padx=5, pady=5)
search_button = Button(search_frame, text="Search", command=search)
search_button.grid(row=0, column=1, padx=5, pady=5)
add_button = Button(search_frame, text="add+", command=add_emp)
add_button.grid(row=0, column=2, padx=5, pady=5)

# Create a canvas and a scrollbar for the display frame
canvas = Canvas(main_frame, bg='grey', height=500, width=550)
canvas.place(x=25, y=75)
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.place(x=575, y=75, height=500)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the display content
display_frame = Frame(canvas, bg='grey', width=550)
canvas.create_window((0, 0), window=display_frame, anchor='nw')

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

display_frame.bind('<Configure>', on_configure)

render_row(emp_array)

root.mainloop()
