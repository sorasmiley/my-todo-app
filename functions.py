FILEPATH = "todos.txt" # You can just change file name here.


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    # read file and store current todos in list
    # file = open('todos.txt', 'r')
    # todos = file.readlines()
    # file.close()
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # create variable to hold list todos
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file.
    It modifies text file but it does not need to return anything.
    """
    # first argument is path to file, second argument is write or read
    # file = open('todos.txt', 'w') # store the file object
    # file.writelines(todos)
    # file.close()
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)