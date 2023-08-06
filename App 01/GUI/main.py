from class_text_file import TextFile
import PySimpleGUI as sg
import time
text_file = TextFile()

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=text_file._get_todos_(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            new_todo = values['todo'] + "\n"
            text_file._write_todos_(new_todo)
            window['todos'].update(values=text_file._get_todos_())

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                text_file._edit_todos_(todo_to_edit, new_todo)
                window['todos'].update(values=text_file._get_todos_())
            except IndexError:
                sg.popup("Please select an item first.",
                         font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                text_file._remove_todos_(todo_to_complete)
                window['todos'].update(values=text_file._get_todos_())
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.",
                         font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
