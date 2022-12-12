# MCQ using Dictionary

# Key -> Question and Options
# Value -> Correct Answer

#Questins
q1 = """ Q.1 Favorite Color
    A. Blue
    B. Black
    C. White
    D. Orange 
    """

q2 = """ Q.1 Favorite Color or
    A. Blue
    B. Black
    C. White
    D. Orange 
    """

q3 = """ Q.1 Favorite Color which
    A. Blue
    B. Black
    C. White
    D. Orange 
    """

q4 = """ Q.1 Favorite Color are
    A. Blue
    B. Black
    C. White
    D. Orange 
    """

q5 = """ Q.1 Favorite Color is
    A. Blue
    B. Black
    C. White
    D. Orange 
    """
# Create Dictionary

questions = {q1: "A", q2: "A", q3: "B", q4: "B", q5: "C"}
print("""
      ---Welcome to Quiz---
    Rules:
    1. choose Single answer.
    2. If answer is correct the 1 point
    3. If answer is wrong then -1 point
    4. If all answers are correct you will get Certified
        """)

name = input("Enter your Name : ")

print("Welcome, ", name)
pts = 0

for i in questions:
    print(i)  # i is the key
    # ch = input("Do you want to Skip this Question - Y/N :")
    # if ch.capitalize() == "Y":
    #     continue

    ans = input("Enter Your Option : ")

    if ans.capitalize() == questions[i]:
        pts = pts+1
        print("\t\t\t\t\t\t\t\t (score = ", pts, ")")

    else:
        pts = pts - 1
        print("\t\t\t\t\t\t\t\t ""(score = ", pts, ")")
    chquit = input("Do you want to Quit this Quiz - Y/N :")
    print("-------------------------------------------------------------------------------")
    if chquit.capitalize() == "Y":
        break

print(name, "your final score is :", pts)
