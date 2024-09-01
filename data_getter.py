from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from canvasapi import Canvas

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
        self.sign_in_button = ttk.Button(self.sign_in_frame, text='Sign In', width=16, style="Blue.TButton", command=self.sign_in_func)
        self.sign_in_button.grid(column=1, row=5, sticky=E, padx=12)

    def sign_in_func(self):
        try:
            self.sign_in_frame.destroy()
            ShowData(self.root, course_dict, grade_dict)
        except Exception as e:
            pass

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
