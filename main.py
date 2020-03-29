from tkinter import filedialog
from tkinter import *
from callbacks import *

window = Tk()


def open_file_manager():
    filename = filedialog.askopenfilename(title="Select file", filetypes=(("java files", "*.java"), ("all files", "*.*")))
    if filename != '':
        generate_files(filename)
    else:
        messagebox.showerror("Error", "Selected a valid file-")


def file_input():
    btn = Button(window, text="Select File", command=open_file_manager)
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)


def main():
    window.geometry('200x100')
    window.title("Spring Boot Utility")
    file_input()
    window.mainloop()


if __name__ == '__main__':
    main()
