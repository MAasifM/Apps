from class_todos import TodosList
TEXT_FILE_PATH = r'C:\CureMD\Courses\Pyhton Megs Course\Apps\App 01\Web\todos.txt'


class TextFile(TodosList):
    def __init__(self):
        super().__init__()
        return None

    def _get_todos_(self, filepath=TEXT_FILE_PATH):
        """_summary_
        Read a text file and return the list of the to-do items.
        Args:
            filepath (str, optional): _description_. Defaults to "todos.txt".
        """
        with open(filepath, 'r') as current_file:
            current_todos = current_file.readlines()
        self._todos = current_todos
        print(self)
        return current_todos

    def _write_todos_(self, list_of_todos=None, filepath=TEXT_FILE_PATH):
        """_summary_
        Write the to-dos items list in a textfile.
        Args:
            list_of_todos (_type_, optional): _description_. Defaults to None.
            filepath (str, optional): _description_. Defaults to "todos.txt".
        """
        self._todos.append(list_of_todos + "\n")
        with open(filepath, 'w') as current_file:
            current_file.writelines(self._todos)

    def _remove_todos_(self, todo_number, filepath=TEXT_FILE_PATH):
        """_summary_
        Remove a to-dos item from the list in a textfile.
        Args:
            list_of_todos (_type_, optional): _description_. Defaults to None.
            filepath (str, optional): _description_. Defaults to "todos.txt".
        """
        self._todos.pop(todo_number)
        with open(filepath, 'w') as current_file:
            current_file.writelines(self._todos)

    def _edit_todos_(self, todo_number, filepath=TEXT_FILE_PATH):
        """_summary_
        Edit a To Do.
        Args:
            list_of_todos (_type_, optional): _description_. Defaults to None.
            filepath (str, optional): _description_. Defaults to "todos.txt".
        """
        edited_todo = input("Write To Do: ")
        self._todos[todo_number] = edited_todo + "\n"
        with open(filepath, 'w') as current_file:
            current_file.writelines(self._todos)
