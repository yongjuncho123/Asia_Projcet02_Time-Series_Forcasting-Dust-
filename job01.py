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
unpre_GN = unpre_dust[unpre_dust['구분'] == '강남구']
print(unpre_GN)
unpre_GN.isna().sum()
unpre_GN = unpre_GN.loc[::-1]
print(unpre_GN)

# 전처리
unpre_GN['일시'] = pd.to_datetime(unpre_GN['일시'])
unpre_GN.set_index('일시', inplace=True)
print(unpre_GN)



while unpre_GN['미세먼지(PM10)'].isna().sum() and unpre_GN['초미세먼지(PM25)'].isna().sum() != 0:
    unpre_GN[['미세먼지(PM10)', '초미세먼지(PM25)']] = unpre_GN[['미세먼지(PM10)', '초미세먼지(PM25)']].fillna(unpre_GN[['미세먼지(PM10)', '초미세먼지(PM25)']].rolling('3H', min_periods=1).mean())

unpre_GN.isna().sum()

unpre_GN.to_csv('./DATA/cleaned/pre_GN.csv')















import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame({'date': ['2023-02-14 00:00:00', '2023-02-14 01:00:00', '2023-02-14 02:00:00', '2023-02-14 03:00:00'],
                   'value1': [10, 20, 30, 40],
                   'value2': [5, np.nan, 8, np.nan],
                   'value3': [15, 25, 35, 45],
                   'value4': [12, np.nan, 18, np.nan]})

# Convert the date column to a datetime data type
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the dataframe index
df.set_index('date', inplace=True)

# Fill missing values with the average of the past three hours
df[['value2', 'value4']] = df[['value2', 'value4']].fillna(df[['value2', 'value4']].rolling('3H', min_periods=1).mean())

print(df)