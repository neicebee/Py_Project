import requests
import fake_useragent
from bs4 import BeautifulSoup
import sys

ua = fake_useragent.UserAgent()
user_agent = ua.random

def get_url(username):
    url = "http://fow.kr/find/" + username

    return url

def get_getreq(url):
    req = requests.get(url)

    if req.status_code != 200:
        print("Web Error!")
        sys.exit(1)

    soup = BeautifulSoup(req.text, 'html.parser')

    return soup

def get_summoner_presence_and_refresh_bool(soup):
    try:
        refresh_check = soup.find('div', {'class': 'profile'})

        if "갱신불가" in refresh_check.text:
            return False
        elif "갱신가능" in refresh_check.text:
            return True
    except:
        print("그런 이름의 소환사는 없습니다.")
        sys.exit(1)

def get_sid(soup):
    sid_check = soup.find('a', {'class' : 'sbtn refresh_sid'})
    sid = sid_check.get('sid')

    return sid

def post_data(username, sid, main_url):
    hdr = {'User-Agent': str(user_agent)}
    url = "http://fow.kr/api_new_ajax.php"

    data = {
        'action' : 'refresh',
        'name' : username,
        'sid' : sid
    }

    refresh_session = requests.post(url, headers=hdr, data=data)

    if refresh_session.status_code != 200:
        print("Error!")
        sys.exit(1)
    else:
        print("Update!")
        soup = get_getreq(main_url)

        return soup

def post_game_check(summoner_sid, summoner_name):
    hdr = {'User-Agent': str(user_agent)}
    url = "http://fow.kr/api_new_ajax.php"
    data = {
        'action': 'spec',
        'sid': summoner_sid,
        'iname': summoner_name
    }

    game_check_session = requests.post(url, headers=hdr, data=data)

    if game_check_session.status_code != 200:
        print("Error!")
        sys.exit(1)
    else:
        print("Done!")
        game_check = BeautifulSoup(game_check_session.text, 'html.parser')

        return game_check

def parsing(soup):
    # 소환사 이름 파싱
    summoner_name = soup.find('span', {'class' : 'username'}).get('iname')

    # 소환사 정보 파싱
    summoner_info_list = soup.select("body > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div.profile > div:nth-child(3)")
    summoner_info = []
    summoner_info_check = ""

    # 소환사 솔로 리그 티어 파싱
    summoner_unranked_check = soup.find('div', {'class' : 'table_summary'})
    summoner_tier_list = soup.select("body > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div.table_summary > div:nth-child(2)")
    summoner_tier = []
    summoner_tier_check = ""

    # 소환사 자유 리그 티어 파싱
    summoner_free_tier_list = soup.select("body > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div.table_summary > div:nth-child(4)")
    summoner_free_tier = []
    summoner_free_tier_check = ""

    # 현재 게임 중 파싱
    summoner_sid = soup.find('div', {'class' : 'acc_info'}).get('sid')
    game_check_list = post_game_check(summoner_sid, summoner_name)
    game_check = game_check_list.text

    # 현 시즌 전체 랭크 모스트 3까지 파싱 후 정리
    try:
        most_champ_all_info_check = soup.find('div', {'class' : 'rankchamp_S10_div rankchamp_S10_div_all'}).thead.text.split("\n")
        most_champ_all_info = []
        most_champ_all_list_1 = []
        most_champ_all_list_2 = []
        most_champ_all_list_3 = []

        for mcai in range(0, len(most_champ_all_info_check)):
            if most_champ_all_info_check[mcai] == "":
                continue
            else:
                most_champ_all_info.append(most_champ_all_info_check[mcai])

        for num in range(1, 4):
            most_champ_all_list_check = soup.select("body > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div.rankchamp_S10_div.rankchamp_S10_div_all > table > tbody > tr:nth-child({})".format(num))[0].text.split("\n")

            for mcal in range(0, len(most_champ_all_list_check)):
                if most_champ_all_list_check[mcal] == "":
                    continue
                else:
                    if num == 1:
                        most_champ_all_list_1.append(most_champ_all_list_check[mcal].strip())
                    elif num == 2:
                        most_champ_all_list_2.append(most_champ_all_list_check[mcal].strip())
                    elif num == 3:
                        most_champ_all_list_3.append(most_champ_all_list_check[mcal].strip())

        most_champ_all = {
            'most champ all info' : most_champ_all_info,
            '1' : most_champ_all_list_1,
            '2' : most_champ_all_list_2,
            '3' : most_champ_all_list_3
        }

    except:
        most_champ_all = ""
        msg1 = summoner_name + " 소환사는 현 시즌 랭크 정보가 없습니다."
        most_champ_all = msg1

    # 전 시즌 전체 랭크 모스트 3까지 파싱 후 정리
    try:
        last_most_champ_all_info_check = soup.find('div', {'class': 'rankchamp_div rankchamp_div_all'}).thead.text.split("\n")
        last_most_champ_all_info = []
        last_most_champ_all_list_1 = []
        last_most_champ_all_list_2 = []
        last_most_champ_all_list_3 = []

        for lmcai in range(0, len(last_most_champ_all_info_check)):
            if last_most_champ_all_info_check[lmcai] == "":
                continue
            else:
                last_most_champ_all_info.append(last_most_champ_all_info_check[lmcai])

        for num2 in range(1, 4):
            last_most_champ_all_list_check = soup.select("body > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div.rankchamp_div.rankchamp_div_all > table > tbody > tr:nth-child({})".format(num2))[0].text.split("\n")

            for lmcal in range(0, len(last_most_champ_all_list_check)):
                if last_most_champ_all_list_check[lmcal] == "":
                    continue
                else:
                    if num2 == 1:
                        last_most_champ_all_list_1.append(last_most_champ_all_list_check[lmcal].strip())
                    elif num2 == 2:
                        last_most_champ_all_list_2.append(last_most_champ_all_list_check[lmcal].strip())
                    elif num2 == 3:
                        last_most_champ_all_list_3.append(last_most_champ_all_list_check[lmcal].strip())

        last_most_champ_all = {
            'last most champ all info' : last_most_champ_all_info,
            '1' : last_most_champ_all_list_1,
            '2' : last_most_champ_all_list_2,
            '3' : last_most_champ_all_list_3
        }
    except:
        last_most_champ_all = ""
        msg2 = summoner_name + " 소환사는 전 시즌 랭크 정보가 없습니다."
        last_most_champ_all = msg2

    # 최근 전체 30 경기 요약 파싱
    try:
        game_play_info_check = soup.find('div', {'class' : 'detail_toggle'}).text.split("\n")
        game_play_info = []

        for gpi in range(0, len(game_play_info_check)):
            if game_play_info_check[gpi] == "":
                continue
            else:
                game_play_info.append(game_play_info_check[gpi].strip())
    except:
        game_play_info = []
        msg3 = summoner_name + " 소환사는 최근 30게임 정보가 없습니다."
        game_play_info.append(msg3)

    # 소환사 정보 파싱 내용 정리
    for check in summoner_info_list:
        summoner_info_check = check.text.split("\n")

    for info in range(0, len(summoner_info_check)):
        if summoner_info_check[info] == "":
            continue
        else:
            summoner_info.append(summoner_info_check[info])

    # 소환사 리그 티어 내용 정리
    if summoner_unranked_check == None:
        summoner_tier.append(summoner_name + " 소환사 님은 솔로 랭크 정보가 없습니다.")
        summoner_free_tier.append(summoner_name + " 소환사 님은 자유 랭크 정보가 없습니다.")
    else:
        for tier in summoner_tier_list:
            summoner_tier_check = tier.text.strip().split("\n")
        for tier_check in range(0, len(summoner_tier_check)):
            if summoner_tier_check[tier_check] == "":
                continue
            else:
                summoner_tier.append(summoner_tier_check[tier_check].strip())

        for free_tier in summoner_free_tier_list:
            summoner_free_tier_check = free_tier.text.strip().split("\n")
        for free_tier_check in range(0, len(summoner_free_tier_check)):
            if summoner_free_tier_check[free_tier_check] == "":
                continue
            else:
                summoner_free_tier.append(summoner_free_tier_check[free_tier_check].strip())

    # 현재 게임 중 내용 정리
    if "님은 게임 중이 아닙니다." not in game_check:
        game_check_url = "http://fow.kr/find/" + summoner_name
        game = "< " + summoner_name + " >" + "님은 현재 게임 중 입니다.\n다음 링크로 들어가 상세 정보를 확인하십시오.\n" + game_check_url
    else:
        game = game_check

    last_msg = msg_rt(summoner_name, summoner_info, summoner_tier, summoner_free_tier, game, most_champ_all, last_most_champ_all, game_play_info)

    return last_msg

def msg_rt(username, summoner_info, summoner_tier, summoner_free_tier, game, most_champ_all, last_most_champ_all, game_play_info):
    if str(type(most_champ_all)) == "<class 'dict'>" and str(type(last_most_champ_all)) == "<class 'dict'>":
        msg1 = "소환사 닉네임: " + username + '\n'

        msg2 = ""
        for si in range(0, len(summoner_info)):
            msg2 = msg2 + summoner_info[si] + '\n'

        msg3 = ""
        for st in range(0, len(summoner_tier)):
            msg3 = msg3 + summoner_tier[st] + '\n'

        msg4 = ""
        for sft in range(0, len(summoner_free_tier)):
            msg4 = msg4 + summoner_free_tier[sft] + '\n'

        msg5 = game + '\n'

        msg6_check = most_champ_all['most champ all info']
        msg6 = ""
        for mca in range(0, 4):
            msg6 = msg6 + msg6_check[mca] + " "

        msg7_check = most_champ_all['1']
        msg7 = ""
        for mca_1 in range(0, 4):
            msg7 = msg7 + msg7_check[mca_1] + " "

        msg8_check = most_champ_all['2']
        msg8 = ""
        for mca_2 in range(0, 4):
            msg8 = msg8 + msg8_check[mca_2] + " "

        msg9_check = most_champ_all['3']
        msg9 = ""
        for mca_3 in range(0, 4):
            msg9 = msg9 + msg9_check[mca_3] + " "

        msg10_check = last_most_champ_all['last most champ all info']
        msg10 = ""
        for lmca in range(0, 4):
            msg10 = msg10 + msg10_check[lmca] + " "

        msg11_check = last_most_champ_all['1']
        msg11 = ""
        for lmca_1 in range(0, 4):
            msg11 = msg11 + msg11_check[lmca_1] + " "

        msg12_check = last_most_champ_all['2']
        msg12 = ""
        for lmca_2 in range(0, 4):
            msg12 = msg12 + msg12_check[lmca_2] + " "

        msg13_check = last_most_champ_all['3']
        msg13 = ""
        for lmca_3 in range(0, 4):
            msg13 = msg13 + msg13_check[lmca_3] + " "

        msg14 = "최근 30게임 평가 (전체)\n"
        for gpi in range(0, len(game_play_info)):
            msg14 = msg14 + game_play_info[gpi] + " "

        msg = msg1 + '\n' + msg2 + '\n' + msg3 + '\n' + msg4 + '\n' + msg5 + '\n' + msg6 + '\n' + msg7 + '\n' + msg8 + '\n' + msg9 + '\n\n' + msg10 + '\n' + msg11 + '\n' + msg12 + '\n' + msg13 + '\n\n' + msg14

        return msg
    elif str(type(most_champ_all)) == "<class 'dict'>" and str(type(last_most_champ_all)) == "<class 'str'>":
        msg1 = "소환사 닉네임: " + username + '\n'

        msg2 = ""
        for si in range(0, len(summoner_info)):
            msg2 = msg2 + summoner_info[si] + '\n'

        msg3 = ""
        for st in range(0, len(summoner_tier)):
            msg3 = msg3 + summoner_tier[st] + '\n'

        msg4 = ""
        for sft in range(0, len(summoner_free_tier)):
            msg4 = msg4 + summoner_free_tier[sft] + '\n'

        msg5 = game + '\n'

        msg6_check = most_champ_all['most champ all info']
        msg6 = ""
        for mca in range(0, 4):
            msg6 = msg6 + msg6_check[mca] + " "

        msg7_check = most_champ_all['1']
        msg7 = ""
        for mca_1 in range(0, 4):
            msg7 = msg7 + msg7_check[mca_1] + " "

        msg8_check = most_champ_all['2']
        msg8 = ""
        for mca_2 in range(0, 4):
            msg8 = msg8 + msg8_check[mca_2] + " "

        msg9_check = most_champ_all['3']
        msg9 = ""
        for mca_3 in range(0, 4):
            msg9 = msg9 + msg9_check[mca_3] + " "

        msg10 = last_most_champ_all

        msg11 = "최근 30게임 평가 (전체)\n"
        for gpi in range(0, len(game_play_info)):
            msg11 = msg11 + game_play_info[gpi] + " "

        msg = msg1 + '\n' + msg2 + '\n' + msg3 + '\n' + msg4 + '\n' + msg5 + '\n' + msg6 + '\n' + msg7 + '\n' + msg8 + '\n' + msg9 + '\n\n' + msg10 + '\n\n' + msg11

        return msg
    elif str(type(most_champ_all)) == "<class 'str'>" and str(type(last_most_champ_all)) == "<class 'dict'>":
        msg1 = "소환사 닉네임: " + username + '\n'

        msg2 = ""
        for si in range(0, len(summoner_info)):
            msg2 = msg2 + summoner_info[si] + '\n'

        msg3 = ""
        for st in range(0, len(summoner_tier)):
            msg3 = msg3 + summoner_tier[st] + '\n'

        msg4 = ""
        for sft in range(0, len(summoner_free_tier)):
            msg4 = msg4 + summoner_free_tier[sft] + '\n'

        msg5 = game + '\n'

        msg6 = most_champ_all

        msg7_check = last_most_champ_all['last most champ all info']
        msg7 = ""
        for lmca in range(0, 4):
            msg7 = msg7 + msg7_check[lmca] + " "

        msg8_check = last_most_champ_all['1']
        msg8 = ""
        for lmca_1 in range(0, 4):
            msg8 = msg8 + msg8_check[lmca_1] + " "

        msg9_check = last_most_champ_all['2']
        msg9 = ""
        for lmca_2 in range(0, 4):
            msg9 = msg9 + msg9_check[lmca_2] + " "

        msg10_check = last_most_champ_all['3']
        msg10 = ""
        for lmca_3 in range(0, 4):
            msg10 = msg10 + msg10_check[lmca_3] + " "

        msg11 = "최근 30게임 평가 (전체)\n"
        for gpi in range(0, len(game_play_info)):
            msg11 = msg11 + game_play_info[gpi] + " "

        msg = msg1 + '\n' + msg2 + '\n' + msg3 + '\n' + msg4 + '\n' + msg5 + '\n\n' + msg6 + '\n' + msg7 + '\n' + msg8 + '\n' + msg9 + '\n\n' + msg10 + '\n\n' + msg11

        return msg
    elif str(type(most_champ_all)) == "<class 'str'>" and str(type(last_most_champ_all)) == "<class 'str'>":
        msg1 = "소환사 닉네임: " + username + '\n'

        msg2 = ""
        for si in range(0, len(summoner_info)):
            msg2 = msg2 + summoner_info[si] + '\n'

        msg3 = ""
        for st in range(0, len(summoner_tier)):
            msg3 = msg3 + summoner_tier[st] + '\n'

        msg4 = ""
        for sft in range(0, len(summoner_free_tier)):
            msg4 = msg4 + summoner_free_tier[sft] + '\n'

        msg5 = game + '\n'

        msg6 = most_champ_all

        msg7 = last_most_champ_all

        msg8 = "최근 30게임 평가 (전체)\n"
        for gpi in range(0, len(game_play_info)):
            msg8 = msg8 + game_play_info[gpi] + " "

        msg = msg1 + '\n' + msg2 + '\n' + msg3 + '\n' + msg4 + '\n' + msg5 + '\n' + msg6 + '\n\n' + msg7 + '\n\n' + msg8

        return msg
    else:
        msg = "Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        return msg

if __name__ == '__main__':
    answer = ['Y', 'y', 'N', 'n']

    while True:
        username = input("소환사 닉네임을 입력해주세요.\n>>> ")
        url = get_url(username)

        getreq = get_getreq(url)
        refresh_bool = get_summoner_presence_and_refresh_bool(getreq)

        print(refresh_bool)

        if refresh_bool == True:
            sid = get_sid(getreq)
            soup = post_data(username, sid, url)
            msg = parsing(soup)
            print(msg)
        else:
            msg = parsing(getreq)
            print(msg)

        while True:
            re_search_answer = input("다른 소환사 닉네임을 검색하시겠습니까?(Y/N)")

            if not re_search_answer in answer:
                print("정확한 값을 반환해주세요.")
                continue
            else:
                break

        if re_search_answer == answer[2] or re_search_answer == answer[3]:
            print("Script End!")
            break
        else:
            continue