from tkinter import *
from tkinter import filedialog

# create main window
root = Tk()
root.title("Notepad")

# create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# create text widget
my_text = Text(my_frame,width=60,height=20)
my_text.pack()

# create menu bar
my_menu = Menu(root)
root.config(menu=my_menu)

# create file menu
file_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=lambda: my_text.delete(1.0, END))
file_menu.add_command(label="Open",command=lambda: my_text.insert(INSERT, filedialog.askopenfilename()))
file_menu.add_command(label="Save",command=lambda: filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create edit menu
edit_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda:my_text.event_generate(("<<Cut>>")))
edit_menu.add_command(label="Copy",command=lambda:my_text.event_generate(("<<Copy>>")))
edit_menu.add_command(label="Paste",command=lambda:my_text.event_generate(("<<Paste>>")))

# create help menu
help_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About Notepad",command=lambda: messagebox.showinfo("About Notepad", "A simple notepad application made using python tkinter."))

# start tkinter main loop
root.mainloop()
