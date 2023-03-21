from tkinter import *
from tkinter import messagebox
import json
import random

# TODO fix the displaying of images
# TODO get rid of buttons, make text entries

FONT1 = ("New Courier", 18, "normal")


class SpinTheAtom:
    def __init__(self):
        self.curr_ans = []
        self.keys = {
            "category": "",
            "difficulty": ""
        }
        self.categories = ["Atomic Structure", "Periodic Table and Electrons", "Bonding and Naming",
                           "Types of Reactions \nand Balancing Equations", "Stoichiometry", "Energy"]
        self.difficulties = ["E", "M", "H"]

        self.window = Tk()
        self.window.title("Spin The Atom!")
        self.window.geometry("800x600")
        self.window.resizable(True, True)
        self.window.config(padx=50, pady=50)

        # category chooser
        self.category_label = Label(text="Click Below!", font=FONT1)
        self.category_label.grid(row=0, column=0)

        self.category_button = Button(text="Get Category", width=20, command=self.get_category)
        self.category_button.config(pady=15)
        self.category_button.grid(row=1, column=0)

        # difficulty chooser
        self.difficulty_label = Label(text="Click Below!", font=FONT1)
        self.difficulty_label.grid(row=0, column=2)

        self.difficulty_button = Button(text="Get Question!", width=20, command=self.get_difficulty)
        self.difficulty_button.grid(row=1, column=2)
        self.difficulty_button.config(pady=15)

        self.get_question_button = Button(text="Get Question!", width=20, command=self.get_question)
        self.get_question_button.grid(row=2, column=1)

        self.question_label = Label(text="", font=FONT1)
        self.question_label.grid(row=3, column=1)
        self.question_label.config(pady=20)

        self.get_a_button = Button(text="Get Answer!", width=20, command=self.get_ans)
        self.get_a_button.grid(row=4, column=1)

        self.ans_label = Label(text="", font=FONT1)
        self.ans_label.grid(row=5, column=1)
        self.ans_label.config(pady=20)

        self.canvas = Canvas(self.window, width=800, height=500)
        self.curr_image = PhotoImage(file="images/C1a.png")
        self.displayed_image = self.canvas.create_image(250, 250, image=self.curr_image)
        self.canvas.grid(row=6, column=0, columnspan=3)

        self.window.mainloop()

    def get_difficulty(self):
        difficulty = random.choice(self.difficulties)

        # update label
        self.difficulty_label.config(text=difficulty)

        # add to list
        self.keys["difficulty"] = difficulty

    def get_question(self):
        self.curr_ans.clear()
        self.ans_label.config(text="")

        with open("questions.json") as file:
            data = json.load(file)  # save the data in a var

        c = self.keys["category"]
        d = self.keys["difficulty"]

        if c == "" or d == "":
            messagebox.showerror(message="Make sure to get Category and Question first!")

        possible_questions = list(data[c][d].items())

        question_obj = random.choice(possible_questions)[1]
        print(question_obj)
        question = question_obj["question"]
        ans = question_obj["answer"]
        image = question_obj["image"]

        # update question label
        self.question_label.config(text=question)
        self.curr_ans.append(ans)

        # update canvas
        if image != "images/NO IMAGE.png":
            self.curr_image = PhotoImage(file=image)
            self.canvas.itemconfig(self.displayed_image, image=self.curr_image)
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

    def get_category(self):
        num = random.randint(1, 6)
        # random.randint is inclusive

        # find the actual category
        category = self.categories[num - 1]

        # update label
        self.category_label.config(text=category)

        # add number to list
        self.keys["category"] = str(num)


if __name__ == "__main__":
    SpinTheAtom()
