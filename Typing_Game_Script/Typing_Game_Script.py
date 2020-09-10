import time
import random
import sys

word = ['programming', 'python', 'thread', 'time', 'random', 'library', 'class', 'method', 'pandas', 'tensorflow']

def game():
    check_question = []
    count = 0
    fail_count = 0

    start = time.time()
    while count < 5:
        while True:
            question = random.choice(word)
            if not count == 0:
                if question in check_question:
                    continue
                else:
                    break
            else:
                break

        check_question.append(question)
        print("{}번".format(count + 1))
        print(question)
        answer = input()

        if answer == question:
            print("<Pass!>")
            count += 1
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
    answer = ['Y', 'y', 'N', 'n']

    while True:
        print("게임시작>>> Enter!")
        x = input()
        if x == "":
            runtime = game()
        else:
            print("Error!")
            sys.exit(1)

        print("Runtime: " + runtime + "초")

        while True:
            player_answer = input("Regame?(Y/N)")

            if not player_answer in answer:
                print("정확한 값을 전달해주세요")
                continue
            else:
                break

        if player_answer == answer[2] or player_answer == answer[3]:
            print("Game Over!")
            break
        else:
            continue
