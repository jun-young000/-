import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")


def write_company(company):
    file = open(f"{company['name']}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in company["jobs"]:
      writer.writerow(list(job.values()))


alba_url = "http://www.alba.co.kr"

alba_request = requests.get(alba_url)
alba_soup = BeautifulSoup(alba_request.text, "html.parser")
main = alba_soup.find("div", {"id": "MainSuperBrand"})
brands = main.find_all("li", {"class": "impact"})
for brand in brands:
    link = brand.find("a", {"class": "goodsBox-info"})
    name = brand.find("span", {"class": "company"})
    if link and name:
        link = link["href"]
        name = name.text
        company = {'name': name, 'jobs': []}
        jobs_request = requests.get(link)
        jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")
        tbody = jobs_soup.find("div", {"id": "NormalInfo"}).find("tbody")
        rows = tbody.find_all("tr", {"class": ""})
        for row in rows:
            local = row.find("td", {"class": "local"})
            if local:
                local = local.text.replace(u'\xa0', ' ')
            title = row.find("td", {"class": "title"})
            if title:
                title = title.find("a").find("span", {
                    "class": "company"
                }).text.strip()
                title = title.replace(u'\xa0', ' ')
            time = row.find("td", {"class": "data"})
            if time:
                time = time.text.replace(u'\xa0', ' ')
            pay = row.find("td", {"class": "pay"})
            if pay:
                pay = pay.text.replace(u'\xa0', ' ')
            date = row.find("td", {"class": "regDate"})
            if date:
                date = date.text.replace(u'\xa0', ' ')
            job = {
                "place": local,
                "title": title,
                "time": time,
                "pay": pay,
                "date": date
            }
            company['jobs'].append(job)
        write_company(company)

# 강사님 코드
import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")


def write_company(company):
    file = open(f"{company['name']}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in company["jobs"]:
      writer.writerow(list(job.values()))
    print(f"Completed....{company['name']}")


alba_url = "http://www.alba.co.kr"

alba_request = requests.get(alba_url)
alba_soup = BeautifulSoup(alba_request.text, "html.parser")
main = alba_soup.find("div", {"id": "MainSuperBrand"})
brands = main.find_all("li", {"class": "impact"})
for brand in brands:
    link = brand.find("a", {"class": "goodsBox-info"})
    name = brand.find("span", {"class": "company"})
    if link and name:
        link = link["href"]
        name = name.text
        if "/" in name :
          name = name.replace("/"," ")
        company = {'name': name, 'jobs': []}
        jobs_request = requests.get(link)
        jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")
        tbody = jobs_soup.find("div", {"id": "NormalInfo"}).find("tbody")
        rows = tbody.find_all("tr", {"class": ""})
        for row in rows:
            local = row.find("td", {"class": "local"})
            if local:
                local = local.text
            title = row.find("td", {"class": "title"})
            if title:
                title = title.find("a").find("span", {
                    "class": "company"
                }).text.strip()

            time = row.find("td", {"class": "data"})
            if time:
                time = time.text
            pay = row.find("td", {"class": "pay"})
            if pay:
                pay = pay.text
            date = row.find("td", {"class": "regDate"})
            if date:
                date = date.text
            job = {
                "place": local,
                "title": title,
                "time": time,
                "pay": pay,
                "date": date
            }
            company['jobs'].append(job)
        write_company(company)

#         ##TA's 정답 해설
# 알바천국 홈페이지에서 슈퍼브랜드 채용 회사 정보 가져오기 (Line 18 ~ 32)
# Line 18 ~ 21 : requests 와 beautifulSoup 라이브러리를 사용하여 알바천국 홈페이지에서 정보를 긁어 올 준비를 합니다.
# 알바천국 홈페이지를 inspect 해보면 슈퍼브랜드 채용 정보는 id가 MainSuperBrand인 <div> 태그 안에 담겨있는 것을 확인할 수 있습니다.
# main = alba_soup.find("div", {"id": "MainSuperBrand"})
# 위와 같이 입력하여 슈퍼브랜드 채용 정보만 긁어옵니다.
# 더 자세히 들어가면 <ul> 태그 밑에 <li> 태그 들이 존재하는데 각각의<li> 안에 회사 정보가 들어있습니다.
# main 변수에 저장되어있는 html 코드들 중에 모든 <li> 태그들만 가져오기 위해 아래와 같이 작성해줍니다.
# brands = main.find_all("li", {"class": "impact"})
# 위의 코드는 main에 저장 되어 있는 html 코드 중에 클래스 이름에 "impact"가 포함된 <li> 태그들을 모두 찾아 brands 리스트에 저장합니다.
# Line 24 ~ 26 : for문을 사용하여 brands 리스트에 저장 된 정보들을 차례로 하나씩 꺼내 회사의 링크와 회사명만 뽑아서 link, name 변수에 저장합니다.
# 회사 링크는 클래스 명에 "goodsBox-info"가 포함된 a 태그 안에 있고 회사 명은 클래스 명에 "company"가 포함된 span 태그 안에 있습니다.
# Line 27 ~ 29 : 필요로하는 정보의 html 코드가 담긴 변수들(name, link) 에서 텍스트만 뽑아내야 됩니다.
# 혹시 모르니 if link and name: 을 작성하여 link와 name 모두 공백이 아닐때만 실행시켜주도록 하는 조건문을 사용합니다.
# <a> 태그에서 링크는 "href" 라는 속성에 담겨있습니다.
# link = link["href"]
# 위에 적혀있는 코드는 link 변수에 link에 저장되어있는 html 코드에서 href 속성에 담겨있는 값만 추출하여 덮어쓰기 해줍니다.
# 참고문서 : Attributes
# name도 name = name.text 로 텍스트만 뽑아서 저장해줍니다.
# Line 30 ~ 31 : 만약 회사 명에 파일 이름으로 쓸 수없는 특수문자(/, *, \, : 등) 가 있다면 .replace() 를 사용하여 다른 문자로 치환해줍니다.
# 각 회사별 홈페이지로 들어가서 일자리 정보 가져오기 (Line 33 ~ 63)
# company 라는 딕셔너리를 생성합니다. company 딕셔너리 안에는 회사명을 넣어주고 일자리들을 저장할 빈 리스트 선언해줍니다.
# Line 33 ~ 34 : requests 와 beautifulSoup 라이브러리를 사용하여 link 변수에 저장되어 있는 회사 링크 안에 들어있는 일자리 정보들을 긁어오기 위해 준비합니다.
# 각각의 일자리에서 가져와야 될 정보는 근무지(local), 회사명(title), 근무시간(time), 급여(pay), 등록일(date) 입니다.
# Line 35 ~ 55 : 위에서 슈퍼브랜드 채용에서 회사 정보들을 가져왔던 것과 마찬가지로 일자리 정보가 담겨 있는 태그를 찾아 세부적으로 들어가서 원하는 정보를 추출하면 됩니다.
# 단, 일자리 정보를 잘 보면 각각의 <tr> 태그에 들어가 있는 것을 확인할 수 있는데 <tr> 태그들 중에서도 class가 없는 태그들에만 제대로 된 정보가 들어가 있습니다.
# 따라서 class가 없는 <tr> 태그들만 가져오기 위해 아래와 같이 작성합니다.
# rows = tbody.find_all("tr", {"class": ""}) (36번째 줄 참고)
# Line 56 ~ 62 : 추출한 정보들(local, title, time, pay, date)를 job 딕셔너리 안에 넣어줍니다.
# Line 63 : 32번째 줄에서 생성하였던 company 딕셔너리 안에 있는 job 리스트에 방금 만들었던 job 딕셔너리를 추가해줍니다.
# company 딕셔너리에는 다음과 같은 형태로 정보들이 저장 됩니다.
# company = {'name' : '이마트' , 'jobs' : [{"place": "서울", "title" : "asdf".....}, {"place" : "경기", "title" : "111111".....}]}
# 추출한 정보가 저장된 company 딕셔너리를 csv 파일로 내보내기 위해 write_company(company) 를 실행시켜줍니다.
# write_company(company) 함수 (Line 9 ~ 15)
# 추출한 정보들을 csv 파일로 만들기 위한 함수입니다.
# 참고문서 : CSV 파일 읽기와 쓰기
# Line 10 : csv 파일 이름은 회사 명으로 지정합니다.
# Line 12 : 일자리 정보들을 넣기 전에 먼저 .writerow 를 사용하여 헤더를 추가해줍니다.
# for문을 이용하여 company 딕셔너리의 "jobs"의 value 값만 csv 파일에 추가합니다.
# 결론
# 그동안 연습했던 requests 와 beautifulSoup 라이브러리를 이용하여 홈페이지의 정보를 긁어오는 것뿐만 아니라 그 정보들을 csv 파일로 저장하는 연습을 할 수 있었던 난이도가 조금 있는 챌린지였습니다.
# 나중에 데이터 분석을 하게 된다면 데이터 수집을 할 때 이번 챌린지에서 연습한 것이 도움이 될 것입니다.