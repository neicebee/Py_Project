import pyautogui as pag, time, keyboard, sys

def pick_scene(position):
    count = 1

    while 1:
        pick_image_1 = pag.locateOnScreen('lolpick/pick1.PNG')

        if not pick_image_1 == None:
            chatting_image = pag.locateOnScreen('lolpick/chatting.PNG')
            if not chatting_image == None:
                pag.screenshot('lolpick/chatting_img.PNG', region=list(chatting_image))
                chatting = pag.locateCenterOnScreen('lolpick/chatting_img.PNG')

                for i in range(10):
                    pag.click(chatting)
                    keyboard.write(position)
                    keyboard.press('enter')
                
                value = 'Success'
                break
            else:
                print("Script Error!")
                value = 'Fail'
                break
        else:
            print(f'{count} 시도')

        count += 1

    return value

if __name__ == '__main__':
    stop_script = time.time() + 15
    print("+++++++++++++++++++++++++++++++++")
    print("+ 포지션 입력 후 키 입력")
    print("+ Start : [키 입력")
    print("+ Exit : ]키 입력")
    print("+ 15초 동안 키 입력 없으면 종료")
    print("+++++++++++++++++++++++++++++++++")
    position = input("포지션 입력: ")

    while 1:
        if keyboard.is_pressed('['):
            print("Start!")
            value = pick_scene(position)
            if value == 'Success':
                print("스크립트 정상 종료")
            else:
                print("스크립트 비정상 종료")
            break

        if keyboard.is_pressed(']'):
            print("Exit!")
            break

        if time.time() > stop_script:
            print("Time Over!")
            sys.exit(-1)

    sys.exit(0)