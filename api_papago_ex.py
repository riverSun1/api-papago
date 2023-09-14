# 다량의 영문장을 번역을할때 Naver papago API를 이용하면 된다.
# 번역 ai가 아무리 잘 되었다고 해도 사람을 따라갈 순 없다.
# papago로 번역을 하면 번역이 어색하게 될 것이다.
# 실제 번역일 하는 사람들은 papago에 먼저 돌려서 결과를 내고
# 그걸 검수하는 식으로 번역을 다시해서 일을 한다.
# 처음부터 타이핑을 하는 것보다 훨씬 시간절약이 된다.
# 번역 ai를 만드는 것이 아니라 네이버 파파고의 서비스를 빌리는 것이다.

# API - 서버와 통신하는 방법/문법
# 예를 들어 네이버가 서비스를 하나 만들었는데 그게 너무 뛰어나서 자랑하고 싶은상황.
# 그래서 그 서비스들을 외부인들도 이용할 수 있게 만든게 API이다.

# 네이버 API - 네이버 서버랑 통신하는 방법.
# 네이버 파파고 API - 네이버 파파고 서버랑 통신하는 방법.
# 네이버 개발자 센터 => https://developers.naver.com/main/ 접속 후 로그인
# 애플리케이션 등록 (API 이용신청)
# 번역 > 파파고 번역 > WEB설정 > http://localhost

import os
import sys
import urllib.request
client_id = "YOUR_CLIENT_ID" # 개발자센터에서 발급받은 Client ID 값
client_secret = "YOUR_CLIENT_SECRET" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)