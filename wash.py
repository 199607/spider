import pandas as pd
from sqlalchemy import create_engine
import numpy as np

engine = create_engine('mysql+pymysql://root:root@localhost:3306/spider',encoding='utf-8')
sql = '''select * from 京东电脑;'''

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

data = pd.DataFrame(pd.read_sql(sql,engine))
# 数据处理---------------------------------------------

# 删除数据表中重复的数值
data.drop_duplicates()

# 对空值数据进行删除
data.dropna()

# 对数据进行分组****在数据表的价格字段记录了电脑价格，这里我们可以根据价格的多少对上商品进行分级
bins = [0, 1000, 5000, 8000,10000]
group_names = ['原始人笔记本', '办公型笔记本', '游戏本', '败家笔记本']
data['售价定位'] = pd.cut(data['价格'], bins, labels=group_names)

# 首先将评论中字符’+‘给去除，然后将’万‘转换成10000，最后将数据转化成int类型进行处理
data['评论']=data['评论'].str.split('+').str[0]
data['评论']=data['评论'].apply(lambda x:  float(x.split('万')[0])*10000 if x.split('万')[-1]=='' else float(x)).astype(int)

data.to_sql('京东电脑done',con=engine,if_exists='replace',index=False)
print(data)