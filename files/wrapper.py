from utils import write_file


def get_getter(classname: str):
    return f"\tpublic List<{classname}> get{classname}s() {{\n" + \
           f"\t\treturn {classname.lower()}s;\n" + \
           "\t}\n"


def get_setter(classname: str, java_list: str):
    return f"\tpublic void set{classname}s({java_list}) {{\n" + \
           f"\t\treturn {classname.lower()}s;\n" + \
           "\t}\n"


def get_constructor(class_name, wrapper_name, java_list):
    return f"\tpublic {wrapper_name}({java_list}) {{\n" + \
           f"\t\tthis.{class_name.lower()}s = {class_name.lower()}s\n" + \
           "\t}\n"


def create_wrapper(class_name):
    dependencies = "import java.util.List;\n"
    wrapper_name = class_name + "Wrapper"
    java_list = f"List<{class_name}> {class_name.lower()}s"

    text = dependencies + "\n" + \
           f"public class {wrapper_name} {{\n" + \
           "\t" + java_list + ";\n" + \
           get_constructor(class_name, wrapper_name, java_list) + \
           get_getter(class_name) + \
           get_setter(class_name, java_list) + \
           "}"

    write_file(wrapper_name, text)
