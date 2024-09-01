from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from data_getter import SignIn

class ShowData:
    def __init__(self, old_root, original_course_dict, original_grade_dict):
        self.root = old_root
        self.root.title("Grades Page")

        # variables
        self.course_dict = original_course_dict
        self.grade_dict = original_grade_dict