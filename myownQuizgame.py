


from ansicolors import Colors
t = Colors


print(f"{t.YELLOW}==========================================================")
print("                  24 KARAT QUESTIONS                                 ")
print(f"=========================================================={t.END}")


#player name input
name = input("Enter player name: ")
print(f"Good luck, {name}!")

questions = ("1. Software is defined as ______: ",
            "2. Comments in Python are written with a special character, which one?: ",
            "3. Which one is NOT a legal variable name? ",
            "4. What are the features of Software Code?: ",
            "5. What is the correct file extension for Python files?: ",
            "6. What is the correct syntax to output the type of a variable or object in Python?",
            "7. Which method can be used to remove any whitespace from both the beginning and the end of a string?",
            "8. Which collection is ordered, changeable, and allows duplicate members?",
            "9. How do you start writing a for loop in Python?",
            "10. Which statement is used to stop a loop?")

options =  (("A. set of programs, documentation & configuration of data", "B. set of programs", "C. documentation and configuration of data", "D. None of the mentioned"),
                   ("A. #This is a comment", "B. =This is a comment", "C. -This is a comment", "D. None of these above"),
                   ("A. my-var", "B. my_var", "C. _myvar", "D. Myvar"),
                   ("A. Simplicity", "B. Accessibility", "C. Modularity", "D. All of the above"),
                   ("A. .pyt", "B. .pyth", "C. .py", "D. .pogi"),
                   ("A. print(typeof x)","B. print(type(x))","C. print(typeOf(x))","D. printypeME"),
                   ("A. strip()","B. len()","C. ptrim","D. trim()"),
                   ("A. Tuple","B. Set","C. Dictionary","D. List"),
                   ("A. for x in y","B. for x > y","C. for each x in y","D. for y in x"),
                   ("A. return","B. exit","C. stop","D. break"))


answers = ("A", "A", "A", "C", "C", "B", "A", "D","A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("==========================================================")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print(f"{t.GREEN}CORRECT!{t.END}")
    else:
        print(f"{t.RED}INCORRECT!{t.END}")
        print(f"{t.RED}{answers[question_num]} is the correct answer.{t.END}")
    question_num += 1

print(f"{t.PURPLE}--------   RESULTS   --------{t.END}")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


if score <= 50:
    print(f"{t.RED}Better luck nxt time!{t.END}")
elif score >= 100:
    print(f"{t.BLUE}Congratulations, You're a genius!{t.END}")

