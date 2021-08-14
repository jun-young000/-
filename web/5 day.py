import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")



print("hello,please choose selent a country by number:")

iban_result = requests.get("https://www.iban.com/currency-codes")
iban_soup = BeautifulSoup(iban_result.text, "html.parser")

tr = iban_soup.find("tr")
tds = iban_soup.find_all("td")


date = []


for tr in iban_soup.find_all("tr"):
  tds = list(tr.find_all("td"))
  if tr.find_all("td"):
        country=tds[0].text
        currency= tds[1].text
        code=tds[2].text
        number=tds[3].text
        date.append([country,currency,code,number])


for i in range(len(date)):
    print(f"# {i+1}", date[i][0])
    i=i+1


def  user_answer():


    try:
        answer= int(input("where areyou from? choose a country by number. \n #:"))
        if 0< answer<269:
            print(date[answer-1][0])    

        elif answer<1 or answer>268:
            print("choose from a number list.")
            user_answer()

    except:
        print("this in not a number.")
        user_answer()

    return answer

def user_answer_2():


    try:
        answer_2 = int(input(" \n Now choose another country,  \n #:"))
        if 0 < answer_2 < 269:
            print(date[answer_2-1][0]) 
        elif answer_2 < 1 or answer_2 > 268:  
            user_answer_2()  

    except:
        print("this in not a number.")
        user_answer_2()


    return answer_2()        



def converter():
    from_country = user_answer()
    to_country= user_answer_2()


    answer_3 = int(input(f"\n How many {date[from_country-1][1]} do you want to convert to {date[from_country-1][1]}? \n"))

    tw=requests.get(f" https://wise.com/gb/currency-converter/ {date[from_country][2]}-to-{date[to_country][2]}-rate?amount-{answer_3}")
    tw_soup = BeautifulSoup(tw.text, "html.parser")
    converted =float(iban_soup.find("span",{"calss":"text-success"}.text))
    result = float(converted*answer_3)

    print(f"{date[from_country-1][1]}{answer_3} is {date[to_country][1]}{result}")

    return result

converter()








# 학습 내용

# 1) 모듈설치
# 2) 가져올 페이지의 url요청 (get .text)
# 3) 원하는 html 파트 가져오기 (Beautiful Soup)
# 4) pagination 찾기
# 5-1) pagination 안의 모든 앵커 찾기
# 5-2) loop를 이용해 각 페이지의 "span" 모두 찾기
# 6) 불러올 페이지 넘버 지정해주기

# #1. Import Packages (모듈설치)
# -영상에서 쓰인 모듈 :
# ㄴRequest (사이트 정보 가져오기 (text))
# ㄴBeautiful Soup (html 내 필요한 부분 추출하기 (html))

# #2. 가져올 페이지의 url요청 (request.get)
# -페이지.text 가져왕

# #3. 원하는 html 파트 가져오기 (Beautiful Soup)
# -위 .text에서 HTML 불러왕 (html.parser)

# #4. HTML 내에서 내가 원하는 정보의 pagination(페이지 네비게이터)을 찾기(indeed_soup.find)
# ㄴ"div" 를 찾아서 "pagination" 클래스 불러와줭

# #5-1. pagination 안의 모든 앵커('a href' 형태로 되어있는 링크들) 찾아주기
# ㄴpagination.find_all('a'))

# #5-2. 페이지 링크마다 있는 태그를 각각 모두 불러와줘야 하므로 loop(for-in) 사용
# ㄴfor link in links: pages.append(link.find("span"))


# #6. 어디서부터 어디까지 불러올건지 페이지 넘버 지정해주기
# ㄴpages = pages[0:-1]




# TA's 정답 해설
# 1. 홈페이지에서 국가와 통화 목록 스크래핑 하기
# requests 모듈을 이용해 해당 홈페이지의 GET 요청을 보냅니다.
# BeautifulSoup 라이브러리를 사용하여 soup = BeautifulSoup(request.text, "html.parser") 
# 라는 코드를 작성하시면 해당 홈페이지의 html 코드들을 가져오실 수 있습니다.
# 필요한 정보는 국가들과 통화 코드들 입니다. 해당 정보가 있는 곳의 html코드를 보면 
# <table> 태그 안에 정보가 들어 있는 것을 확인할 수 있습니다.
# table = soup.find("table") 으로 <table> 코드 안에 있는 모든 html 코드들을 가져옵니다.
# <table> 코드 안에 있는 각각의 행들의 정보를 가져오기 위해
# rows = table.find_all("tr")[1:] 라는 코드를 작성합니다.
# table.find_all("tr")[1:] 뒷부분에 [1:] 이 붙는 이유는 <tr> 태그들의 맨 첫 번째
# 항목은 헤더 부분이기 때문에 이 부분은 필요가 없으므로 이를 제외하고 rows 리스트에 
# 저장 시키기 위해서입니다.
# rows 리스트에 저장된 각각의 행들의 정보를 차례로 가져오기 위해 for row in rows: 라는
#  반복문을 사용합니다.
# <tr> 태그 밑에는 4개의 <td> 태그가 존재합니다.
#  순서대로 나라 이름, 통화명, 통화 코드, 번호의 정보를 가지고 있습니다.
# items = row.find_all("td") 를 사용하여 4개의 <td> 태그에 담긴 정보들을 
# items 리스트에 저장합니다.
# 필요로 하는 정보는 국가 이름과 통화 코드 입니다. 국가 이름은 items[0] 에 
# 통화 코드는 items[2] 에 저장 되어 있으므로 .text 를 사용하여 문자만 추출합니다.
# 논리연산 and를 이용하여 만약 name 과 code 모두 값이 존재할 때만 작동한다는 
# 조건문 if name and code : 을 작성합니다.
# country 딕셔너리에 국가 이름과 통화 코드를 추가하기 위해
#  country = {'name':name.capitalize(),' code': code} 와 같은 코드를 작성합니다.
# countries.append(country) 로 countries 리스트 안에 country 딕셔너리를 넣어줍니다.
# 각 정보들은 리스트 안에 딕셔너리가 들어있는 아래와 같은 형태로 저장이 됩니다.
# [{'name': 'Afghanistan', 'code': 'AFN'}, {'name': 'Åland islands', 'code': 'EUR'},
#  ........]
# 
# 2.사용자에게 입력 번호 묻는 함수 ask()
# 사용자에게 입력을 받아 countries 리스트의 인덱스와 일치하는 정보를 출력해줍니다.
# 만약 숫자가 아닌 문자나 countries 리스트의 인덱스 외의 숫자를 입력 받으면 해당 정보를 
# 찾을 수 없다는 경고를 출력해주기 위해 try-except문을 사용합니다.
# 먼저 사용자에게 입력 받은 값을 choice = int(input("#: ")) 를 사용하여 정수형으로 
# 변환시켜줍니다.
# 단, 사용자가 "abcd" 같은 문자를 입력하면 위의 코드를 사용하여도 절대 정수로 변환시킬 
# 수 없는데 이러한 경우 "ValueError"가 발생하므로 except ValueError: 를 사용하여 
# 에러 처리를 해주면 됩니다.
# if choice >= len(countries) or choice <0: 를 사용하여 choice가 리스트의 
# 인덱스 범위보다 크거나 0보다 작으면 리스트 안에 있는 번호를 선택 하라는 메세지를 
# 출력시켜주고 ask() 함수를 다시 불러옵니다.
# 
# 3.프로그램 실행 시 국가 리스트들 모두 출력해주기
# 프로그램을 실행시키면 국가와 통화를 스크래핑 하여 그 결과를 차례로 번호를 매겨
#  모두 출력시켜야 됩니다.
# 스크래핑 해온 모든 정보가 담긴 countries 리스트를 번호를 매겨 차례로 출력 시키기 위해서
#  for문을 사용하여 아래와 같이 코딩해주시면 됩니다.
# enumerate는 "열거하다" 라는 의미로 자료형을 입력받으면 인덱스 값을 포함 시켜서 
# enumerate 객체를 돌려줍니다.
# enumerate(countries) 를 이용해 인덱스 값을 포함시켜 다시 돌려 받았으므로 적절히
# 포맷팅을 하여(위 사진 2번째 줄 참고) 챌린지 예시 동영상과 비슷한 형태로 출력되게 만들면 됩니다.


# 결론
# 그동안 강의에서 배웠던 requests 와 BeautifulSoup 라이브러리를 사용하여 웹 스크래핑을 
# 해보는 첫 챌린지였습니다.
# 웹 스크래핑을 할 땐 각각의 사이트마다 html 코드들이 다르므로 상황에 따라 다르게 코딩해야
#  되므로 여러 웹 사이트들을 스크래핑 하는 연습을 많이 하시는 것을 추천드립니다.




# 니코샘 코드

# import os
# import requests
# from bs4 import BeautifulSoup

# os.system("clear")


# url = "https://www.iban.com/currency-codes"


# countries = []

# request = requests.get(url)
# soup = BeautifulSoup(request.text, "html.parser")

# table = soup.find("table")
# rows = table.find_all("tr")[1:]

# for row in rows:
#   items = row.find_all("td")
#   name = items[0].text
#   code =items[2].text
#   if name and code:
#       country = {
#         'name':name.capitalize(),
#         'code': code
#       }
#       countries.append(country)


# def ask():
#   try:
#     choice = int(input("#: "))
#     if choice >= len(countries) or choice <0:
#       print("Choose a number from the list.")
#       ask()
#     else:
#       country = countries[choice]
#       print(f"You chose {country['name']}\nThe currency code is {country['code']}")
#   except ValueError:
#     print("That wasn't a number.")
#     ask()


# print("Hello! Please choose select a country by number:")
# for index, country in enumerate(countries):
#   print(f"#{index} {country['name']}")

# # ask()