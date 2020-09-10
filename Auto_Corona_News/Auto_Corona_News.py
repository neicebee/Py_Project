import sys
import json
from bs4 import BeautifulSoup
import requests
import time
import threading

TotalC = []
TotalLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty"

SeoulC = []
SeoulLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%84%9C%EC%9A%B8&where=news&ie=utf8&sm=nws_hty"

SejongC = []
SejongLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%84%B8%EC%A2%85%EC%8B%9C&where=news&ie=utf8&sm=nws_hty"

BusanC = []
BusanLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%B6%80%EC%82%B0&where=news&ie=utf8&sm=nws_hty"

DaeguC = []
DaeguLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%8C%80%EA%B5%AC&where=news&ie=utf8&sm=nws_hty"

GwangjuC = []
GwangjuLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EA%B4%91%EC%A3%BC&where=news&ie=utf8&sm=nws_hty"

IncheonC = []
IncheonLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%9D%B8%EC%B2%9C&where=news&ie=utf8&sm=nws_hty"

DaejeonC = []
DaejeonLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%8C%80%EC%A0%84&where=news&ie=utf8&sm=nws_hty"

UlsanC = []
UlsanLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%9A%B8%EC%82%B0&where=news&ie=utf8&sm=nws_hty"

GyeonggiC = []
GyeonggiLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EA%B2%BD%EA%B8%B0%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

GangwonC = []
GangwonLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EA%B0%95%EC%9B%90%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

ChungbukC = []
ChungbukLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

ChungnamC = []
ChungnamLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

JeonbukC = []
JeonbukLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%A0%84%EB%9D%BC%EB%B6%81%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

JeonnamC = []
JeonnamLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%A0%84%EB%9D%BC%EB%82%A8%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

GyeongbukC = []
GyeongbukLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

GyeongnamC = []
GyeongnamLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

JejuC = []
JejuLink = "https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%A0%9C%EC%A3%BC%EB%8F%84&where=news&ie=utf8&sm=nws_hty"

hdr = {'User-Agent': (
        'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')}

def TotalNewsGet(Link):
    url = Link
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    ErrorCheck = soup.find('div', {'id' : 'notfound'})

    Object = ""
    Title = []
    Press = []
    Time = []
    Hyperlink = []

    if not 'None' in str(ErrorCheck):
        print("Error! 개발자에게 문의하십시오.")
        sys.exit(1)
    else:
        for i in soup.select('h1[class=blind]'):
            LocationInfo = i.text
            Object1 = LocationInfo.split(" ")
            if len(Object1) == 3:
                Object = "종합"
            else:
                Object = Object1[1]

            print(Object)

        checknews = soup.find('ul', 'type01')

        for i in range(0, 100):
            # 뉴스 타이틀 출력을 위한 체크 단계
            news1 = checknews.find('li', {'id' : 'sp_nws{}'.format(i)})

            # sp_nws의 숫자가 일정하지 않기 때문에 걸러주는 단계
            if str(news1) == "None":
                continue

            news2 = news1.dl.dt.a
            newsinfo1 = news1.dl.dd

            # 에러 체크 단계
            if str(news2) == "None" or str(newsinfo1) == "None":
                print("Error! 개발자에게 문의하십시오.")
                sys.exit(1)
            else:
                # 타이틀 및 하이퍼링크 추출
                news = news2.get('title')
                Title.append(news)

                newshref = news2.get('href')
                Hyperlink.append(newshref)

                newsinfo2 = newsinfo1.text

                # 신문사 및 기사 시간 추출
                if "언론사 선정" in newsinfo2:
                    newsinfo3 = newsinfo2.split("언론사 선정")
                    newsinfo = newsinfo3[0]
                    Press.append(newsinfo)

                    newsinfo4 = newsinfo3[1].split("  ")
                    newstime = newsinfo4[1]
                    Time.append(newstime)
                else:
                    newsinfo3 = newsinfo2.split("  ")

                    newsinfo = newsinfo3[0]
                    Press.append(newsinfo)

                    newstime = newsinfo3[1]
                    Time.append(newstime)

    print(LocationInfo + " Crawling Success!")
    makedict(Object, Title, Press, Time, Hyperlink)

def makedict(Object, Title, Press, Time, Hyperlink):
    if Object == "종합":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                TotalC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "서울":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                SeoulC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "세종시":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                SejongC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "부산":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                BusanC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "대구":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                DaeguC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "대전":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                DaejeonC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "인천":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                IncheonC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "광주":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                GwangjuC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "울산":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                UlsanC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "경기도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
               GyeonggiC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "강원도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                GangwonC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "충청북도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                ChungbukC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "충청남도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                ChungnamC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "전라북도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                JeonbukC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "전라남도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                JeonnamC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "경상북도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                GyeongbukC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "경상남도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                GyeongnamC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    elif Object == "제주도":
        if len(Title) == len(Press) == len(Time) == len(Hyperlink):
            for i in range(0, len(Title)):
                JejuC.append({"Title" : Title[i], "Press" : Press[i], "Time" : Time[i], "Link" : Hyperlink[i]})
        else:
            print("Error! 개발자에게 문의하세요!")
            sys.exit(1)

    else:
        print("Error! 개발자에게 문의하세요!")
        sys.exit(1)

    print("Make dict Success!")
    print("=====================")

def makejsonfile():
    finalNews = {
        "Type" : "success",
        "Message" : "성공",
        "종합" : TotalC,
        "서울" : SeoulC,
        "세종" : SejongC,
        "부산" : BusanC,
        "대구" : DaeguC,
        "대전" : DaejeonC,
        "인천" : IncheonC,
        "광주" : GwangjuC,
        "울산" : UlsanC,
        "경기도" : GyeonggiC,
        "강원도" : GangwonC,
        "충청북도" : ChungbukC,
        "충청남도" : ChungnamC,
        "전라북도" : JeonbukC,
        "전라남도" : JeonnamC,
        "경상북도" : GyeongbukC,
        "경상남도" : GyeongnamC,
        "제주도" : JejuC
    }

    with open('CoronaNews.json', 'w', encoding='utf-8') as make_file:
        json.dump(finalNews, make_file, ensure_ascii=False)

    make_file.close()

    print("Jsonfile make Success!")

def thread_run():
    print("Start Script!\n", "=====", time.ctime(), "=====")

    TotalNewsGet(TotalLink)
    TotalNewsGet(SeoulLink)
    TotalNewsGet(SejongLink)
    TotalNewsGet(BusanLink)
    TotalNewsGet(DaeguLink)
    TotalNewsGet(DaejeonLink)
    TotalNewsGet(IncheonLink)
    TotalNewsGet(GwangjuLink)
    TotalNewsGet(UlsanLink)
    TotalNewsGet(GyeonggiLink)
    TotalNewsGet(GangwonLink)
    TotalNewsGet(ChungbukLink)
    TotalNewsGet(ChungnamLink)
    TotalNewsGet(JeonbukLink)
    TotalNewsGet(JeonnamLink)
    TotalNewsGet(GyeongbukLink)
    TotalNewsGet(GyeongnamLink)
    TotalNewsGet(JejuLink)

    makejsonfile()

    print("Script Success!")

    threading.Timer(120, thread_run).start()

if __name__ == '__main__':
    thread_run()