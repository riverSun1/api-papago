import os
import sys
import urllib.request
import json # json에서 데이터를 뽑기위해 dictionary로 변환

def translator(text):
    client_id = " " # 개발자센터에서 발급받은 Client ID 값
    client_secret = " " # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(text)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read() ##
        # json에서 데이터를 뽑기위해 dictionary로 변환
        dic = json.loads(response_body) ##
        return dic['message']['result']['translatedText']
    else:
        return "Error Code:" + rescode

# {"message":{"result":{"srcLangType":"ko","tarLangType":"en","translatedText":"Nice to meet you.","engineType":"PRETRANS"},"@type":"response","@service":"naverservice.nmt.proxy","@version":"1.0.0"}}
# => 출력결과가 딕셔너리 비슷하다.

# 내 컴퓨터랑 네이버 서버랑 데이터를 주고 받았다.
# 이런식으로 랜선을 타고 data를 주고 받을 때는 딕셔너리 형태는 주고받을 수 없다.
# 순전히 text data만 주고 받을 수 있다.
# 딕셔너리 => { 'name' : 'john' }
# json => '{ "name" : "john" }' => 문자같은 취급을 받는다. text.

# json에서 데이터를 뽑아보자.
# response_body -> dictionary 변환