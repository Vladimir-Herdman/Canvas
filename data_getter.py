from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from canvasapi import Canvas


class SignIn:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Token Sign In")

        self.sign_in_frame = ttk.Frame(root, padding='12 12 12 12')
        self.sign_in_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

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
        self.sign_in_button = ttk.Button(self.sign_in_frame, text='Sign In', command=self.sign_in_func, bg='lightblue')
        self.sign_in_button.grid(column=0, row=3, columnspan=2, sticky=(W, E))

    def sign_in_func(self):
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
                Hello, is this message box
                working
            """
        )
