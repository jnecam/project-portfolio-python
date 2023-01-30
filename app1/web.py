import streamlit as st
from functions import get_todos, write_todos
from time import sleep

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # if todo == "":
    #
    # todos.append(todo)
    # write_todos(todos)


def clear_todo():
    clear_todos = st.session_state["cls"]
    if clear_todos:
        todos.clear()
        write_todos(todos)


st.title("TODO APP")
st.header("This is to increase your productivity.")
# clear = st.session_state['cls']
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.button(label="Clear", on_click=clear_todo, key='cls')

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

# st.session_state
