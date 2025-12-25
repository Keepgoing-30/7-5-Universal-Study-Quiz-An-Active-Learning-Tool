import random
import sys
import time
import os
from func_timeout import func_timeout, FunctionTimedOut
from quiz_data import quiz_data  

def get_user_input():
    return input("Your choice (A/B/C/D): ").strip().upper()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0
all_answers = list(quiz_data.values())

for question, correct_answer in quiz_data.items():
    options = [correct_answer]
    while len(options) < 4:
        if isinstance(correct_answer, int):
            wrong_choice = correct_answer + random.randint(-20, 20)
        else:
            wrong_choice = random.choice(all_answers)
            
        if wrong_choice != correct_answer and wrong_choice not in options:
            options.append(wrong_choice)
    
    random.shuffle(options)
    labels = ['A', 'B', 'C', 'D']
    mapped_options = dict(zip(labels, options))
    
    guess_count = 0
    guess_limit = 3
    solved = False
    timed_out = False 

    clear_screen()
    print(f"\n" + "="*40)
    print(f"QUESTION: {question}")
    for label, value in mapped_options.items():
        print(f"  {label}. {value}")
    print(f"\n⚠️  QUICK! You have 60 seconds! | Current Score: {score}")

    while guess_count < guess_limit:
        try:
            user_choice = func_timeout(60, get_user_input)
            
            if user_choice not in mapped_options:
                print("⚠️ Please enter only A, B, C, or D!")
                continue

            guess_count += 1
            if mapped_options[user_choice] == correct_answer:
                score += 1
                print(f'✨ CORRECT! -> Score: {score}')
                solved = True
                time.sleep(1.5)
                break
            else:
                if guess_count < guess_limit:
                    print(f'❌ WRONG! {guess_limit - guess_count} attempt(s) left!')

        except FunctionTimedOut:
            print(f"\n⏰ TIME'S UP!")
            print(f"💀 The correct answer was: {correct_answer}")
            score -= 1 # Trừ điểm vì để hết thời gian
            
            decision = input('\nType Y to continue or N to stop: ').strip().upper()
            if decision == 'N':
                clear_screen()
                print(f"Final Score: {score}")
                sys.exit() 
            else:
                timed_out = True
                break 

    if timed_out:
        continue 

    if not solved:
        score -= 1
        print(f'💀 FAILED! The answer was: {correct_answer}. Score: {score}')
        time.sleep(2)

clear_screen()
print(f"\n" + "="*40)
print(f"🎉 QUIZ FINISHED! Final Score: {score}/{len(quiz_data)}")