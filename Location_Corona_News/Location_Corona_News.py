import sys
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd

#리스트 선언
location_text = ""
title_text=[]
link_text=[]
time_text=[]
press_text=[]
result={}

#엑셀로 저장하기 위한 변수
RESULT_PATH ='C:/News Execl/'  #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기

def main():
    location = input("지역을 입력하세요.\n>>> ")
    finallocation = location + "+코로나"
    crawler(finallocation)

def crawler(finallocation):
    url = 'https://search.naver.com/search.naver?query=' + finallocation + '&where=news&ie=utf8&sm=nws_hty'
    hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')}
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    ErrorCheck = soup.find('div', {'id' : 'notfound'})

    if not 'None' in str(ErrorCheck):
        print("Error! 지역 검색 오류! 정확한 지역 이름을 입력하십시오.")
        sys.exit(1)
    else:
        # 지역 뉴스검색 결과 텍스트
        for i in soup.select('h1[class=blind]'):
            LocationInfo = i.text
            location_text = LocationInfo

        # 뉴스 체크
        checknews = soup.find('ul', 'type01')

        print("* " + LocationInfo + " *\n=============================")

        # 뉴스
        for i in range(0, 100):
            # 뉴스 타이틀 출력을 위한 체크 단계
            firstnews1 = checknews.find('li', {'id' : 'sp_nws{}'.format(i)})

            # sp_nws의 숫자가 일정하지 않기 때문에 걸러주는 단계
            if str(firstnews1) == "None":
                continue

            firstnews2 = firstnews1.dl.dt.a
            firstnewsinfo1 = firstnews1.dl.dd

            # 에러 체크 단계
            if str(firstnews2) == "None" or str(firstnewsinfo1) == "None":
                print("Error! 개발자에게 문의하십시오.")
                sys.exit(1)
            else:
                # 타이틀 및 하이퍼링크 추출
                firstnews = firstnews2.get('title')
                title_text.append(firstnews)

                firstnewshref = firstnews2.get('href')
                link_text.append(firstnewshref)

                firstnewsinfo2 = firstnewsinfo1.text

                # 신문사 및 기사 시간 추출
                if "언론사 선정" in firstnewsinfo2:
                    firstnewsinfo3 = firstnewsinfo2.split("언론사 선정")
                    firstnewsinfo = firstnewsinfo3[0]
                    press_text.append(firstnewsinfo)

                    firstnewsinfo4 = firstnewsinfo3[1].split("  ")
                    firstnewstime = firstnewsinfo4[1]
                    time_text.append(firstnewstime)
                else:
                    firstnewsinfo3 = firstnewsinfo2.split("  ")

                    firstnewsinfo = firstnewsinfo3[0]
                    press_text.append(firstnewsinfo)

                    firstnewstime = firstnewsinfo3[1]
                    time_text.append(firstnewstime)

            print(firstnews + " - " + firstnewsinfo + " - " + firstnewstime)
            print(firstnewshref + "\n")

        result = {"time": time_text, "title": title_text, "press": press_text, "link": link_text}

        df = pd.DataFrame(result)  # df로 변환

    outputFileName = '%s(%s.%s.%s %s시 %s분 %s초).xlsx' % (location_text, now.year, now.month, now.day, now.hour, now.minute, now.second)
    df.to_excel(RESULT_PATH + outputFileName, sheet_name='sheet1')

main()