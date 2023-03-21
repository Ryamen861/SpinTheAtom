from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import random

# TODO fix the displaying of images
# TODO get rid of buttons, make text entries

FONT1 = ("Times New Roman", 24, "normal")
S_FONT = ("Times New Roman", 18, "normal")

class SpinTheAtom:
    def __init__(self):
        self.curr_ans = []

        self.categories = ["Atomic Structure", "Periodic Table and Electrons", "Bonding and Naming",
                           "Types of Reactions \nand Balancing Equations", "Stoichiometry", "Energy"]
        self.difficulties = ["E", "M", "H"]

        self.window = Tk()
        self.window.title("Spin The Atom!")
        self.window.geometry("1200x600")
        self.window.resizable(True, True)
        self.window.config(padx=50, pady=50)

        # category entry
        self.category_label = Label(text="Enter the Category Number Below!", font=FONT1)
        self.category_label.grid(row=0, column=0)

        self.category_entry = Entry(width=20, font=FONT1)
        self.category_entry.grid(row=1, column=0)

        # difficulty entry
        self.difficulty_label = Label(text="Enter the Difficulty Below \n(first letter, uppercased)", font=FONT1)
        self.difficulty_label.grid(row=0, column=2)

        self.difficulty_entry = Entry(width=20, font=FONT1)
        self.difficulty_entry.grid(row=1, column=2)

        self.get_question_button = Button(text="Get Question!", width=15, command=self.get_question, font=S_FONT)
        self.get_question_button.grid(row=2, column=1)

        self.question_label = Label(text="", font=FONT1)
        self.question_label.grid(row=3, column=0, columnspan=3)
        self.question_label.config(pady=20)

        self.get_a_button = Button(text="Get Answer!", width=15, command=self.get_ans, font=S_FONT)
        self.get_a_button.grid(row=4, column=1)

        self.ans_label = Label(text="", font=FONT1)
        self.ans_label.grid(row=5, column=0, columnspan=3)

        self.tk_image = PhotoImage(file="images/blank_for_SpinTheAtom.png")
        self.image_display = Label(width=800, height=300, image=self.tk_image)
        self.image_display.grid(row=6, column=0, columnspan=3, sticky="NE")

        self.window.mainloop()

    def get_question(self):
        self.curr_ans.clear()
        self.ans_label.config(text="")

        with open("questions.json") as file:
            data = json.load(file)  # save the data in a var

        d = self.difficulty_entry.get()
        c = self.category_entry.get()
        
        # check if valid inputs
        if d not in self.difficulties:
            messagebox.showerror(title="Input Error", message='Please enter in the first letter of the difficulty, capitalized.\nEx: for medium, "M"')

        if int(c) not in range(1, 7):
            messagebox.showerror(title="Input Error", message="Please enter in a number between 1 and 6")

        possible_questions = list(data[c][d].items())

        question_obj = random.choice(possible_questions)[1]
        print(question_obj)
        question = question_obj["question"]
        ans = question_obj["answer"]
        image_path = question_obj["image"]

        # update question label
        self.question_label.config(text=question)
        self.curr_ans.append(ans)

        # update canvas
        if image_path == "images/NO IMAGE.png":
            self.tk_image = PhotoImage(file="images/blank_for_SpinTheAtom.png")
            self.image_display.config(image=self.tk_image)
        else:
            self.tk_image = PhotoImage(file=image_path)
            self.image_display.config(image=self.tk_image)
        # try:
        #     with open("questions.json") as file:
        #         data = json.load(file)  # read the data
        # except FileNotFoundError:
        #     with open("questions.json", "w") as makefile:
        #         default_data = {
        #             "1": {"This is question number one": "This is the answer to number one"},
        #             "2": {"This is question number two": "This is the answer to number two"},
        #             "3": {"This is question number three": "This is the answer to question three"},
        #             "4": {"This is question number four": "This is the answer to question four"},
        #             "5": {"This is question number five": "This is the answer to question five"}
        #         }
        #         json.dump(default_data, makefile, indent=4)  # entering data into the json file
        #     get_question()    # call itself to restart the process, but now with a json file
        #
        # else:
        #     for q, a in data[number].items():
        #         curr_set[0] = q
        #         curr_set[1] = a
        #
        #     # clear the answer label
        #     ans_label.config(text="")
        #
        #     question_label.config(text=f"{curr_set[0]}")
        #     number_entry.delete(0, END)  # clear the inputs

    def get_ans(self):
        self.ans_label.config(text=f"{self.curr_ans[0]}")


if __name__ == "__main__":
    SpinTheAtom()
