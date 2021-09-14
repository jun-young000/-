# Challenge goals:
# Using this boilerplate we are going to build a mini clone of the Hacker News Website using the Hacker News Search API and Flask.
# 해커뉴스 API와 Flask를 활용하여 해커뉴스 웹사이트 클론코딩을 진행합니다.
# 위의 힌트 (Clues)를 활용하여, 필요조건 (Requirements) 에 맞추어 과제를 완수하세요.
# 최종 결과 모습을 참고하세요.
# 클론코딩할 웹사이트는 다음과 같은 경로를 가집니다.
# /
# /?order_by=new
# /?order_by=popular
# /＜id＞
# 조건
# 강의 #4.6와 같은 fakeDB를 구현하여 'new' 및 'popular'가 더 빠르게 로드 될 수 있도록합니다.
# 클론 웹사이트는 order_by의 현재 선택 사항을 반영해야 합니다.
# 메인 페이지 "/"는 기본적으로 order_by가 popular로 선택되어야 합니다.
# 각 타이틀에 링크를 걸어 그 타이틀에 해당하는 모든 코멘트들을 볼 수 있도록 합니다.
# Nico's 힌트
# 코멘트에 작성자가 없는 경우에는 이 코멘트가 삭제되었음을 의미합니다.
# 코멘트를 가져올 때 HTML 태그에 영향을 주는 특수문자(&, >, <, ")가 포함되는 경우를 생각하여 Autoescaping 해주는 Flask의 safe 를 사용하세요.
# CSS는 신경 안 써도 됩니다. 보일러플레이트에 CSS파일을 포함하였습니다. <header>, <section>, <div>, <h1>와 같은 태그들을 사용하기만 해도 자동적으로 깔끔하게 보일 겁니다.
# API는 시간당 10,000건 이상의 요청을 할 수 없으니 주의하세요.