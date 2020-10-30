import random, sys, requests, fake_useragent
from bs4 import BeautifulSoup

def get_lottonum():
    lotto_num = []
    lotto_num.append(random.randint(1, 45))

    while(True):
        boolean = []
        a = random.randint(1, 45)

        for i in range(0, len(lotto_num)):
            boolean.append(get_True_False(lotto_num[i], a))

        if len(lotto_num) == 6:
            lotto_num.sort()
            break

        if False in boolean:
            continue
        else:
            lotto_num.append(a)

    bounsnum = get_bonusnum(lotto_num)

    return lotto_num, bounsnum

def get_True_False(lotto_num, a):

    if lotto_num == a:
        return False
    else:
        return True

def get_bonusnum(lotto_num):
    while(True):
        check = True
        b = random.randint(1, 45)

        for i in range(0, len(lotto_num)):
            if lotto_num[i] == b:
                check = False

        if check == True:
            bonusnum = b
            break

    return bonusnum

def get_last_lotto_num(params=None):
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
    ua = fake_useragent.UserAgent()

    hdr = {'User-Agent':str(ua.random)}

    req = requests.get(url, params=params, headers=hdr)
    print('[get_html] url:', req.url)
    print('[get_html] status_code:', req.status_code)

    if req.status_code != 200:
        print("Error!")
        sys.exit(1)

    soup = BeautifulSoup(req.text, 'html.parser')

    last_round = soup.find('div', {'class' : 'win_result'}).h4.strong.text

    last_round_date_check1 = soup.find('p', {'class' : 'desc'}).text.split("(")
    last_round_date_check2 = last_round_date_check1[1].split(")")
    last_round_date = last_round_date_check2[0]

    last_round_num_check = soup.find('div', {'class' : 'num win'}).p.text.split('\n')
    last_round_num = []
    for i in range(0, 7):
        if i == 0 or i == 7:
            continue
        last_round_num.append(int(last_round_num_check[i]))

    last_round_bonus_num = soup.find('div', {'class' : 'num bonus'}).p.text

    return last_round, last_round_date, last_round_num, last_round_bonus_num

if __name__ == '__main__':
    while(True):
        a = input("로또 번호를 생성하려면 1을 저번 당첨 로또 번호를 확인하려면 2를 종료하려면 0을 입력하세요...\n>>> ")

        if a == "1":
            lotto_num, bonusnum = get_lottonum()
            print(lotto_num)
            print(bonusnum)
        elif a == '2':
            last_round, last_round_date, last_round_num, last_round_bonus_num = get_last_lotto_num()
            print(last_round)
            print(last_round_date)
            print(last_round_num)
            print(last_round_bonus_num)
        elif a == '0':
            print("종료")
            sys.exit(0)
        else:
            print("다시 입력하십시오...")