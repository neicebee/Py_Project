import sys

# 명령어 체크 메서드
def check_command():
    try:
        '''
        만약 
        python memo.py -a hello world
        라는 명령어를 입력했을 때
        sys.argv[0]은 memo.py이며
        sys.argv[1]은 -a
        즉 공백으로 리스트를 나눈다고 보면 된다.
        '''
        option = sys.argv[1]

        return option
    except:
        return False

# 메모 추가 메서드
def write_memo(memo):
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write("\n")
    f.close()
    print("Write Done!")

# 메모 읽기 메서드
def read_memo():
    f = open('memo.txt')
    memo = f.read()
    f.close()

    if memo == "":
        print("내용이 없습니다.")
    else:
        print(memo)

    print("Read Done!")

# 메모 삭제 메서드
def delete_memo():
    f = open('memo.txt', 'w')
    f.close()
    print("Delete Done!")

if __name__ == '__main__':
    option = check_command()

    if option == "-w":
        memo = ""
        try:
            # -w 다음 문자열들을 공백 상관없이 메모 처리하는 코드
            for i in range(2, len(sys.argv)):
                memo = memo + sys.argv[i] + " "
            write_memo(memo.strip())
        except:
            print("-w 명령어 뒤에 메모에 추가할 문자열이 필요합니다.")
    elif option == "-r":
        read_memo()
    elif option == '-d':
        delete_memo()
    else:
        print("Command Error!")