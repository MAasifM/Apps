import streamlit as st
import pandas

st.set_page_config(layout="wide")


class WebApp:

    def __init__(self, image=None, name=" ", content=""):
        self._image = image
        self._name = name
        self._content = content

    def _build_web_app_(self):

        col1, col2 = st.columns(2)

        with col1:
            st.image(self._image)

        with col2:
            st.title(self._name)
            st.info(self._content)

        content2 = """
        Below you can find some of the apps I have built in Python. Feel free to contact me!
        """
        st.write(content2)

        col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

        df = pandas.read_csv("data.csv", sep=";")

        with col3:
            for index, row in df[:10].iterrows():
                st.header(row["title"])
                st.write(row["description"])
                st.image("images/" + row["image"])
                st.write(f"[Source Code]({row['url']})")

        with col4:
            for index, row in df[10:].iterrows():
                st.header(row["title"])
                st.write(row["description"])
                st.image("images/" + row["image"])
                st.write(f"[Source Code]({row['url']})")
