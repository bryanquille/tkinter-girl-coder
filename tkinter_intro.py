from tkinter import *
from tkinter import ttk


# Creating a window
window = Tk()

# Changing the name to the window
window.title("Demo-Window")

# Sizing the window
window.geometry("800x600")

# Locking the resizable window
window.resizable(height=False, width=False)

# Changing the backgroundcolor
bg_color = "#1f6cb0"  # Creating a varible with color
window.config(bg=bg_color)




# Creating and configuring a label
fg_color = "#e7e8f5"
label_1 = Label(window, height=2, width=18, text="First Name", bg="#70a3c4", fg=fg_color, font=("Ubuntu", 16), anchor="center")

# Placing and showing the label
label_1.place(x=25, y=25)

# Creating and configuring another label
label_2 = Label(window, height=2, width=18, text="Last Name", bg="#70a3c4", fg=fg_color, font=("Ubuntu", 16), anchor="center")
label_2.place(x=25, y=90)




# Using another geometry managers

# pack()
# window_2 = Tk()
# window_2.title("Pack")
# window_2.geometry("800x600")
# window_2.resizable(width=False, height=False)
# window_2.config(bg="#f75940")
# label_3 = Label(window_2, width=20, height=3, text="Hola mundo", bg="#364857", fg="#3dc7be", font=("Arial", 18))
# label_3.pack(side=TOP)
# label_4 = Label(window_2, width=20, height=3, text="¿Cómo te va?", bg="#364857", fg="#3dc7be", font=("Arial", 18))
# label_4.pack(side=BOTTOM)

# grid()
# window_3 = Tk()
# window_3.title("Pack")
# window_3.geometry("800x600")
# window_3.resizable(width=False, height=False)
# window_3.config(bg="#892c41")
# label_5 = Label(window_3, width=20, height=3, text="Hola mundo", bg="#c89034", fg="#fbff5f", font=("Arial", 18))
# label_5.grid(row=1, column=1)
# label_6 = Label(window_3, width=20, height=3, text="¿Cómo te va?", bg="#c89034", fg="#fbff5f", font=("Arial", 18))
# label_6.grid(row=3, column=1)




# Creating entries
entry_1 = Entry(window, width=18, bd=2, bg=fg_color, fg="#444444", font=("Ubuntu", 16))
entry_1.place(x=320, y=25)

entry_2 = Entry(window, width=18, bd=2, bg=fg_color, fg="#444444", font=("Ubuntu", 16))
entry_2.place(x=320, y=90)




# Creating a Combobox
combo = ttk.Combobox(window, width=18, font=("ubuntu", 16))
combo['values'] = ("nice", "happy", "hungry")
combo.current(0)
combo.place(x=25, y=250)




# Creating a label
label_7 = Label(window, width=18, height=4, bg="#70a3c4", fg=fg_color, font=("Ubuntu", 16))
label_7.place(x=320, y=155)




# Creating a function
def sayHello():
    print("Hello world")
    entry_1Text = entry_1.get()
    entry_2Text = entry_2.get()
    comboText = combo.get()
    text = f"Hello {entry_1Text} {entry_2Text}\nYou're {comboText}"
    label_7.configure(text=text)




# Creating a button
button = Button(window, width=18, height=2, text="Click me!", bg="#f7b32d", fg="#4e4e6a", font=("Ubuntu", 16), command=sayHello)
button.place(x=25, y=155)




# SHowing the window
window.mainloop()
# window_2.mainloop()
# window_3.mainloop()