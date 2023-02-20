import numpy as np
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.pyplot as fm
import datetime
from datetime import *


unpre_dust = pd.read_csv('./DATA/서울시 대기질 자료 제공_2016-2019.csv', encoding='cp949')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc0 in position 0: invalid start byte
# pd.read_csv의 함수 파라미터로 encoding='cp949' 입력 시 오류해결

# 데이터 구조 살펴보기
unpre_dust.info()
unpre_dust.tail(10)
unpre_dust.isna().sum()
unpre_dust.describe()

# 강남구만 뽑기
unpre_GS = unpre_dust[unpre_dust['구분'] == '강서구']
print(unpre_GS)
unpre_GS.isna().sum()
unpre_GS = unpre_GS.loc[::-1]
print(unpre_GS)

# 전처리
unpre_GS['일시'] = pd.to_datetime(unpre_GS['일시'])
unpre_GS.set_index('일시', inplace=True)
print(unpre_GS)



while unpre_GS['미세먼지(PM10)'].isna().sum() and unpre_GS['초미세먼지(PM25)'].isna().sum() != 0:
    unpre_GS[['미세먼지(PM10)', '초미세먼지(PM25)']] = unpre_GS[['미세먼지(PM10)', '초미세먼지(PM25)']].fillna(unpre_GS[['미세먼지(PM10)', '초미세먼지(PM25)']].rolling('3H', min_periods=1).mean())

unpre_GS[unpre_GS['미세먼지(PM10)'].isnull()]

unpre_GS.to_csv('./DATA/cleaned/pre_GS.csv')