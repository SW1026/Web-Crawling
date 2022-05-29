# Web-Crawling


[크롤링방법]

1. html \\ index.html 파일 크롤링
   1-1. open()을 이용하여 파일 로드
        file = open("html\\index.html", "r")
        read = file.read()

   1-2. bs4.BeautifulSoup() 이용해 html 파싱
        html = bs4.BeautifulSoup(read, 'html.parser')

   1-3. find(), find_all()을 이용해 태그 분석

2. http://192.168.0.1xx/index.html 파일 크롤링
   2-1. requests.get()을 이용하여 웹접속
        response = requests.get("http://192.168.0.1xx/index.html")
                   응답내용: response = http.header + content
        content  = response.content

   2-2. bs4.BeautifulSoup() 이용해 html 파싱
        html = bs4.BeautifulSoup(content, 'html.parser')

   2-3. find(), find_all()을 이용해 태그 분석
