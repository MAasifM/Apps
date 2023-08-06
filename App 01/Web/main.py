import streamlit as st
from class_text_file import TextFile
T = TextFile()


def add_todo():
    todo = st.session_state["add_todo"]
    T._write_todos_(todo)


st.title("My Todo App")
st.subheader("This is my ToDo App.")
st.write("This app is to increase your productivity.")

for Index, ToDo in enumerate(T._get_todos_()):
    checkbox = st.checkbox(ToDo, key=ToDo)
    if checkbox:
        T._remove_todos_(Index)
        del st.session_state[ToDo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo here...",
              on_change=add_todo, key="add_todo")
