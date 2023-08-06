class TodosList:
    def __init__(self):
        self._todos = []
    
    todos = property()
    """_summary_
    This is the instanace attribute "TODOS" defines as a Property.
    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    @todos.getter
    def todos(self):
        return self._todos
    
    @todos.setter
    def todos(self, list_of_todos):
        if type(list_of_todos) != list:
            raise TypeError("The ToDos must be a List")
        self._todos = list_of_todos
    
    def __getitem__(self, _index):
        """_summary_
        Get the item from the List of todos.
        Args:
            _index (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self._todos[_index]
    
    def __len__(self):
        """_summary_
        Return the length of the todos list.
        Returns:
            _type_: _description_
        """
        return len(self._todos)
    
    def __repr__(self):
        """_summary_
        This is the representation of the todos list.
        """
        print("The Todos are: ")
        for index, todo in enumerate(self._todos):
            todo = todo.strip('\n')
            print(f"{index+1}. {todo}")
        return ""
    
    def __str__(self):
        """_summary_
        This is the string representation of the todos list.
        """
        print("The Todos are: ")
        for index, todo in enumerate(self._todos):
            todo = todo.strip('\n')
            print(f"{index+1}. {todo}")
        return ""