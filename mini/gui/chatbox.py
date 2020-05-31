from tkinter import *


#functions


# create window

app = Tk()

app.title("Global CS Chatbot")
app.geometry('700x350')




# chatarea
chat_area = Listbox(app, height=8, width=50)
chat_area.grid(row=0, column=0, columnspan=4, rowspan=2, pady=20, padx=20)

# textbox
input_txt = StringVar()
input_label = Label(app, text='Input', font=('bold', 14), pady=20)
input_label.grid(row=5, column=0)
input_area = Entry(app, textvariable=input_txt)
input_area.grid(row=5, column=0, rowspan=3, columnspan=5)

# createscrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=0, column=4)

# setscroll to listbox
chat_area.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=chat_area.yview)

#button
send_btn = Button(app, text='Send Message', width=12, command=send_message)
send_btn.grid(row=5, column=6)

# start program
app.mainloop()
