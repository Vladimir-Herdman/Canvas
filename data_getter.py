from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from canvasapi import Canvas

from datetime import date
from pandas import to_datetime

from show_data import ShowData


class SignIn:
    def __init__(self, old_root):
        self.root = old_root
        self.root.title("Canvas Token Sign In")

        self.sign_in_frame = ttk.Frame(self.root, padding='12 12 12 12')
        self.sign_in_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # variables
        self.canvas_domain = StringVar()
        self.canvas_token = StringVar()

        # label
        domain_label = ttk.Label(self.sign_in_frame, text="Insert Canvas domain name:").grid(column=0, row=0, sticky=E)
        token_label = ttk.Label(self.sign_in_frame, text="Insert Canvas API Token:").grid(column=0, row=2, sticky=E)

        # entry
        self.domain_entry = ttk.Entry(self.sign_in_frame, width=40, textvariable=self.canvas_domain)
        self.domain_entry.grid(column=1, row=1, sticky=(W, E))
        
        self.token_entry = ttk.Entry(self.sign_in_frame, width=40, textvariable=self.canvas_token)
        self.token_entry.grid(column=1, row=3, sticky=(W, E))

        # help buttons
            # question mark image creation
        question_mark_image = PhotoImage(file="images/question_mark.png")
        question_mark_image = question_mark_image.subsample(25, 25) 
            # actual button
        self.domain_help = Button(self.sign_in_frame, image=question_mark_image, highlightthickness=0, bd=0, command=self.domain_help_func)
        self.domain_help.image = question_mark_image
        self.domain_help.grid(column=2, row=1, sticky=W, padx=3)

        self.token_help = Button(self.sign_in_frame, image=question_mark_image, highlightthickness=0, bd=0, command=self.token_help_func)
        self.token_help.image = question_mark_image
        self.token_help.grid(column=2, row=3, sticky=W, padx=3)

        # sign in button
        self.sign_in_button = ttk.Button(self.sign_in_frame, text='Sign In', width=10, command=self.sign_in_func)
        self.sign_in_button.grid(column=1, row=5, sticky=E, padx=12)

        # load saved data button
        load_button = ttk.Button(self.sign_in_frame, text='Load Saved Info', width=14, command=self.load_func)
        load_button.grid(column=1, row=5, sticky=W, padx=12)

        self.root.after(100, self.domain_entry.focus)
        self.root.bind('<Return>', self.sign_in_func)

    def load_func(self, *args):
        with open('saved_personal', 'r') as saved_data:
            data_list = saved_data.read().split(",")
            self.canvas_domain.set(data_list[0])
            self.canvas_token.set(data_list[1])
        self.sign_in_func()

    def sign_in_func(self, *args):
        try:
            # clean if needed
            if self.canvas_domain.get()[0] == "<" or self.canvas_domain.get()[-1] == ">":
                self.canvas_domain.set(self.canvas_domain.get()[1:-1])
            if self.canvas_domain.get()[-4:] == ".com":
                self.canvas_domain.set(self.canvas_domain.get()[0:-4])

            # get canvas information
            canvas = Canvas(f"https://{self.canvas_domain.get()}.com", self.canvas_token.get())

            current_user = canvas.get_current_user()
            all_courses_ever = current_user.get_courses()
            courses = list()

            today = date.today()
            if today.month > 8:
                for course in all_courses_ever:
                    course_date = to_datetime(course.start_at)
                    if course_date and course_date.month >= 8 and course_date.year == today.year:  # short circuit
                        courses.append(course)
            else:
                for course in all_courses_ever:
                    course_date = to_datetime(course.start_at)
                    if course_date and course_date.year == today.year:
                        courses.append(course)


            enrollments = list()

            course_dict = dict()  # for having the name of the course be referencable by id, as canvasapi uses id's more than course names []
            grades_dict = dict()

            for course in courses:
                id = course.id
                name = course.name

                enrollments.append(course.get_enrollments(user_id=current_user.id))
                course_dict[id] = [name]

                # if course code exists, append it to the classes dictionary list
                if course.course_code:
                    course_dict[id].append(course.course_code)

            for enrollment in enrollments:
                grades_dict[enrollment[0].course_id] = enrollment[0].grades['current_score']
            
            self.sign_in_frame.destroy()
            ShowData(self.root, course_dict, grades_dict)
        except Exception as e:
            try:
                print(f"Error in ShowData class:  {e}")
                ttk.Label(self.sign_in_frame, text='Error in canvas domain or token', foreground='red').grid(column=0, row=5, sticky=E)
            except Exception as e:
                print(f"Error in putting label to sign_in_func:  {e}")

    def domain_help_func(self):
        messagebox.showinfo(title="Domain Help", icon="info", message=
            """
                If you open Canvas to the
                dashboard page in your
                webbrowser and look at the
                url, you will see something
                that looks like this:

                https://<domain_name>.com

                <domain_name> is what you
                should copy and paste into
                the domain entry 
                
                (you don't need to include 
                the < > brackets)
            """
        )

    def token_help_func(self):
        messagebox.showinfo(title="Token Help", icon="info", message=
            """
                Canvas API Token steps:

                1. Open Canvas
                2. Click on Account
                3. Click on Settings
                4. Scroll to "Approved Integrations" 
                5. Click "+ New Access Token"
                6. Profit!

                When you create the token, 
                you can set an expiration, 
                remember to write down / save 
                the token as you can't see it 
                after the creation screen
            """
        )
