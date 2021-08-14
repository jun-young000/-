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