# install custom tkinter from the command prompt as pip install custom tkinter
from tkinter import Button

import customtkinter as ctk

# create defining functions for the app to function
def add_tasks():
    task = entry_field.get()
    label2 = ctk.CTkLabel(scrollable_frame,font=ctk.CTkFont('arial bold',15),
                          text=task)
    label2.pack()
    entry_field.delete(0,ctk.END)

def clear():
    task = entry_field.get()
    label2 = ctk.CTkLabel(scrollable_frame, font=ctk.CTkFont('arial bold', 15),
                        text=task)
    label2.pack()
    label2.destroy()


# creating the layouts using custom tkinter
win = ctk.CTk()
win.title('TODO App')
win.geometry('600x400')
# creating the app's interface/frontend
label0 = ctk.CTkLabel(win,text='Daily Tasks',
                      font=ctk.CTkFont('britannic bold',35))
label0.pack(anchor='center')
frame0 = ctk.CTkFrame(win,width=600,height=250)
frame0.pack(anchor='center',pady=30)
scrollable_frame = ctk.CTkScrollableFrame(frame0,width=400,corner_radius=10)
scrollable_frame.pack(pady=10)
entry_field = ctk.CTkEntry(frame0,width=600,placeholder_text='ADD TASKS',
                           placeholder_text_color='blue')
entry_field.place(x=0,y=0)
button0 = ctk.CTkButton(win,text='ADD',bg_color='blue',
                        font=ctk.CTkFont('gotham bold',15),width=400,
                        border_width=0,border_spacing=5,command=lambda :add_tasks())
button0.place(x=100,y=325)
delete_button = Button(win,text='Clear',bg='red',fg='white',font=('arial bold',15),
                       width=20,bd=0,borderwidth=1,command=lambda :clear())
delete_button.place(x=300,y=550)

win.mainloop()
