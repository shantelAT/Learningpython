
#Make a list that has four options and at
#one point if the answer is correct, deduct
#one point if the answer is incorrect. Also it should
#have an option to skip a question designed the quiz using directories

q1 = """Is python case sensitive when dealing with identifiers
A.yes
B.no
C. Machine dependent
D.none"""

q2 = """Which of the following is not a keyword?
A.eval
B.assert
C.local
D.pass """

q3 = """Which one of these is floor division?
A./
B.//
C.%
D.none """

q4 = """What is the output of 3*1**3?
A.27
B.9
C.3
D.1"""

q5 = """ a+bc=??
A.a
B.bc
C.bca
D.abc """

answers = {q1:"a", q2:"b",q3:"c",q4:"b", q5:"c"}

score = 0


for i in answers:
    print(i)
    skip=input("do you want to skip question, yes or no? or do you want to quit?")
    if skip == "yes":
        continue
    elif skip == "quit" :
        break
    else:
    ans = input("what is your answer?")

    if ans == answers[i]:
        print("correct!")
        score = score+1
    else:
        print("wrong!")
        score=score-1


print("Your final score is ", score)
