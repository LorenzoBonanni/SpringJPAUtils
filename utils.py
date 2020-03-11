import os
import re


def get_id_row(content: str):
    splitted_content = content.split("\n")
    flag = 0
    for r in splitted_content:
        if flag:
            if "public" in r or "private" in r:
                return r
        if "@Id" in r:
            flag = 1


def get_id_obj_type(id_row: str):
    regex = "(private|public) (.*?) "
    result = re.search(regex, id_row)
    id_type = result.groups()[1]
    if id_type == "char":
        return "Character"
    elif id_type == "int":
        return "Integer"
    else:
        return id_type.title()


def get_id_type(id_row: str):
    regex = "(private|public) (.*?) "
    result = re.search(regex, id_row)
    id_type = result.groups()[1]
    return id_type


def write_file(name, content):
    if not os.path.exists("output"):
        os.mkdir("output")
    with open("output/" + name + ".java", 'w') as f:
        f.write(content)
