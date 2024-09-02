from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class ShowData:
    def __init__(self, old_root, original_course_dict, original_grade_dict):
        self.root = old_root
        self.root.title("Grades Page")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # colors for differentiating classes
        self.colors = {
            "background": "#f0ead6",
            1: "#eb6a6a",
            2: "#eb8f6a",
            3: "#ebab6a",
            4: "#ebcd6a",
            5: "#c4eb6a",
            6: "#6aeba6",
            7: "#6aebde",
            8: "#6abaeb",
            9: "#6a82eb",
            10: "#ab6aeb",
            11: "#d56aeb",
            12: "#eb6ab3",
            "extra": "#ccb1b1"
        }

        self.grades_frame = Frame(self.root, bg=self.colors["background"])
        self.grades_frame.grid(column=0, row=0, sticky=(N, E, S, W), padx=12, pady=12)

        # variables
        self.course_dict = original_course_dict
        self.grade_dict = original_grade_dict

        self.place_classes_and_grades()

    def place_classes_and_grades(self):
        for i, course_id in enumerate(self.course_dict.keys()):
            
            if i+1 < 13:
                color = self.colors[i+1]
            else:
                color = self.colors["extra"]

            class_name = self.course_dict[course_id][0].lstrip().rstrip().center(45)
            
            course_code = None
            if self.course_dict[course_id][1]:
                course_code = self.course_dict[course_id][1].center(45)

            letter_grade = None
            if self.grade_dict[course_id]:
                number_grade = str(round(self.grade_dict[course_id], 3)).center(15)

                letter_grade = ("A" if self.grade_dict[course_id] >= 90 else 
                            "B" if self.grade_dict[course_id] >= 80 else 
                            "C" if self.grade_dict[course_id] >= 70 else 
                            "D" if self.grade_dict[course_id] >= 60 else 
                            "F").center(15)
            else:
                number_grade = "No Grade".center(15)
            
            if course_code and letter_grade:
                full_text = f"{class_name}  |  {course_code}  |  {number_grade}  |  {letter_grade}"
            elif course_code and not letter_grade:
                full_text = f"{class_name}  |  {course_code}  |  {number_grade}  |  {number_grade}"
            elif letter_grade and not course_code:
                full_text = f"{class_name}  |  {number_grade}  |  {letter_grade}"
            else:
                full_text = f"{class_name}  |  {number_grade}  |  {number_grade}"

            class_label = Label(self.grades_frame, bg=color, font=("Courier", 15), text=full_text, anchor="w")
            class_label.grid(column=0, row=i+1, sticky=(W, E), padx=12, pady=12)