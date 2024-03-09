import streamlit as st

from streamlit_option_menu import option_menu
import bookname,writername


class MultiApp:
    
    def __init__(self):
        self.apps =[]
    def add_app(self, title, function):
        self.apps.append({
            "title":title,
            "function":function
        })
        
    def run():
        
        app = option_menu(
        menu_title=None,
        options=["책명","작가"],
        icons=["book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
)
    
        if app == "책명":
            bookname.app()
        if app =="작가":
            writername.app()
            
    run()