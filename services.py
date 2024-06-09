from _global import *
from tkinter import *

def get_details():
    db = mysql.connector.connect(
      host=mysql_host,
      user=mysql_user,
      password=mysql_pwd)
    print(f"Connected to database: {mysql_user}")
    cursor = db.cursor()
    cursor.execute(f"USE {mysql_db}")
    cursor.execute(f"SELECT * FROM {emp_table};")
  
    return list(cursor.fetchall())

class Row:
    def __init__(self, row_num , name, display_frame):
        self.id = row_num
        self.name = name
        self.display_frame = display_frame
        self.row_font =  ('Arial', 15)
    def delete(self, name):
        pass
    def plot(self):
        self.row_frame = Frame(self.display_frame, borderwidth=1, relief="solid", width= 550)
        self.row_frame.grid(row=self.row_num, column=0, padx=5, pady=5, sticky=(W, E))
        Label(self.row_frame, text=id, font=self.row_font).grid(row=self.row_num, column=0, padx=5, pady=5, sticky=W)
        Label(self.row_frame, text=self.name, font=self.ow_font,width = 40).grid(row=self.row_num, column=1, padx=5, pady=5, sticky=E)
        Button(self.row_frame, text = "X", font=self.row_font, command = lambda : self.delete(self.name)).grid(row=self.ow_num, column=2, padx=5, pady=5, sticky=E)