
import random

from data.questions import QUESTIONS
from data.answers import ANSWERS

def main():

    correct_counter = 0
    incorrect_counter = 0

    total_questions = len(ANSWERS)
    fancy_print('Welcome to VEFT QuizUp!')
    print('There are a total of ' + str(total_questions) + ' questions in this quiz!')
    print('Quit at any time by entering any character or an unavailable integer.')
    print('Good luck!\n')

    answered_questions = list()

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

        answer = input('--> ')

        try:
            val = int(answer)-1
        except ValueError:
            break

        if val >= len(options):
            break
        
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
            fancy_print('You finished all the questions with ' + str(correct_counter) + '/' + str(correct_counter+incorrect_counter) + ' correct answers. ('+ str(percent) + '%)')
            break

def fancy_print(str):
    """ Prints a fancy string """
    line = '═'*(len(str)+6)
    print('╔' + line + '╗')
    print('║ ~ ' + str + ' ~ ║')
    print('╚' + line + '╝')
    

if __name__ == '__main__':
    main()