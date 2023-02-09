import numpy as np
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.pyplot as fm
import datetime
from datetime import *


unpre_dust = pd.read_csv('./data/서울시 대기질 자료 제공_2016-2019.csv', encoding='cp949')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc0 in position 0: invalid start byte
# pd.read_csv의 함수 파라미터로 encoding='cp949' 입력 시 오류해결
unpre_dust.tail(10)

unpre_GN = unpre_dust[unpre_dust['구분'] == '강남구']
print(unpre_GN)

