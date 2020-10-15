"""
네이버 로그인 js 함수 과정
confirmSubmit() -> encryptIdPw() -> getLenChar()

네이버 로그인 시 소프트웨어에 의한 값 입력 혹은 마우스 및 키패드 동작 현상이 없으면 captcha가 실행
마우스 및 키패드 동작 로그를 가진 무언가를 찾아서 post로 보내줘야함 => bvsd
네이버 로그인 시 captcha 무력화 방법 => bvsd 값을 post_data에 삽입해야함
"""

import uuid
import requests
import rsa, sys
import lzstring

def encrypt(keys2, id, pw):
    sessionkey, keyname, e_value, n_value = keys2.split(',')

    # encpw의 값 => sessionkey 길이의 아스키 문자값 + sessionkey + id 길이의 아스키 문자값 + id + pw 길의의 아스키 문자값 + pw
    enctext = enc_source([sessionkey, id, pw]).encode()

    # int(value => int로 변환할 값, base => 진수)
    e, n = int(e_value, 16), int(n_value, 16)

    pub_key = rsa.PublicKey(e, n)

    return keyname, rsa.encrypt(enctext, pub_key)

def enc_source(enc_list):
    return "".join([chr(len(a)) + a for a in enc_list])

def n_session(id, pw):
    keys2_nhn = requests.get("https://nid.naver.com/login/ext/keys2.nhn").content.decode('utf-8')

    return encrypt(keys2_nhn, id, pw)

def sign_in_naver(encnm, encpw):
    s = requests.Session()

    hdr = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    # 네이버 로그인 captcha 무력화 주요 코드
    # uuid => universally unique identifier : 범용 고유 식별자
    """
    uuid1(node=None, clock_seq=None) => 호스트ID, 시퀀스, 현재 시간을 기준으로 uuid 생성
    uuid3(namespace, name) => 네임스페이스 uuid와 이름의 md5 해시에서 uuid 생성
    uuid4() => 랜덤 uuid 생성
    uuid5() => 네임스페이스 uuid와 이름의 sha-1 해시에서 uuid 생성
    """
    bvsd_uuid = uuid.uuid4()

    """
    소프트웨어로 키를 입력하거나 마우스 이동이 없는 경우, captcha가 뜬다.
    bvsd의 값에서 encData에는 네이버 로그인 창에서 마우스/키/디바이스 정보를 가지고 compressToEncodedURIComponent로 인코딩한 것
    
    로그인 창에서 post되는 bvsd의 값에서 encData만 뽑아와 decompressFromEncodedURIComponent로 디코딩하고 Formating을 알아내서 계속 써먹을 수 있다.
    """
    encData = '{"a":"%s-4","b":"1.3.4","d":[{"i":"id","b":{"a":["0,%s"]},"d":"%s","e":false,"f":false},{"i":"%s","e":true,"f":false}],"h":"1f","i":{"a":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}}' % (bvsd_uuid, id, id, pw)
    bvsd = '{"uuid":"%s","encData":"%s"}' % (bvsd_uuid, lzstring.LZString.compressToEncodedURIComponent(encData))
    #####################################

    post_data = {
        'encnm': encnm,
        'encpw': encpw.hex(),
        'bvsd': bvsd
    }

    res = s.post('https://nid.naver.com/nidlogin.login', data=post_data, headers=hdr)

    if res.text.count("\n") > 10:
        print("sign in fail.")
        sys.exit(-1)

    login_url = res.text[res.text.find("replace(\"")+9:res.text.find("\");")].strip()

    s.close()

    # 반환해주는 login_url을 접속하게 되면 naver에 로그인이 된다.
    return login_url


if __name__ == '__main__':
    id = str(input("Naver ID: "))
    pw = str(input("Naver PW: "))

    keyname, encpw = n_session(id, pw)
    login_url = sign_in_naver(keyname, encpw)

    print("네이버 로그인 url : " + login_url)