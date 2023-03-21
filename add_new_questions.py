from tkinter import *
from tkinter import messagebox


def parse_question():
    question = number_entry.get()

    if len(question) <= 0:
        messagebox.showerror(title="Input Error", message="Nothing has been entered in!")

    try:
        with open("raw_questions.txt", "a") as file:
            file.write(question + "\n")
    except FileNotFoundError:
        with open("raw_questions.txt", "w") as file:
            # call itself to write it in the txt file
            parse_question()
    else:
        number_entry.delete(0, END)  # clear the inputs


font1 = ("New Courier", 18, "normal")

window = Tk()
window.title("Science Project")
window.geometry("900x500")
window.resizable(True, True)
window.config(padx=50, pady=50)

number_entry_label = Label(text='Question \n(number#question#answer#imagePath ["image/filePath"])', font=font1)
number_entry_label.config(pady=10)
number_entry_label.pack()

number_entry = Entry(width=100)
number_entry.pack()

make_q_button = Button(text="Submit Question!", width=20, command=parse_question)
make_q_button.pack(pady=20)
make_q_button.config(pady=15)

window.mainloop()
