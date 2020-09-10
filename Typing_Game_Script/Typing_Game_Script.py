import time
import random
import sys

word = ['programming', 'python', 'thread', 'time', 'random', 'library', 'class', 'method', 'pandas', 'tensorflow']
check_question = []

def game():
    count = 0
    fail_count = 0

    start = time.time()
    question = random.choice(word)
    while count < 5:
        check_question.append(question)
        print("{}번".format(count + 1))
        print(question)
        answer = input()

        if answer == question:
            print("<Pass!>")
            count += 1
            question = random.choice(word)

            for i in range(0, len(check_question)):
                if check_question[i] == question:
                    question = random.choice(word)
        else:
            print("<Fail!>")
            fail_count += 1

        if fail_count == 3:
            print("Fail 3번 누적\nGame Over!")
            break

    end = time.time()
    runtime = format(end - start, ".2f")

    return runtime

if __name__ == '__main__':
    print("게임시작>>> Enter!")
    x = input()
    if x == "":
        runtime = game()
    else:
        print("Error!")
        sys.exit(1)

    print("Runtime: " + runtime + "초")
