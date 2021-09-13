# 환전 결과 값을 나타내는 "Convert to"의 value값은 홈페이지 코드 변경으로 인해 가져올 수 없으니 다른 방식으로 접근하셔야 합니다.
# 홈페이지에서 환전 정보를 가져올 때 requests 와 beautifulSoup 라이브러리만 이용하여도 충분히 가져올 수 있는 방법이 존재합니다.
# 예를 들어, 미국 2달러(Amount)를 한국 돈으로 환전하고 싶으면 홈페이지 Converted to 아랫부분에 “1 USD = 1108.30000 KRW” 라고 1달러당 현재 환율이 표기되어 있는데 “1108.30000” 부분을 추출해서 Amount와 곱해주시면 구하고자 하는 환전 값을 얻을 수 있습니다.
# 블루프린트에 작성되어 있는 format_currency(5000, "KRW", locale="ko_KR")는 5000이란 숫자를 한국 통화(KRW) 형식으로 변환하여 “₩5,000”으로 출력시켜줍니다. 만약 달러 형식으로 변환하고 싶다면 “KRW” 대신 “USD”를 넣어 “$5,000.00”의 결과값을 얻을 수 있습니다.
# 참고문서 : format_currency()




import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from day5 import play5

os.system("clear")



def comefileday5():
  biglist = play5.firstwork()
  return biglist

def finding(biglist):  
  country = input("#: ")
  if country.isdecimal():
    number = int(country)
    if number <= len(biglist):
      print(biglist[number][1])
      return number
    else:
      print("Choose a number from the list.")
      return finding(biglist)
  else:
    print("That wasn\'t a number.")
    return finding(biglist)

def money(papper1,papper2):  
  print(f"\nHow many {papper1} do you want to convert to {papper2}?")
  moneyback = input()
  if moneyback.isdecimal():
    number = int(moneyback)
    return number
  else:
    print("That wasn\'t a number.")
    return money(papper1,papper2)

  

def extractmoney(money1, money2, mymoney):
  result = requests.get(f"https://transferwise.com/gb/currency-converter/{money1}-to-{money2}-rate?amount={mymoney}")
  soup = BeautifulSoup(result.text,"html.parser")
  change = soup.find_all('input',{"id":"rate"})
  
  listdata = []

  for form in change:
    listdata.append(form)
  listsimple=str(listdata[0]).split()
  for i in listsimple:
    if 'value' == i[0:5]:
      moneychange = float(i[7:-3])
      done = float(mymoney)*moneychange
      print(format_currency(float(mymoney), money1.upper(), locale="ko_KR"),end= '')
      print(' is ',end='')
      print(format_currency(done, money2.upper(), locale="ko_KR"))

  



def startgame():  
  print("Welcome to CurrencyConvert PRO 2000")
  biglist = comefileday5()
  print("\nWhere are you from? Choose a country by number.\n")
  country_num1 = biglist[finding(biglist)][3]
  print("\nNow choose another country.\n")
  country_num2 = biglist[finding(biglist)][3]
  mymoneyback = money(country_num1.upper(),country_num2.upper())
  extractmoney(country_num1.lower(),country_num2.lower(),mymoneyback)


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))


print(format_currency(5000, "KRW", locale="ko_KR"))
"""




### 니코샘 코드
# import os
# import requests
# from bs4 import BeautifulSoup
# from babel.numbers import format_currency

# os.system("clear")


# code_url = "https://www.iban.com/currency-codes"
# currency_url = "https://transferwise.com/gb/currency-converter/"


# countries = []

# codes_request = requests.get(code_url)
# codes_soup = BeautifulSoup(codes_request.text, "html.parser")

# table = codes_soup.find("table")
# rows = table.find_all("tr")[1:]

# for row in rows:
#   items = row.find_all("td")
#   name = items[0].text
#   code =items[2].text
#   if name and code:
#     if name != "No universal currency":
#       country = {
#         'name':name.capitalize(),
#         'code': code
#       }
#       countries.append(country)


# def ask_country(text):
#   print(text)
#   try:
#     choice = int(input("#: "))
#     if choice > len(countries):
#       print("Choose a number from the list.")
#       return ask_country(text)
#     else:
#       print(f"{countries[choice]['name']}")
#       return countries[choice]
#   except ValueError:
#     print("That wasn't a number.")
#     return ask_country(text)


# def ask_amount(a_country, b_country):
#   try:
#     print(f"\nHow many {a_country['code']} do you want to convert to {b_country['code']}?")
#     amount = int(input())
#     return amount
#   except ValueError:
#     print("That wasn't a number.")
#     return ask_amount(a_country, b_country)
  


# print("Welcome to CurrencyConvert PRO 2000\n")
# for index, country in enumerate(countries):
#   print(f"#{index} {country['name']}")

# user_country = ask_country("\nWhere are you from? Choose a country by number.\n")
# target_country = ask_country("\nNow choose another country.\n")


# amount = ask_amount(user_country, target_country)

# from_code = user_country['code']
# to_code = target_country['code']

# currency_request = requests.get(f"{currency_url}{from_code}-to-{to_code}-rate?amount={amount}")
# currency_soup = BeautifulSoup(currency_request.text, "html.parser")
# result = currency_soup.find("input", {"id":"cc-amount-to"})
# if result:
#   result = result['value']
#   amount = format_currency(amount, from_code, locale="ko_KR")
#   result = format_currency(result, to_code, locale="ko_KR")
#   print(f"{amount} is {result}")
#
# ask_country(text) 함수 (Line 34 ~ 46)
# 지난 시간에 완성했던 ask() 함수와 거의 비슷하나 43번째 줄에서 countries[choice] 값을
# 리턴해주는 부분이 추가되었습니다.
# user_country, target_country 값 구하기 (Line 64 ~ 65)
# ask_country(text) 함수를 불러와 사용자가 고른 나라의 이름과 통화 코드를 저장 시켜줍니다.
# user_country, target_country 모두 같은 방식으로 동작합니다.
# amount 값 구하기 (Line 68)
# 사용자가 얼마만큼의 돈을 환전할지 알아내야 합니다.
# 그러기 위해선 ask_amount 함수를 작성하여 인자 값으로 user_country, target_country 를 보내야합니다.
# ask_amount(a_country, b_country) 함수 (Line 49 ~ 56)
# 사용자가 선택한 두 나라의 정보를 인자 값으로 받아왔습니다.
# 두 나라의 정보는 오로지 사용자에게 질문을 던지는 출력문에만 쓰입니다.
# amount = int(input()) 을 사용하여 사용자에게 환전할 돈의 양을 묻습니다.
# 돈은 숫자이므로 반드시 int() 로 감싸서 형변환 시켜줍니다.
# 그리고 amount 값을 리턴 시켜줍니다.
# 사용자가 만약 숫자가 아닌 문자를 입력했을 경우를 대비하여 try-except문을 사용하여 예외처리를 해줍니다.
# 사용자가 선택한 두 나라의 통화 코드(from_code, to_code) 가져오기 (Line 70 ~ 71)
# 2번에서 구한 user_country, target_country 값을 이용하여 간단히 통화 코드를 가져올 수 있습니다.
# 각각의 새로운 변수에 user_country['code'] , target_country['code'] 를 넣어주시면 오로지 통화
# 코드만 저장되는 것을 볼 수 있습니다.
# 홈페이지에서 환전 결과를 가져오기 (Line 73 ~ 80)
# 스크래핑을 하기에 앞서, requests 라이브러리를 이용하여 Transfer Wise 홈페이지에 HTTP 요청을 보내야합니다.
# 사용자로부터 입력을 받은 정보들을 URL에 포맷팅하여 GET 방식으로 HTTP 요청을 아래와 같은 코드로 보냅니다.
# currency_request = requests.get(f"{currency_url}{from_code}-to-{to_code}-rate?amount={amount}")
# beautifulSoup 라이브러리를 사용하여 해당 홈페이지의 html 코드들을 가져옵니다.
# 위의 사진은 환전 결과 값을 가져오기 위해 크롬 개발자 도구에서 inspect한 결과입니다.
# 홈페이지의 코드 변경으로 인해 환전 결과의 value 값을 가져올 수 없습니다.
# 그러므로 환전 결과 값을 가져오는 것이 아니라 다른 방법으로 접근하여야 됩니다.
# 홈페이지 하단에 보시면 1 COP = 0.30937 KRW 이라는 값이 있는데 초록색 글씨로 되어있는 0.30937 을
# 긁어와서 amount 값이랑 곱해주는 것으로 환전 결과 값을 얻을 수 있습니다.
# 저 초록색 값을 가져오기 위해 rate = currency_soup.find("span", {"class":"text-success"}).get_text()
# 이라는 코드를 작성해줍니다.
# 혹시 rate 값이 존재하지 않을 경우도 생각하여 if rate: 를 사용하여 rate 값이 존재할 때만
# 환전 값을 구하도록 코드를 작성합니다.
# 위에서 구한 rate 값을 float 형식으로 변환한 다음 amount 값이랑 곱하여 환전 값을 구하기 위해 아래와 같이 작성합니다.
# result = float(rate) * amount
# 마지막으로 환전할 돈의 양(amount) , 환전 결과(result) 를 format_currency() 를 이용하여 통화 형식으로
# 포맷 시켜줍니다.

# 결론
# 홈페이지의 코드 변경으로 인해 환전 결과 값을 바로 가져올 수 없게 되어 다른 방법을 생각해서 해결해야 되
# 는 챌린지였습니다.
# 같은 홈페이지여도 시간이 지남에 따라 html코드가 변경 되는 경우가 꽤 있으므로 주의하여야 합니다.