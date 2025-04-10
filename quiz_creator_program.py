# Create a loop that will allow you to create a question and answer again
file = open("quiz_file.txt", "a")

while True:
# Inside the loop:
# Ask enter a question
    question = input("Enter a question: ")

# Ask to enter choices for A, B, C, and D
    choice_a = input("Enter answer for A: ")
    choice_b = input("Enter answer for B: ")
    choice_c = input("Enter answer for C: ")
    choice_d = input("Enter answer for D: ")

# Ask enter the correct answer
    while True:
        correct_ans = input("Enter the correct answer: ").upper()
        if correct_ans in ['A', 'B', 'C', 'D']:
            break
        print("Invalid input, Please type A, B, C, and D only")

# Ask if you want to save
    while True:
        save = input("Do you want to save it? yes or no?: ").lower()
        if save in ['yes', 'y']:
# if yes, all the question and answer will be writen to another file
            file.write(f"\n\n\nQUESTION: \n{question}\n")
            file.write(f"CHOICES:\n")
            file.write(f"A. {choice_a}\n")
            file.write(f"B. {choice_b}\n")
            file.write(f"C. {choice_c}\n")
            file.write(f"D. {choice_d}\n")
            file.write(f"ANSWER:\n{correct_ans}")
            break
# if no, it will not be saved and automatically proceed
        elif save in ['no', 'n']:
            break
        else:
            print("Invalid input, please enter yes or no")

# Ask if you want to enter a question and answer again
# If yes, it will ask to input the questions and answers again
# if no, it will exit the loop and close the program
    break
