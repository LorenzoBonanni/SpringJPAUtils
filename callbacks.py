import re
import time
from tkinter import messagebox
from tkinter.messagebox import showinfo

from files.controller import create_controller
from files.interface import create_interface
from files.service import create_service
from files.wrapper import create_wrapper


def get_class_name(text):
    regex = r"class (.*?) {"
    result = re.search(regex, text)
    return result.groups()[0]


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def generate_files(path):
    content = read_file(path)
    if '@Id' in content:
        class_name = get_class_name(content)
        create_wrapper(class_name)
        create_interface(class_name, content)
        create_controller(class_name, content)
        create_service(class_name, content)
        time.sleep(0.5)
        showinfo("Status", "Finished")
    else:
        messagebox.showerror("Error", "Selected file is not a JPA Entity")
