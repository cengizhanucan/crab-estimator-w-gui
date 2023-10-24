from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import webbrowser
import tkinter as tk
from idlelib.tooltip import Hovertip
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ctypes as ct
from tkinter import PhotoImage
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class CrabEstimatorApp:



    def __init__(self):
        self.l1 = None
        self.l2 = None
        self.l3 = None
        self.l4 = None
        self.l5 = None
        self.l6 = None
        self.entry1 = None
        self.entry2 = None
        self.entry3 = None
        self.win = Tk()
        self.win.geometry("720x480")
        self.win.resizable(False, False)
        dark_title_bar(self.win)
        self.create_main_frame()
        self.create_buttons()
        self.create_title_frame()
        self.setup_window()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack(fill='both', expand=1)
        bg = ImageTk.PhotoImage(file=resource_path("c1.png"))
        self.bg_label = tk.Label(self.main_frame, image=bg)
        self.bg_label.image = bg  # Keep a reference to the image to prevent garbage collection
        self.bg_label.place(relwidth=1, relheight=1)
        
    def create_buttons(self):
        button_frame = tk.Frame(self.main_frame)

        # Make these image variables instance variables by prefixing them with 'self'
        self.linkedin_image = PhotoImage(file=resource_path('l.png')).subsample(3, 3)
        self.github_image = PhotoImage(file=resource_path('g.png')).subsample(3, 3)
        self.kaggle_image = PhotoImage(file=resource_path('k.png')).subsample(3, 3)

        linkedin_button = ttk.Button(
            button_frame,
            image=self.linkedin_image,
            command=lambda: webbrowser.open_new_tab("https://www.linkedin.com/in/cengizhanucan/"),
            bootstyle=(SECONDARY, OUTLINE)
        )

        github_button = ttk.Button(
            button_frame,
            image=self.github_image,
            command=lambda: webbrowser.open_new_tab("https://github.com/cengizhanucan"),
            bootstyle=(SECONDARY, OUTLINE)
        )

        kaggle_button = ttk.Button(
            button_frame,
            image=self.kaggle_image,
            command=lambda: webbrowser.open_new_tab("https://www.kaggle.com/cengizhanucan"),
            bootstyle=(SECONDARY, OUTLINE)
        )

        linkedin_button.pack(side="left", padx=10)
        github_button.pack(side="left", padx=10)
        kaggle_button.pack(side="left", padx=10)

        socials = ttk.Label(self.main_frame, text="Socials", font=("tkDefaultFont", 7))
        button_frame.pack(side="bottom", pady=5)
        socials.pack(side="bottom", pady=0)
        Hovertip(linkedin_button, 'A link to my LinkedIn profile', hover_delay=500)
        Hovertip(github_button, 'A link to my GitHub profile', hover_delay=500)
        Hovertip(kaggle_button, 'A link to my Kaggle profile', hover_delay=500)
        
    def create_title_frame(self):
        title_frame = tk.Frame(self.main_frame)
        title = ttk.Label(title_frame, text="How Old Is Your Crab?", font=("tkDefaultFont", 20))
        title2 = ttk.Label(title_frame, text="A Crab Age Estimator Tool", font=("tkDefaultFont", 10))

        btn1 = ttk.Button(title_frame, text="Begin", command=self.switch_to_second_frame, bootstyle=(DARK, OUTLINE))
        btn2 = ttk.Button(title_frame, text="About", command=self.switch_to_about_frame, bootstyle=(DARK, OUTLINE))

        title.pack(side="top", pady=0)
        title2.pack(side="top", pady=5)
        btn1.pack(side="top", pady=5)
        btn2.pack(side="top", pady=5)
        title_frame.place(relx=0.5, rely=0.4, anchor="center")

    def create_second_frame(self):
        self.second_frame = tk.Frame(self.win)

        # Set background image for the second frame
        bg1 = ImageTk.PhotoImage(file=resource_path("c2.png"))  # Replace with the path to your image
        bg_label = tk.Label(self.second_frame, image=bg1)
        bg_label.image = bg1
        
        bg_label.place(relwidth=1, relheight=1)
        
        # Create labels at the top center
        label1 = ttk.Label(self.second_frame, text="Question Nr. 1:", font=("tkDefaultFont", 22))
        label2 = ttk.Label(self.second_frame, text="What is the gender of your crab?", font=("tkDefaultFont", 16))
        label3 = ttk.Label(self.second_frame, text="(You can Turn your crab upside down to check.)", font=("tkDefaultFont", 8))

        label1.pack(side="top", pady=0)
        label2.pack(side="top", pady=0)
        label3.pack(side="top", pady=0)


        # Create a variable to store the user's selection
        self.gender_selection = IntVar()

        # Create a frame to hold the radio buttons
        radio_frame = tk.Frame(self.second_frame)
        male_radio = ttk.Radiobutton(radio_frame, text="Male", variable=self.gender_selection, value=1, bootstyle=(DARK))
        female_radio = ttk.Radiobutton(radio_frame, text="Female", variable=self.gender_selection, value=2,bootstyle=(DARK))

        male_radio.pack(side="left", padx=150, pady=5)
        female_radio.pack(side="left", padx=150, pady=5)

        # Create buttons at the bottom right
        button1 = ttk.Button(self.second_frame, text="Next", command=self.switch_to_third_frame, bootstyle=(DARK, OUTLINE))

        button1.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

        # Place the radio frame at the center of the second frame
        radio_frame.pack(side="top", pady=10)
        img_path3 = resource_path("c3.png")  # Replace with the actual image path
        img3 = ImageTk.PhotoImage(file=img_path3)
        img_label3 = tk.Label(self.second_frame, image=img3)
        img_label3.image = img3
        img_label3.pack(side="top", padx=10, pady=0)
        # Place the second frame so that it fills the entire window
        self.second_frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        
    def create_third_frame(self):
        self.third_frame = tk.Frame(self.win)

        # Set background image for the third frame
        bg1 = ImageTk.PhotoImage(file=resource_path("c2.png"))  # Replace with the path to your image
        bg_label = tk.Label(self.third_frame, image=bg1)
        bg_label.image = bg1
        bg_label.place(relwidth=1, relheight=1)

        # Create labels and buttons as needed for the fourth frame
        label7 = ttk.Label(self.third_frame, text="Question Nr. 3:", font=("tkDefaultFont", 22))
        label8 = ttk.Label(self.third_frame, text="What are the lengths of your crab?", font=("tkDefaultFont", 16))
        label9 = ttk.Label(self.third_frame, text="(You can use a Tape Measure for this step. Use centimeter values.)",font=("tkDefaultFont", 8))
        label7.pack(side="top", pady=0)
        label8.pack(side="top", pady=0)
        label9.pack(side="top", pady=0)
        # Create a single dimension frame with an image on the left
        dimension_frame = tk.Frame(self.third_frame)
        dimension_frame.pack(side="top", padx=10, pady=0)

        img_path = resource_path("c4.png")  # Replace with the actual image path
        img = PhotoImage(file=img_path).subsample(2, 2)
        img_label = tk.Label(dimension_frame, image=img)
        img_label.image = img
        img_label.pack(side="left", padx=10, pady=5)

        # Create a separate frame on the right
        labels_frame = tk.Frame(dimension_frame)
        labels_frame.pack(side="left", padx=10, pady=5)

        # Create labels and entry fields in a vertical line
        label1 = ttk.Label(labels_frame, text="Length:", font=("tkDefaultFont", 12))
        label1.pack(side="top", pady=5)

        self.entry1 = ttk.Entry(labels_frame, font=("tkDefaultFont", 12))
        self.entry1.insert(0, 'Enter a numeric value.')
        self.entry1.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry1, 'Enter a numeric value.'))
        self.entry1.pack(side="top", pady=5)

        label2 = ttk.Label(labels_frame, text="Diameter:", font=("tkDefaultFont", 12))
        label2.pack(side="top", pady=5)

        self.entry2 = ttk.Entry(labels_frame, font=("tkDefaultFont", 12))
        self.entry2.insert(0, 'Enter a numeric value.')
        self.entry2.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry2, 'Enter a numeric value.'))
        self.entry2.pack(side="top", pady=5)

        label3 = ttk.Label(labels_frame, text="Height:", font=("tkDefaultFont", 12))
        label3.pack(side="top", pady=5)

        self.entry3 = ttk.Entry(labels_frame, font=("tkDefaultFont", 12))
        self.entry3.insert(0, 'Enter a numeric value.')
        self.entry3.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry3))
        self.entry3.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry3, 'Enter a numeric value.'))
        self.entry3.pack(side="top", pady=5)

        # Create a "Next" button
        button2 = ttk.Button(self.third_frame, text="Next", command=self.switch_to_fourth_frame, bootstyle=(DARK, OUTLINE))
        button2.pack(side=BOTTOM, anchor="e", padx=8, pady=10)

        # Place the third frame so that it fills the entire window
        self.third_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def create_fourth_frame(self):
        self.fourth_frame = tk.Frame(self.win)
        # Set background image for the second frame
        bg1 = ImageTk.PhotoImage(file=resource_path("c2.png"))  # Replace with the path to your image
        bg_label = tk.Label(self.fourth_frame, image=bg1)
        bg_label.image = bg1
        bg_label.place(relwidth=1, relheight=1)

        # Create labels and buttons as needed for the fourth frame
        label7 = ttk.Label(self.fourth_frame, text="Question Nr. 4:", font=("tkDefaultFont", 22))
        label8 = ttk.Label(self.fourth_frame, text="What are the weights of your crab?", font=("tkDefaultFont", 16))
        label9 = ttk.Label(self.fourth_frame, text="(You can use a precision scale for this step. Use gram values.)",font=("tkDefaultFont", 8))
        label10 = ttk.Label(self.fourth_frame, text="Shucked Weight: Weight of the crab after the shell is removed.",font=("tkDefaultFont", 7),foreground="darkred")

        button3 = ttk.Button(self.fourth_frame, text="Next", command=self.switch_to_fifth_frame, bootstyle=(DARK, OUTLINE))
        label7.pack(side="top", pady=0)
        label8.pack(side="top", pady=0)
        label9.pack(side="top", pady=0)
        label10.pack(side="top", pady=0)
        # Create a single dimension frame with an image on the left
        dimension_frame = tk.Frame(self.fourth_frame)
        dimension_frame.pack(side="top", padx=10, pady=0)

        img_path = resource_path("c5.png")  # Replace with the actual image path
        img = PhotoImage(file=img_path).subsample(3, 3)
        img_label = tk.Label(dimension_frame, image=img)
        img_label.image = img
        img_label.pack(side="top", padx=10, pady=5)
        labels_frame1 = tk.Frame(dimension_frame)
        labels_frame1.pack(side="left", padx=10, pady=5)

        #create a entry field frame inside the dimension frame
        labels_frame2 = tk.Frame(dimension_frame)
        labels_frame2.pack(side="right", padx=10, pady=5)

        # Create labels and entry fields in a vertical line
        label1 = ttk.Label(labels_frame1, text="Weight:", font=("tkDefaultFont", 12))
        label1.pack(side="top", padx=5)

        self.entry1 = ttk.Entry(labels_frame1, font=("tkDefaultFont", 12))
        self.entry1.insert(0, 'Enter a numeric value.')
        self.entry1.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry1, 'Enter a numeric value.'))
        self.entry1.pack(side="top", padx=5)

        label2 = ttk.Label(labels_frame2, text="Shucked Weight:", font=("tkDefaultFont", 12))
        label2.pack(side="top",padx=5)

        self.entry2 = ttk.Entry(labels_frame2, font=("tkDefaultFont", 12),foreground="darkred")
        self.entry2.insert(0, 'You are a horrible person.')
        self.entry2.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry2, 'Enter a numeric value.'))
        self.entry2.pack(side="top", padx=5)

        button3.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

        self.fourth_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def create_fifth_frame(self):
        self.fifth_frame = tk.Frame(self.win)

        # Set background image for the second frame
        bg1 = ImageTk.PhotoImage(file=resource_path("c2.png"))  # Replace with the path to your image
        bg_label = tk.Label(self.fifth_frame, image=bg1)
        bg_label.image = bg1
        bg_label.place(relwidth=1, relheight=1)
        # Create labels and buttons as needed for the fifth frame
        label10 = ttk.Label(self.fifth_frame, text="Congratulations! Your crab is", font=("tkDefaultFont", 22))
        label11 = ttk.Label(self.fifth_frame, text="Your crab is(was)", font=("tkDefaultFont", 22))
        #create a random float with 10 decimals between 0 and 3
        import random
        random_float = random.uniform(0, 3)
        #create a string that contains the random float with 10 decimals
        random_float_string = str(round(random_float, 10))
        label12 = ttk.Label(self.fifth_frame, text=random_float_string+" years old.", font=("tkDefaultFont", 18))
        
        gif_frames = [
            PhotoImage(file=resource_path("c6.gif"), format="gif -index %i" % i)
            for i in range(99)  # Replace 31 with the number of frames in your GIF
        ]

        def update_gif(ind):
            frame = gif_frames[ind]
            ind += 1
            if ind >= len(gif_frames):
                ind = 0  # Restart the animation when all frames are shown
            gif_label.configure(image=frame)
            self.fifth_frame.after(100, update_gif, ind)  # Adjust the delay (in milliseconds) to control the GIF speed
        gif_label = ttk.Label(self.fifth_frame)
        gif_label.pack()

        # Start the GIF animation by calling the update_gif function
        update_gif(0)

        button4 = ttk.Button(self.fifth_frame, text="Try again.", command=self.switch_to_main_frame, bootstyle=(DARK, OUTLINE))

        label10.pack(side="top", pady=0)
        label11.pack(side="top", pady=0)
        label12.pack(side="top", pady=0)
        button4.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

        self.fifth_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def create_about_frame(self):
        self.about_frame = tk.Frame(self.win)
        # Set background image for the second frame
        bg1 = ImageTk.PhotoImage(file=resource_path("c2.png"))  # Replace with the path to your image
        bg_label = tk.Label(self.about_frame, image=bg1)
        bg_label.image = bg1
        bg_label.place(relwidth=1, relheight=1)

        # Create labels and buttons as needed for the fourth frame
        label7 = ttk.Label(self.about_frame, text="Question Nr. 3:", font=("tkDefaultFont", 22))
        label8 = ttk.Label(self.about_frame, text="What are the weights of your crab?", font=("tkDefaultFont", 16))
        label9 = ttk.Label(self.about_frame, text="(You can use a precision scale for this step.)",font=("tkDefaultFont", 8))
        button3 = ttk.Button(self.about_frame, text="Go Back to Menu", command=self.switch_to_main_frame, bootstyle=(DARK, OUTLINE))
        #add a gif
        label7.pack(side="top", pady=0)
        label8.pack(side="top", pady=0)
        label9.pack(side="top", pady=0)
        button3.pack(side=BOTTOM, anchor="e", padx=8, pady=8)
        
        self.about_frame.place(relwidth=1, relheight=1, relx=0, rely=0)



    def setup_window(self): 
        self.win.title("Crab Estimator")

        self.win.mainloop()
        
    def switch_to_second_frame(self):
        self.destroy_current_frame()
        self.create_second_frame()
        # Restore the user's selection
        if hasattr(self, 'gender_selection'):
            self.gender_selection.set(1)  # Set the default selection to Male (or any other default)

    def switch_to_third_frame(self):
        self.destroy_current_frame()
        self.create_third_frame()

    def switch_to_fourth_frame(self):
        self.l1 = self.entry1.get()
        self.l2 = self.entry2.get()
        self.l3 = self.entry3.get()
        self.destroy_current_frame()
        self.create_fourth_frame()

    def switch_to_fifth_frame(self):
        self.l4 = self.entry1.get()
        self.l5 = self.entry2.get()
        print("l1",self.l1, "l2",self.l2,"l3", self.l3,"l4",self.l4,"l5",self.l5)
        print("gender",self.gender_selection.get())
        self.destroy_current_frame()
        self.create_fifth_frame()

    def switch_to_main_frame(self):
        self.destroy_current_frame()
        self.create_main_frame()
        self.create_buttons()
        self.create_title_frame()

    def switch_to_about_frame(self):
        self.destroy_current_frame()
        self.create_about_frame()
        pass
    def destroy_current_frame(self):
        if hasattr(self, 'second_frame'):
            self.second_frame.destroy()
        if hasattr(self, 'third_frame'):
            self.third_frame.destroy()
        if hasattr(self, 'fourth_frame'):
            self.fourth_frame.destroy()
        if hasattr(self, 'fifth_frame'):
            self.fifth_frame.destroy()
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()
        if hasattr(self, 'about_frame'):
            self.about_frame.destroy()

def focus_out_entry_box(widget, widget_text):
    if len(widget.get()) == 0:
        widget.delete(0, END)
        widget.insert(0, widget_text)

def dark_title_bar(window):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),4)
    
def focus_in_entry_box(widget):
        widget.delete(0, END)
if __name__ == "__main__":
    app = CrabEstimatorApp()
