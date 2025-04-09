# Create a loop that will allow you to create a question and answer again
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
    correct_ans = input("Enter the correct answer: ")
    
# Ask if you want to save
# if yes, all the question and answer will be writen to another file
# if no, it will not be saved and automatically proceed

# Ask if you want to enter a question and answer again
# If yes, it will ask to input the questions and answers again
# if no, it will exit the loop and close the program
    break
