#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import platform
import time

from data.questions import QUESTIONS
from data.answers import ANSWERS

def main():

    # Set the proper command for clearing the screen based on OS
    if platform.system() == 'Windows':
        clear = 'cls'
    else:
        clear = 'clear'

    correct_counter = 0
    incorrect_counter = 0

    total_questions = len(ANSWERS)
    fancy_print('Welcome to VEFT QuizUp!')
    print('There are a total of ' + str(total_questions) + ' questions in this quiz!')
    print('To quit type "q" or ctrl+c')
    print('Good luck!\n')

    answered_questions = list()

    start = time.time()
    # Play quiz
    while 1337:

        # print number of questions left
        left = total_questions - len(answered_questions)
        msg = str(left) + ' questions left!'
        if left <= 1:
            msg = str(left) + ' question left!'
        fancy_print(msg)

        # Get next question
        while 42:
            question = random.choice(list(QUESTIONS))
            if question not in answered_questions:
                answered_questions.append(question)
                break

        correct_answer = ANSWERS[question]
        options = QUESTIONS[question]
        random.shuffle(options)
        
        print(question + '\n')
        counter = 1
        for option in options:
            print(str(counter) + ':', option)
            counter += 1

        invalid_input = True
        while invalid_input:
            try:
                answer = input('--> ')
                if answer.lower() == 'q':
                    exit(0)
                val = int(answer)-1
            except ValueError:
                continue

            if val in range(len(options)):
                invalid_input = False
        
        os.system(clear)

        if options[val] == correct_answer:
            correct_counter += 1
            percent = int((correct_counter / (correct_counter+incorrect_counter)) * 100)
            print('--> Correct!')
            print('--> You have ' + str(correct_counter) + '/' + str(correct_counter+incorrect_counter) + ' correct answers. ('+ str(percent) + '%)\n')
        else:
            incorrect_counter += 1
            percent = int(correct_counter / (correct_counter+incorrect_counter) * 100)
            print('--> Incorrect!')
            print('--> Correct answer is: ' + correct_answer)
            print('--> You have ' + str(correct_counter) + '/' + str(correct_counter+incorrect_counter) + ' correct answers. ('+ str(percent) + '%)\n')

        if len(answered_questions) == total_questions:
            percent = int(correct_counter / (correct_counter+incorrect_counter) * 100)
            elapsed_time = time.time() - start
            fancy_print('You finished in ' + get_time_string(elapsed_time) + ' with ' + str(correct_counter) + '/' + str(correct_counter+incorrect_counter) + ' correct answers. ('+ str(percent) + '%)')
            if percent == 100:
                fancy_print('Such score, very knowledge!')
            elif percent >= 90:
                fancy_print('So close, yet so far away...')
            elif percent >= 70:
                fancy_print('I know you can do better than that!')
            elif percent >= 50:
                fancy_print('Just over halfway there!')
            elif percent >= 30:
                fancy_print("Let's not speak of this score to anyone...")
            else:
                fancy_print("A monkey could've gotten a better score than that...")
            
            break

def fancy_print(str):
    """ Prints a fancy string """
    line = '═'*(len(str)+6)
    print('╔' + line + '╗')
    print('║ ~ ' + str + ' ~ ║')
    print('╚' + line + '╝')

def get_time_string(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)
    

if __name__ == '__main__':
    main()