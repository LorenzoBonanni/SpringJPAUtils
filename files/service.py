from utils import *


def create_get_all(class_name):
    return f"\tpublic List<{class_name}> get{class_name}s() {{\n" + \
           f"\t\tList<{class_name}> {class_name.lower()}s = new ArrayList<>();\n" + \
           f"\t\t{class_name.lower()}Repository.findAll().forEach({class_name.lower()}s::add);\n" + \
           f"\t\treturn {class_name.lower()}s;\n" + \
           "\t}\n\n"


def create_get_by_id(class_name, content):
    return f"\tpublic {class_name} get{class_name}byId({get_id_type(get_id_row(content))} id) {{\n" + \
           f"\t\treturn {class_name.lower()}Repository.findById(id).get();\n" + \
           "\t}\n\n"


def create_add(class_name):
    return f"\tpublic void add{class_name}({class_name} {class_name.lower()}) {{\n" + \
           f"\t\t{class_name.lower()}Repository.save({class_name.lower()});\n" + \
           "\t}\n\n"


def create_update(class_name):
    return f"\tpublic void update{class_name}({class_name} {class_name.lower()}) {{\n" + \
           f"\t\t{class_name.lower()}Repository.save({class_name.lower()});\n" + \
           "\t}\n\n"


def create_delete(class_name, content):
    return f"\tpublic void delete{class_name}({get_id_type(get_id_row(content))} id) {{\n" + \
           f"\t\t{class_name.lower()}Repository.deleteById(id);\n" + \
           "\t}\n"


def create_service(class_name, content):
    service_name = f"{class_name}Service"
    dependecies = "import org.springframework.beans.factory.annotation.Autowired;\n" + \
                  "import org.springframework.stereotype.Service;\n" + \
                  "import java.util.ArrayList;\n" + \
                  "import java.util.List;\n\n"

    text = dependecies + \
           "@Service\n" + \
           f"public class {service_name} {{\n" + \
           "\t@Autowired\n" + \
           f"\tprivate {class_name}Repository {class_name.lower()}Repository;\n\n" + \
           create_get_all(class_name) + \
           create_get_by_id(class_name, content) + \
           create_add(class_name) + \
           create_update(class_name) + \
           create_delete(class_name, content) + \
           "}"

    write_file(service_name, text)