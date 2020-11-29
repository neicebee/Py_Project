import pyautogui as pag, time, keyboard, sys

def get_png_location(sec):
    global count
    stop = int(time.time()) + sec

    count = 1
    while 1:
        if int(time.time()) >= stop:
            print(f"서버 과부하 우려로 스크립트 종료\n총 시도 횟수: {count}")
            sys.exit(-1)
        else:
            check = pag.locateOnScreen('attendance.PNG')
            if not check == None:
                i = pag.locateOnScreen('message_box.PNG')
                if not i == None:
                    pag.screenshot('new_message_box.PNG', region=list(i))
                    location = pag.locateCenterOnScreen('new_message_box.PNG')

                    break
                else:
                    print(f"{count}. 일치하는 이미지 없음")
                    count += 1
            else:
                print(f"{count}. 일치하는 이미지 없음")
                count += 1

        time.sleep(2)

    return location

def click_and_answer(location):
    pag.click(location)
    time.sleep(1)

    keyboard.write('네')
    keyboard.press('enter')

    print(f"Script Success!\n총 시도 횟수: {count}")

if __name__ == '__main__':
    error_count = 3

    while 1:
        try:
            sec = int(input("스크립트를 지속할 초(sec)를 입력하세요...(1 ~ 300)\n>>> "))

            if 1<=sec<=300:
                break
            else:
                error_count -= 1
                print(f"초(sec) 입력 오류\n남은 시도: {error_count}")
        except:
            error_count -= 1
            print(f"초(sec) 입력 오류\n남은 시도: {error_count}")
            pass

        if error_count == 0:
            print("Script Exit.")
            sys.exit(-1)

    click_and_answer(get_png_location(sec))