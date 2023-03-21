import json

with open("raw_questions.txt", encoding="utf8") as file:
    contents = file.readlines()

num_assign = 1

final_questions = {"1": {
    "E": {},
    "M": {},
    "H": {},
},
                   "2": {
    "E": {},
    "M": {},
    "H": {},
},
                   "3": {
    "E": {},
    "M": {},
    "H": {},
},
                   "4": {
    "E": {},
    "M": {},
    "H": {},
},
                   "5": {
    "E": {},
    "M": {},
    "H": {},
},
                   "6": {
    "E": {},
    "M": {},
    "H": {},
},
                   }

no_newlines = []
for i in contents:
    if i != "\n":
        no_newlines.append(i)


first_category = no_newlines[0:7]
second_category = no_newlines[7:14]
third_category = no_newlines[14:22]
fourth_category = no_newlines[22:29]
fifth_category = no_newlines[29:38]
sixth_category = no_newlines[38::]

all_questions = [first_category, second_category, third_category, fourth_category, fifth_category, sixth_category]

for num in range(0, 6):
    for i in all_questions[num]:
        new_question = i.split(" # ")
        question = new_question[0]
        answer = new_question[1]
        difficulty = new_question[2]
        image = "images/" + new_question[3] if new_question[3] != "NO IMAGE" else "NO IMAGE"
        image = image.strip()
        image = image + ".png"

        category_num = num + 1
        print(category_num)
        # {"1": {"M": {"2": {"question": "What is one plus one", "answer": "this is the answer", "image": "this is the image path"} } } }
        final_questions[str(category_num)][difficulty][str(num_assign)] = {}
        final_questions[str(category_num)][difficulty][str(num_assign)]["question"] = question
        final_questions[str(category_num)][difficulty][str(num_assign)]["answer"] = answer
        final_questions[str(category_num)][difficulty][str(num_assign)]["image"] = image
        num_assign += 1

with open("questions.json", "w") as file:
    json.dump(final_questions, file, indent=4)
