import random
import sys
import getpass

def main():

    print("Game Start!\nPlease select the Mode...\n")

    print("=======================")
    print("|   1. Easy           |")
    print("|   2. Normal         |")
    print("|   3. Hard           |")
    print("|   4. Hell           |")
    print("|   5. exit           |")
    print("=======================")

    ran_num, dif = get_ran()

    if dif == "1":
        print(ran_num)
        gamecnt = 20
        easyandnormal_game(ran_num, gamecnt)
    if dif == "2":
        print(ran_num)
        gamecnt = 10
        easyandnormal_game(ran_num, gamecnt)
    if dif == "3":
        print(ran_num)
        gamecnt = 10
        hardandhell_game(ran_num, gamecnt)
    if dif == "4":
        print(ran_num)
        gamecnt = 5
        hardandhell_game(ran_num, gamecnt)

def get_ran():
    while(True):
        dif = input(">>> ")

        if dif == "1":
            print("You have selected the Easy mode...")
            print("Hint: 랜덤 숫자가 1~100까지로 설정됩니다. 기회는 20번입니다.")
            ran_num = random.randrange(1, 100)
            break
        elif dif == "2":
            print("You have selected the Normal mode...")
            print("Hint: 랜덤 숫자가 1~1000까지로 설정됩니다. 기회는 10번입니다.")
            ran_num = random.randrange(1, 1000)
            break
        elif dif == "3":
            print("You have selected the Hard mode...")
            print("Hint: 랜덤 숫자가 1~10000까지로 설정됩니다. 자신이 입력한 숫자는 보이지 않습니다. 기회는 10번입니다.")
            ran_num = random.randrange(1, 10000)
            break
        elif dif == "4":
            print("You have selected the Hell mode...")
            print("Hint: 랜덤 숫자가 1~100000까지로 설정됩니다. 자신이 입력한 숫자는 보이지 않습니다. 기회는 5번입니다.")
            ran_num = random.randrange(1, 100000)
            break
        elif dif == "5":
            print("Game Exit!")
            sys.exit(0)
        else:
            print("Error! Please enter the correct Mode number...")

    return ran_num, dif

def easyandnormal_game(ran_num, gamecnt):

    cnt = 0

    while(1):
        try:
            my_num = int(input("숫자를 입력하세요 >>> "))
        except ValueError:
            print("Error!")
            sys.exit(1)
        except:
            continue

        cnt = cnt + 1
        print(cnt)

        if cnt == gamecnt:
            print("기회 초과! Game Over...")
            break
        elif ran_num == my_num:
            print(str(cnt) + "번의 시도로 Success!")
            break
        elif ran_num > my_num:
            print("UP!")
        else:
            print("DOWN!")

def hardandhell_game(ran_num, gamecnt):

    cnt = 0

    while (1):
        try:
            my_num = int(getpass.getpass("숫자를 입력하세요 >>> "))
        except ValueError:
            print("Error!")
            sys.exit(1)
        except:
            continue

        cnt = cnt + 1
        print(cnt)

        if cnt == gamecnt:
            print("기회 초과! Game Over...")
            break
        elif ran_num == my_num:
            print(str(cnt) + "번의 시도로 Success!")
            break
        elif ran_num > my_num:
            print("UP!")
        else:
            print("DOWN!")

if __name__ == '__main__':
    main()
