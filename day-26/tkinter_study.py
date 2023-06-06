import tkinter


window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I'm Label!!!!", font=("Arial", 25, "bold"))

# advanced python argument
# label_state = {
#     "side": "left"
# }
# my_label.pack(side="left")
my_label.pack()
my_label["text"] = "New text1"
my_label.config(text="New text2")

# button
def button_clicked():
    next_text = input.get()
    my_label.config(text=next_text)

button = tkinter.Button(text="Click Me!!", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry()
input.pack()


window.mainloop()