# Create a loop that will allow you to create a question and answer again
import json

print('WELCOME TO THE QUIZ CREATOR!')
print('\nPlease write down your questions, choices and answers bellow:\n')

quiz_data = []

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
        save = input("\nDo you want to save it? yes or no?: ").lower()

        if save in ['yes', 'y']:
            # Save to the quiz_data list as a dictionary
            quiz_data.append({
                "question": question,
                "choices": {
                    "A": choice_a,
                    "B": choice_b,
                    "C": choice_c,
                    "D": choice_d
                },
                "answer": correct_ans
            })
            break
        elif save in ['no', 'n']:
            break
        else:
            print("Invalid input, please enter yes or no")

# Ask if you want to enter a question and answer again
    enter_again = input("\nWould you like to enter again? yes or no?: ")
    if enter_again in ['yes', 'y']:
        continue
    else:
        print("Thank you")
        break
    
with open("questions.json", "a") as file:
        json.dump(quiz_data, file, indent=4)
    