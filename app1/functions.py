import PySimpleGUI as sg

# The function takes a default parameter.
#  when calling the function, we don't need to pass any arguments since the function takes a default parameter.
# The function takes a default parameter.
#  when calling the function, we don't need to pass any arguments since the function takes a default parameter.
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the text and returns the list of to-do list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# we need a filepath to write to and the todos we will be writing to the file.

def write_todos(todos_args, filepath=FILEPATH):
    """write the to-do items in the next file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_args)


# def my_popup():
#     layout = [
#         [sg.Text("Are You Sure!")],
#         [sg.Button("OK"), sg.Button("CANCEL")]
#     ]
#     win = sg.Window("", layout, modal=True,
#                     grab_anywhere=True, enable_close_attempted_event=True)
#     event, value = win.read()
#     if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
#         event = "CANCEL"
#
#     win.close()
#     win.write_event_value(event, None)


