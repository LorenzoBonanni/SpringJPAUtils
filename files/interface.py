from utils import *


def create_interface(class_name, content):
    dependencies = "import org.springframework.data.repository.CrudRepository;"
    repo_name = f"{class_name}Repository"
    id_row = get_id_row(content)

    text = dependencies + "\n" + \
           f"public interface {repo_name} extends CrudRepository<{class_name}, {get_id_obj_type(id_row)}> {{}}"

    write_file(repo_name, text)
