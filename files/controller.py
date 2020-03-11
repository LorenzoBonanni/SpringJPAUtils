from utils import *


def create_get_all(class_name):
    return "\t@RequestMapping(method = RequestMethod.GET)\n" + \
           f"\tpublic {class_name}Wrapper get{class_name}s() {{\n" + \
           f"\t\treturn new {class_name}Wrapper({class_name}Service.get{class_name}s());\n" + \
           "\t}\n\n"


def create_get_by_id(class_name, content):
    return '\t@RequestMapping(method = RequestMethod.GET, value = "/{id}")\n' + \
           f"\tpublic {class_name} get{class_name}byId(@PathVariable {get_id_type(get_id_row(content))} id) {{\n" + \
           f"\t\treturn {class_name.lower()}Service.get{class_name}byId(id);\n" + \
           "\t}\n\n"


def create_add(class_name):
    return "\t@RequestMapping(method = RequestMethod.POST)\n" + \
           f"\tpublic void add{class_name}(@RequestBody {class_name} {class_name.lower()}) {{\n" + \
           f"\t\t{class_name.lower()}Service.add{class_name}({class_name.lower()});\n" + \
           "\t}\n\n"


def create_update(class_name):
    return "\t@RequestMapping(method = RequestMethod.PUT)\n" + \
           f"\tpublic void update{class_name}(@RequestBody {class_name} {class_name.lower()}) {{\n" + \
           f"\t\t{class_name.lower()}Service.update{class_name}({class_name.lower()});\n" + \
           "\t}\n\n"


def create_delete(class_name, content):
    return '\t@RequestMapping(method = RequestMethod.DELETE, value = "/{id}")\n' + \
           f"\tpublic {class_name} delete{class_name}(@PathVariable {get_id_type(get_id_row(content))} id) {{\n" + \
           f"\t\treturn {class_name.lower()}Service.delete{class_name}(id);\n" + \
           "\t}\n\n"


def create_controller(class_name: str, content: str):
    controller_name = f"{class_name}Controller"

    text = "import org.springframework.web.bind.annotation.*;\n\n" + \
           "@RestController\n" + \
           f'@RequestMapping(value = "/{class_name.lower()}s")\n' + \
           f"public class {controller_name} {{\n" + \
           "\t@Autowired\n" + \
           f"\tprivate {class_name}Service {class_name.lower()}Service;\n\n" + \
           create_get_all(class_name) + \
           create_get_by_id(class_name, content) + \
           create_add(class_name) + \
           create_update(class_name) + \
           create_delete(class_name, content) + \
           "}"

    write_file(controller_name, text)
