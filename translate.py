# 엑셀 파일 english 컬럼에 있는 영문장들을 판다스로 다 읽어서
# 번역기 함수에 집에 넣고 결과를 다시 엑셀파일 korean 컬럼에 넣어준다.

from api_papago import translator
import pandas as pd

# pip install openpyxl

data = pd.read_excel('english-1.xlsx', engine='openpyxl')
# print(data)

# dataframe.iterrows() 반복문 돌리면
# L은 행번호 row는 행내용
for l, row in data.iterrows():
    # print(row['english'])
    # translator(row['english'])
    # data.loc[l, 'korean'] => 데이터프레임.loc[행, 열]
    # row['korean'] = translator(row['english'])
    data.loc[l, 'korean'] = translator(row['english']) # = data.loc['korean'][l]
    # 아직 저장된게 아니어서 저장을 해야한다.
    data.to_excel('output.xlsx')
    # data.to_csv('output2.xlsx')