from Question import Question

Questions = [
    "Is Trump male or female? \na) male\tb) female  c) unknown\n",
    "What color are apples?\na) Red\tb) blue\tc) purple\n",
    "Which is year is current year?\na) 1990\tb) 2008\tc) 2021\n" 
]

gotQuestion = [
    Question(Questions[0], "a"),
    Question(Questions[1], "a"),
    Question(Questions[2], "c"),
]   #set the correct answer

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You already finish it! Your score is: "+ str(score) + " / " + str(len(questions)))

run_test(gotQuestion)