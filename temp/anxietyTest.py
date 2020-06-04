import random
"""
There is a virtual questions, get a score after answering the question
"""
questions = {
    "Q01": ["今天是哪一年？", {"A": ["2017", 1], "B": ["2018", 2], "C": ["2019", 3]}],
    "Q02": ["今天是哪一月？", {"A": ["八月份", 1], "B": ["九月份", 2], "C": ["十月份", 3]}],
    "Q03": ["今天是哪一日？", {"A": ["17号", 1], "B": ["18号", 2], "C": ["19号", 3]}]
}

def displayQues(qnum):
    """display question and its options"""

    options = list(questions[qnum][1].keys())
    print("Q.{}".format(questions[qnum][0]))
    for o in options:
        print("{} {}".format(o, questions[qnum][1][o][0]))

QList = list(questions.keys())
random.shuffle(QList)
score = 0
for i in QList:
    displayQues(i)

    answer = input("Please enter option: ").upper()
    opt = list(questions[i][1].keys())
    while answer not in opt:
        answer = input("Input error! Please re-enter option: ").upper()

    score += questions[i][1][answer][1]

print("{}\nYour total score: {}\n---END---\n".format('='*35, score))
