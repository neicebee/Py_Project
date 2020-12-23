**random 라이브러리로 만드는 로또 번호 생성기**

# 📌 들어가기 전에

랜덤 정수를 배우고 나면 꼭 해봐야하는 프로젝트가 하나 있다.

바로 로또 번호 생성기이다.

로또 번호 생성뿐만 아니라 저번회차 당첨 번호도 크롤링해서 보여주는 코딩과 random 라이브러리의 기본적인 사용법, 핵심 내용인 번호 중복 제거를 설명할 것이다.

## 📌 Used Main Librarys

1. 랜덤 정수를 뽑을 `random`

2. 당첨 번호를 가져올 `requests`와 `bs4`

### 📌 Code Explanation

py 파일 내의 주석을 보면 코딩 이해가 쉬울 것이다.

중요한 것만 설명함

```python
    lotto_num = []
    lotto_num.append(random.randint(1, 45))
```

로또는 `1 ~ 45`의 범위에서 6개의 번호와 1개의 보너스 번호를 뽑는 방식이다.

`random.randint(1, 45)`는 1부터 45의 범위에서 하나의 정수를 반환해주는 메서드이다.

```python
    while(True):
        boolean = []
        a = random.randint(1, 45)

        for i in range(len(lotto_num)):
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
```

a에 lotto_num 리스트에 넣을 랜덤 정수를 넣고 중복체크하는 코딩이다. a가 lotto_num에 있는 숫자와 중복되지 않으면 그대로 append 해주고 lotto_num의 길이가 6이 됐을 때, break를 걸어 반복문을 깬다.

get_bonusnum 메서드도 비슷한 개념이다.

