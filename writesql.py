import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os

path1 = 'D:\Program Files (x86)\Pycharmexsice\spd\shuju'

#
# df = pd.read_csv(path)
# df.to_sql('jingdon', con=engine, if_exists='replace', index=False)

for file in os.listdir(path1):
    file_name = os.path.join(path1,file)
    df = pd.read_csv(file_name,names=['电脑名称','价格','评论','店铺名'])  #name后面加列属性值
    engine = create_engine('mysql+pymysql://root:root@localhost:3306/spider')
    df.to_sql(file,con=engine,if_exists='replace',index=False)